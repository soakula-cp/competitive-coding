import os
from typing import List

from slugify import slugify

from lib.submission.base import Submission


class Parser(object):
    def __init__(self,
                 solution_copyright: bool = True,
                 solution_changelog: bool = True,
                 solution_file_description: bool = True,
                 solution_include_and_using: bool = True,
                 solution_base_class: bool = True,
                 solution_implementation: bool = True,
                 solution_main: bool = True):
        pass

    def read_comment_block(self, lines: List[str], idx: int):
        number_of_lines = len(lines)
        answer = []
        start, end = False, False
        while end is False or idx < number_of_lines:
            if "clang-format off" in lines[idx]:
                idx += 1
                continue
            if "/**" in lines[idx]:
                start = True
            if "*/" in lines[idx]:
                end = True
            if start is True:
                answer.append(lines[idx].rstrip())
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
                idx += 1
                continue
            if "clang-format on" in lines[idx]:
                idx += 1
                continue
            if "namespace" in lines[idx]:
                break
            answer.append(lines[idx].rstrip())
            idx += 1
        return answer, idx

    def read_solution(self, lines: List[str], idx: int):
        number_of_lines = len(lines)
        answer = []
        start, end = False, False
        while idx < number_of_lines:
            if "clang-format off" in lines[idx]:
                idx += 1
                continue
            if "clang-format on" in lines[idx]:
                idx += 1
                continue
            if "namespace" in lines[idx]:
                start = True
            if "// namespace" in lines[idx]:
                end = True
            if start:
                answer.append(lines[idx].rstrip())
            idx += 1
            if end:
                break
        return answer, idx

    def read_solutions(self, lines: List[str], idx: int) -> List[List[str]]:
        number_of_lines = len(lines)
        infos = []
        while idx < number_of_lines:
            info, idx = self.read_solution(lines, idx)
            infos.append(info)
        return infos

    def read_solutions_file(self, file: str) -> List[List[str]]:
        if not os.path.exists(file):
            print(f"Filename: {file} doesn't exist")
            return []
        fp = open(file, "r", encoding="UTF-8")
        lines = fp.readlines()
        fp.close()
        idx = 0
        copyright_notice, idx = self.read_copyright_notice(lines, idx)
        file_description, idx = self.read_file_description(lines, idx)
        changelog, idx = self.read_changelog(lines, idx)
        include_and_usings, idx = self.read_include_and_usings(lines, idx)
        solutions = self.read_solutions(lines, idx)
        return solutions
