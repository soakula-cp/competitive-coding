import argparse
import logging
import os
from datetime import datetime

from lib.utils.enums import JudgeEnum, SourceTypeEnum, LogLevelEnum
from lib.utils.functions import create_empty_file
from lib.utils.readme_utils import create_readme_for_submissions


def sanitize(input_str: str) -> str:
    input_str = input_str.replace("*", "\\*")
    input_str = input_str.replace("_", "\\_")
    return input_str


def setup_logs(log_level: LogLevelEnum = LogLevelEnum.INFO):
    log_filename =(
        os.path.join("logs", "run_logs",
                     f"main__setup__{datetime.now().strftime("%Y-%m-%d--%H-%M-%S-%f")}.log"))
    create_empty_file(log_filename)
    # Reference: https://docs.python.org/3/library/logging.html#logrecord-attributes
    log_format = "%(asctime)s::%(levelname)s::%(module)s::%(funcName)s::%(message)s"
    logging.basicConfig(filename=log_filename, filemode='w', encoding='utf-8',
                        format=log_format, level=int(log_level))
    # logFormatter = logging.Formatter(log_format)
    # rootLogger = logging.getLogger()
    # fileHandler = logging.FileHandler(log_filename)
    # fileHandler.setFormatter(logFormatter)
    # rootLogger.addHandler(fileHandler)
    #
    # consoleHandler = logging.StreamHandler()
    # consoleHandler.setFormatter(logFormatter)
    # rootLogger.addHandler(consoleHandler)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # positional argument
    parser.add_argument(
        "-j", "--judge", type=JudgeEnum.from_string,
        default=JudgeEnum.CODECHEF, required=False,
        choices=list(JudgeEnum),
        help="Which online judge the script should run? "
             "Note: Input is case-sensitive. Should be in "
             "capital letters. Default: CODECHEF.")
    parser.add_argument(
        "-f", "--force", action="store_true",
        default=False,
        help="Force API usage. "
             "Default: False")
    # Reference: https://stackoverflow.com/questions/43968006/support-for-enum-arguments-in-argparse
    parser.add_argument(
        "-l", "--log_level",
        type=LogLevelEnum.from_string,
        default=LogLevelEnum.INFO, required=False,
        choices=list(LogLevelEnum),
        help="Level of logs to be printed? "
             "Note: Input is case-sensitive. Default: INFO.")
    parser.add_argument(
        "-s", "--source_type",
        type=SourceTypeEnum.from_string,
        default=SourceTypeEnum.PRACTICE, required=False,
        choices=list(SourceTypeEnum),
        help="What is the source type? "
             "Note: Input is case-sensitive. Should be in "
             "capital letters. Default: PRACTICE.")
    parser.add_argument(
        "-e", "--explore_identifier", type=str,
        required=False,
        default="",
        help="Subpart of the contest. "
             "Note: Input is case-sensitive. Default: ''.")
    parser.add_argument(
        "-c", "--contest_identifier", type=str,
        required=False,
        default="",
        help="Id for the contest. "
             "Note: Input is case-sensitive. Default: PRACTICE.")
    # command line flags
    parser.add_argument("-q", "--quiet", action="store_true",
                        default=True,
                        help="suppress messages to stdout")
    # parse args
    args = parser.parse_args()
    print(args)
    if args.quiet:
        print("Running in Quiet Mode")

    setup_logs(log_level=args.log_level)

    judge = args.judge
    source_type = args.source_type
    explore_identifier = args.explore_identifier
    contest_identifier = args.contest_identifier
    problem_ids = None

    root_directory = "."
    create_readme_for_submissions(root_directory, judge, source_type,
                                  explore_identifier, contest_identifier,
                                  problem_ids, force=args.force)

    # if args.platform.lower() == "leetcode":
    #     leetcode = LeetCodeApi(args.quiet)
    #     algorithm_problems, _ = leetcode.get_algorithm_problems(force=False)
    #     algorithm_problems.sort(key=lambda x: int(x.identifier), reverse=False)
    #     for problem in algorithm_problems[:8]:
    #         print(problem)
    #     submit_directory = os.path.join("..", "platforms", "leetcode", "practice")
    #     root = os.getcwd()
    #     print("Looking for attempted/solved problems")
    #     template_solutions_file_path = os.path.join("templates", "leetcode", "solutions.cpp")
    #     template_desc_file_path = os.path.join("templates", "leetcode", "description.md")
    #     problems_file = os.path.join("..", "platforms", "leetcode", "PROBLEMS.md")
    #     problems_file_handle = open(problems_file, "w")
    #     problems_file_handle.write("# Problems\n\n")
    #     problems_file_handle.write(
    #         "> **Note:** Please do not modify this file. This file is "
    #         "generated using `main__generate_readme.py`. Manual edits to this "
    #         "file will be lost.\n\n")
    #     problems_file_handle.write("## Practice\n\n")
    #     readme_solutions = []
    #     heading_list = [
    #         "Problem",
    #         "Problem difficulty",
    #         "Solution Id",
    #         "Judge submission link",
    #         "Solution status",
    #         "Time complexity",
    #         "Space complexity",
    #         "Judge time",  # (ms)",
    #         "Judge space",  # (MB)",
    #         "Tags",
    #         "Categories",
    #         "Number of tests passed",
    #         "IsTemplate?"
    #     ]
    #     submission_status_dict = {
    #         "Accepted": "#009688",
    #         "Time Limit Exceeded": "",
    #         "Wrong Answer": "",
    #         "Memory Limit Exceeded": "",
    #         "Output Limit Exceeded": "",
    #         "Runtime Error": "",
    #         "": "#000000"
    #     }
    #     problem_difficulty_dict = {
    #         "Easy": "rgb(67, 160, 71)",
    #         "Medium": "rgb(239, 108, 0)",
    #         "Hard": "rgb(233, 30, 99)",
    #     }
    #     for problem in algorithm_problems:
    #         if problem.is_premium:
    #             continue
    #         # print("Checking solutions.cpp for {0}. {1}"
    #         #       .format(problem.identifier, problem.title))
    #         is_existing, is_attempted, _, _ = check_file(
    #             problem, submit_directory, "solutions.cpp",
    #             root + template_solutions_file_path)
    #         if is_attempted is True:
    #             print("Attempted problem: {0}. {1}".format(
    #                 problem.identifier, problem.title))
    #             solutions_for_problem = read_solutions_file(problem=problem)
    #             for solution in solutions_for_problem:
    #                 readme_solutions.append([
    #                     "[" + str(problem.identifier) + ". " + problem.title +
    #                     "](" + problem.url + ")",
    #                     "<span style=\"color: {0};\">{1}</span>"
    #                         .format(problem_difficulty_dict[problem.difficulty],
    #                                 problem.difficulty),
    #                     str(solution.identifier),
    #                     "[Link](" + solution.judge_submission_link + ")",
    #                     "<span style=\"color: {0};\">{1}</span>"
    #                         .format(submission_status_dict[
    #                                     solution.judge_submission_status],
    #                                 solution.judge_submission_status),
    #                     sanitize(str(solution.time_complexity)),
    #                     sanitize(str(solution.space_complexity)),
    #                     solution.judge_runtime_value,
    #                     solution.judge_memory_usage_value,
    #                     ",".join(solution.tags),
    #                     ",".join(solution.categories),
    #                     solution.judge_testcase_status,
    #                     "No"
    #                 ])
    #     line, underline = "|", "|"
    #     for column in heading_list:
    #         line += column + "|"
    #         underline += '-' * len(column) + "|"
    #     problems_file_handle.write(line + "\n")
    #     problems_file_handle.write(underline + "\n")
    #     for solution in readme_solutions:
    #         line = "|"
    #         for column in solution:
    #             line += column + "|"
    #         problems_file_handle.write(line + "\n")
    #     problems_file_handle.close()
