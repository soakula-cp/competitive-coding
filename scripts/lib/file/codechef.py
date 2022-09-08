import markdownify
from bs4 import BeautifulSoup

from lib.api.codechef import CodeChefApi
from lib.file.base import BaseFileWrite
from lib.problem.codechef import CodeChefProblem
from lib.utils.enums import WriteContentEnum
from lib.utils.functions import get_lines_in_a_file


class CodeChefFileWrite(BaseFileWrite):
    def __init__(self,
                 template_root_directory: str):
        super().__init__(template_root_directory=template_root_directory)

    def write_test(self, tests, dir: str, identifier="Sample"):
        for test in tests:
            input_filename = f"{dir}\\{identifier}_{test['id']}.in.txt"
            output_filename = f"{dir}\\{identifier}_{test['id']}.out.txt"
            with open(input_filename, "w") as filep:
                filep.write(f"{test['input']}")
            with open(output_filename, "w") as filep:
                filep.write(f"{test['output']}")

    def create_file_for_tests(
        self,
        problem: CodeChefProblem,
        output_directory: str,
        should_overwrite: bool = False) -> (bool, str):
        question = CodeChefApi().get_question_info(problem)
        problem_components = \
            question["problemComponents"] \
                if "problemComponents" in question else dict()
        self.write_test(
            problem_components["sampleTestCases"]
                if "sampleTestCases" in problem_components else [],
            output_directory)
        self.write_test(
            question["specialTestCases"]
                if "specialTestCases" in question else [],
            output_directory, "Special")
        return True, ""

    def create_file_for_problem(
        self,
        problem: CodeChefProblem,
        root_directory: str,
        write_type: WriteContentEnum,
        should_overwrite: bool = False) -> None:
        already_setup, output_file_path = super().create_file_for_problem(
            problem, root_directory, write_type,
            should_overwrite=should_overwrite)
        if write_type == WriteContentEnum.TESTCASES:
            return
        question = CodeChefApi().get_question_info(problem)
        lines = get_lines_in_a_file(output_file_path)
        for idx in range(len(lines)):
            lines[idx] = BaseFileWrite.update_file_line(lines[idx], problem)
            problem_components = \
                question["problemComponents"] \
                    if "problemComponents" in question else dict()
            question_tags = \
                ", ".join(
                    question["user_tags"]) if "user_tags" in question else ""
            question_tags += "; "
            question_tags += \
                ", ".join(question[
                              "computed_tags"]) if "computed_tags" in question else ""
            question_editorial_url = \
                question["editorial_url"] if "editorial_url" in question else ""
            contest_code = \
                question["contest_code"] if "contest_code" in question else ""
            contest_name = \
                question["contest_name"] if "contest_name" in question else ""
            # tags = BeautifulSoup(question_tags, "lxml").text
            if "TEMPLATE__PROBLEM_TAGS" in lines[idx]:
                lines[idx] = \
                    lines[idx].replace("TEMPLATE__PROBLEM_TAGS", question_tags)
            if "TEMPLATE__EDITORIAL_URL" in lines[idx]:
                lines[idx] = \
                    lines[idx].replace(
                        "TEMPLATE__EDITORIAL_URL", question_editorial_url)
            if "TEMPLATE__VIDEO_EDITORIAL_URL" in lines[idx]:
                video_url = \
                    question["gumlet_video_url"] \
                        if "gumlet_video_url" in question else ""
                video_url = "" if video_url is None else video_url
                lines[idx] = lines[idx].replace(
                    "TEMPLATE__VIDEO_EDITORIAL_URL",
                    video_url)
            if "TEMPLATE__DISCUSSION_URL" in lines[idx]:
                lines[idx] = lines[idx].replace(
                    "TEMPLATE__DISCUSSION_URL", question["problemDiscussURL"])
            if "TEMPLATE__PROBLEM_STATEMENT" in lines[idx]:
                lines[idx] = lines[idx].replace(
                    "TEMPLATE__PROBLEM_STATEMENT",
                    markdownify.markdownify(problem_components["statement"],
                                            heading_style="ATX"))
            if "TEMPLATE__PROBLEM_CONTEST_NAME" in lines[idx]:
                lines[idx] = lines[idx].replace(
                    "TEMPLATE__PROBLEM_CONTEST_NAME",
                    f"{contest_code} - {contest_name}")
            if "TEMPLATE__PROBLEM_CONSTRAINTS" in lines[idx]:
                lines[idx] = lines[idx].replace(
                    "TEMPLATE__PROBLEM_CONSTRAINTS",
                    problem_components["constraints"])
            if "TEMPLATE__PROBLEM_INPUT_FORMAT" in lines[idx]:
                lines[idx] = lines[idx].replace(
                    "TEMPLATE__PROBLEM_INPUT_FORMAT",
                    problem_components["inputFormat"])
            if "TEMPLATE__PROBLEM_OUTPUT_FORMAT" in lines[idx]:
                lines[idx] = lines[idx].replace(
                    "TEMPLATE__PROBLEM_OUTPUT_FORMAT",
                    problem_components["outputFormat"])
            if "TEMPLATE__PROBLEM_SUBTASKS" in lines[idx]:
                lines[idx] = \
                    lines[idx].replace(
                        "TEMPLATE__PROBLEM_SUBTASKS",
                        problem_components["subtasks"])
            if "TEMPLATE__EXAMPLE_TESTS" in lines[idx]:
                sample_tests = problem_components["sampleTestCases"]
                tests = ""
                for test in sample_tests:
                    tests += f"## Sample Test {test['id']}\n"
                    tests += f"\n**Input:**\n"
                    tests += f"{test['input']}\n"
                    tests += f"\n**Output:**\n"
                    tests += f"{test['output']}\n"
                    tests += f"\n**Explanation:**\n"
                    tests += f"{test['explanation']}\n"
                lines[idx] = lines[idx].replace("TEMPLATE__EXAMPLE_TESTS",
                                                tests)
        with open(output_file_path, "w", encoding="utf-8") as file:
            file.write(''.join(lines))
