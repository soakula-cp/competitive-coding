import os
from typing import List

from lib.problem.base import Problem
from lib.submission.base import AlgorithmMetadata, JudgeMetadata, Submission
from lib.utils.functions import remove_comments


class SubmissionParser(object):
    def __init__(self,
                 copyright_present: bool = True,
                 file_description_present: bool = True,
                 changelog_present: bool = True,
                 include_and_using_present: bool = True,
                 base_class_present: bool = True,
                 implementation_present: bool = True,
                 main_present: bool = True):
        self.solution = {
            'copyright': copyright_present,
            'file_description': file_description_present,
            'changelog': changelog_present,
            'include_and_using': include_and_using_present,
            'base_class': base_class_present,
            'implementation': implementation_present,
            'main': main_present,
        }

    def read_comment_block(self, lines: List[str], idx: int):
        number_of_lines = len(lines)
        answer = []
        start, end = False, False
        while end is False and idx < number_of_lines:
            if "clang-format off" in lines[idx]:
                idx += 1
                continue
            if "/**" in lines[idx]:
                start = True
            if "*/" in lines[idx]:
                end = True
            if start is True:
                answer.append(lines[idx].rstrip("\n"))
            idx += 1
        return answer, idx

    def read_copyright_notice(self, lines: List[str], idx: int):
        return self.read_comment_block(lines, idx)

    def read_file_description(self, lines: List[str], idx: int):
        return self.read_comment_block(lines, idx)

    def read_changelog(self, lines: List[str], idx: int):
        return self.read_comment_block(lines, idx)

    def read_include_and_usings(self, lines: List[str], idx: int):
        number_of_lines = len(lines)
        answer = []
        while idx < number_of_lines:
            if "clang-format off" in lines[idx]:
                break
            if "clang-format on" in lines[idx]:
                idx += 1
                continue
            if "namespace" in lines[idx]:
                break
            answer.append(lines[idx].rstrip("\n"))
            idx += 1
        return answer, idx

    def read_solution(self, lines: List[str], idx: int) -> (List[str], int):
        number_of_lines = len(lines)
        answer = []
        start, end = False, False
        while idx < number_of_lines:
            if "// clang-format off" in lines[idx]:
                start = True
            if "};" in lines[idx]:
                end = True
            if "int main" in lines[idx]:
                answer.clear()
                break
            if start:
                answer.append(lines[idx].rstrip("\n"))
            idx += 1
            if end:
                break
        return answer, idx

    def read_solutions(self, lines: List[str], idx: int) -> (List[List[str]], int):
        number_of_lines = len(lines)
        infos = []
        while idx < number_of_lines:
            info, idx = self.read_solution(lines, idx)
            if len(info) == 0:
                break
            infos.append(info)
        return infos, idx

    def read_solutions_file(self, file: str) -> \
        (List[str], List[List[str]]):
        if not os.path.exists(file):
            print(f"Filename: {file} doesn't exist")
            return []
        fp = open(file, "r", encoding="UTF-8")
        lines = fp.readlines()
        fp.close()
        idx = 0
        base_solution = None
        solutions = None
        if self.solution['copyright'] is True:
            copyright_notice, idx = self.read_copyright_notice(lines, idx)
        if self.solution['file_description'] is True:
            file_description, idx = self.read_file_description(lines, idx)
        if self.solution['changelog'] is True:
            changelog, idx = self.read_changelog(lines, idx)
        if self.solution['include_and_using'] is True:
            includes_and_usings, idx = self.read_include_and_usings(lines, idx)
        if self.solution['base_class'] is True:
            base_solution, idx = self.read_solution(lines, idx)
        if self.solution['implementation'] is True:
            solutions, idx = self.read_solutions(lines, idx)
        if self.solution['main'] is True:
            main_func = lines[idx:]
        return base_solution, solutions

    def extract_metadata(self, lines: List[str]) -> \
        (JudgeMetadata, AlgorithmMetadata):
        judge_metadata_found, algorithm_metadata_found = False, False
        judge_metadata, algorithm_metadata = JudgeMetadata(), AlgorithmMetadata()
        for line in lines:
            if "Judge metadata" in line:
                algorithm_metadata_found = False
                judge_metadata_found = True
            if "Algorithm metadata" in line:
                judge_metadata_found = False
                algorithm_metadata_found = True
            if judge_metadata_found:
                line = line.replace("*", "").replace("-", "").replace(":", "").strip()
                if "Submission link" in line:
                    judge_metadata.url = \
                        line.replace("Submission link", "").strip()
                if "Status" in line:
                    judge_metadata.status = \
                        line.replace("Status", "").strip()
                if "Runtime" in line:
                    judge_metadata.runtime = \
                        line.replace("Runtime", "").strip()
                if "Memory usage" in line:
                    judge_metadata.memory = \
                        line.replace("Memory usage", "").strip()
            if algorithm_metadata_found:
                line = line.replace("*", "") \
                    .replace("-", "").replace(":", "").strip()
                if "Time complexity" in line:
                    algorithm_metadata.time_complexity = \
                        line.replace("Time complexity", "").strip()
                if "Space complexity" in line:
                    algorithm_metadata.space_complexity = \
                        line.replace("Space complexity", "").strip()
                if "Tags" in line:
                    algorithm_metadata.tags = \
                        line.replace("Tags", "").strip().split(",")
                if "Categories" in line:
                    algorithm_metadata.categories = \
                        line.replace("Categories", "").strip().split(",")
        return judge_metadata, algorithm_metadata

    def extract_submission(self, problem: Problem, file: str) -> List[Submission]:
        base_solution, solutions = self.read_solutions_file(file)
        base_solution_code = remove_comments(base_solution)
        submissions = []
        for identifier, solution in enumerate(solutions):
            solution_code = remove_comments(solution)
            solution_metadata = self.extract_metadata(solution)
            submission = Submission(
                problem=problem,
                identifier=identifier + 1,
                code=solution_code,
                judge_metadata=solution_metadata[0],
                algorithm_metadata=solution_metadata[1],
            )
            submissions.append(submission)
        return submissions
