from typing import List

from lib.parser.submission.base import SubmissionParser


class LeetCodeSubmissionParser(SubmissionParser):
    def __init__(self,
                 copyright_present: bool = True,
                 file_description_present: bool = True,
                 changelog_present: bool = True,
                 include_and_using_present: bool = True,
                 base_class_present: bool = False,
                 implementation_present: bool = True,
                 main_present: bool = False):
        super().__init__(copyright_present, file_description_present,
                         changelog_present, include_and_using_present,
                         base_class_present, implementation_present,
                         main_present)

    def read_solution(self, lines: List[str], idx: int) -> tuple[List[str], int]:
        number_of_lines = len(lines)
        answer = []
        start, end = False, False
        while idx < number_of_lines:
            if "namespace Solution" in lines[idx]:
                start = True
            if "// namespace Solution" in lines[idx]:
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
