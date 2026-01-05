import markdownify

from lib.api.advent_of_code import AdventOfCodeApi
from lib.file.base import BaseFileWrite
from lib.problem.advent_of_code import AdventOfCodeProblem
from lib.utils.enums import WriteContentEnum
from lib.utils.functions import get_lines_in_a_file


class AdventOfCodeFileWrite(BaseFileWrite):
    def __init__(self,
                 template_root_directory: str,
                 solution_include_and_using: bool = True,
                 solution_base_class: bool = True,
                 solution_main: bool = True):
        """

        Args:
            template_root_directory:
            solution_include_and_using:
            solution_base_class:
            solution_main:
        """
        super().__init__(
            template_root_directory=template_root_directory,
            solution_include_and_using=solution_include_and_using,
            solution_base_class=solution_base_class,
            solution_main=solution_main)

    def create_file_for_tests(
        self,
        problem: AdventOfCodeProblem,
        output_directory: str,
        should_overwrite: bool = False) -> (bool, str):
        question = AdventOfCodeApi().get_question_info(problem)
        tests = question['exampleTestcases'].split('\n')
        input_filename = f"{output_directory}\\Examples.in.txt"
        filep = open(input_filename, "w")
        filep.write(f"{len(tests)}\n")
        for test in tests:
            filep.write(f"{test}\n")
        filep.close()
        return True, ""

    def create_file_for_problem(
        self,
        problem: AdventOfCodeProblem,
        root_directory: str,
        write_type: WriteContentEnum,
        should_overwrite: bool = False) -> None:
        already_setup, output_file_path = super().create_file_for_problem(
            problem, root_directory, write_type,
            should_overwrite=should_overwrite)
        if write_type == WriteContentEnum.TESTCASES:
            return
        question = AdventOfCodeApi().get_question_info(problem)
        lines = get_lines_in_a_file(output_file_path)
        for idx in range(len(lines)):
            lines[idx] = BaseFileWrite.update_file_line(lines[idx], problem)
            if "TEMPLATE__PROBLEM_CONTENT" in lines[idx]:
                lines[idx] = \
                    lines[idx].replace(
                        "TEMPLATE__PROBLEM_CONTENT",
                        markdownify.markdownify(question['description'],
                                                heading_style="ATX"))
            if "TEMPLATE__PROBLEM_ID" in lines[idx]:
                lines[idx] = \
                    lines[idx].replace(
                        "TEMPLATE__PROBLEM_ID", question['identifier'])
        with open(output_file_path, "w", encoding="utf-8") as file:
            file.write(''.join(lines))
