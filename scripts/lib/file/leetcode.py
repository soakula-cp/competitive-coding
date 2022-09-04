import markdownify

from lib.api.leetcode import LeetCodeApi
from lib.file.base import BaseFileWrite
from lib.problem.leetcode import LeetCodeProblem
from lib.utils.enums import WriteContentEnum
from lib.utils.functions import get_lines_in_a_file


class LeetCodeFileWrite(BaseFileWrite):
    def __init__(self,
                 template_root_directory: str,
                 solution_include_and_using: bool = False,
                 solution_base_class: bool = False,
                 solution_main: bool = False):
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

    def create_file_for_problem(
        self,
        problem: LeetCodeProblem,
        root_directory: str,
        write_type: WriteContentEnum,
        should_overwrite: bool = False) -> None:
        already_setup, output_file_path = super().create_file_for_problem(
            problem, root_directory, write_type,
            should_overwrite=should_overwrite)
        question = LeetCodeApi().get_question_info(problem)
        lines = get_lines_in_a_file(output_file_path)
        for idx in range(len(lines)):
            lines[idx] = BaseFileWrite.update_file_line(lines[idx], problem)
            if "TEMPLATE__PROBLEM_PREMIUM" in lines[idx]:
                lines[idx] = \
                    lines[idx].replace(
                        "TEMPLATE__PROBLEM_PREMIUM",
                        "Yes" if problem.is_premium is True else "No")
            if "TEMPLATE__SOLUTION_STUB" in lines[idx]:
                lines[idx] = \
                    lines[idx].replace(
                        "TEMPLATE__SOLUTION_STUB",
                        question['codeSnippets'][0]['code'])
            if "TEMPLATE__PROBLEM_CONTENT" in lines[idx]:
                lines[idx] = \
                    lines[idx].replace(
                        "TEMPLATE__PROBLEM_CONTENT",
                        markdownify.markdownify(question['content'],
                                                heading_style="ATX"))
            if "TEMPLATE__PROBLEM_TAGS" in lines[idx]:
                tags = [tag['name'] for tag in question['topicTags']]
                lines[idx] = \
                    lines[idx].replace("TEMPLATE__PROBLEM_TAGS", ", ".join(tags))
            if "TEMPLATE__DISCUSSION_URL" in lines[idx]:
                url = f"{problem.problem_url}/discuss/?currentPage=1&orderBy=hot&query="
                lines[idx] = \
                    lines[idx].replace("TEMPLATE__DISCUSSION_URL", url)
            # TODO(sonapraneeth_a)
            if "TEMPLATE__EDITORIAL_URL" in lines[idx]:
                lines[idx] = \
                    lines[idx].replace("TEMPLATE__EDITORIAL_URL", "")
            if "TEMPLATE__COMPANIES" in lines[idx]:
                lines[idx] = \
                    lines[idx].replace("TEMPLATE__COMPANIES", "")
        with open(output_file_path, "w", encoding="utf-8") as file:
            file.write(''.join(lines))
