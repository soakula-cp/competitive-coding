import argparse
import os

from lib.utils.enums import JudgeEnum


def sanitize(input_str: str) -> str:
    input_str = input_str.replace("*", "\\*")
    input_str = input_str.replace("_", "\\_")
    return input_str


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
    # command line flags
    parser.add_argument("-q", "--quiet", action="store_true",
                        default=True,
                        help="suppress messages to stdout")
    # parse args
    args = parser.parse_args()
    print(args)
    if args.quiet:
        print("Running in Quiet Mode")

    if args.platform.lower() == "leetcode":
        leetcode = LeetCodeApi(args.quiet)
        algorithm_problems, _ = leetcode.get_algorithm_problems(force=False)
        algorithm_problems.sort(key=lambda x: int(x.identifier), reverse=False)
        for problem in algorithm_problems[:8]:
            print(problem)
        submit_directory = "..\\platforms\\leetcode\\practice"
        root = os.getcwd()
        print("Looking for attempted/solved problems")
        template_solutions_file_path = \
            "\\templates" + "\\leetcode\\" + "solutions.cpp"
        template_desc_file_path = \
            "\\templates" + "\\leetcode\\" + "description.md"
        problems_file = "..\\platforms\\leetcode\\PROBLEMS.md"
        problems_file_handle = open(problems_file, "w")
        problems_file_handle.write("# Problems\n\n")
        problems_file_handle.write(
            "> **Note:** Please do not modify this file. This file is "
            "generated using `main__generate_readme.py`. Manual edits to this "
            "file will be lost.\n\n")
        problems_file_handle.write("## Practice\n\n")
        readme_solutions = []
        heading_list = [
            "Problem",
            "Problem difficulty",
            "Solution Id",
            "Judge submission link",
            "Solution status",
            "Time complexity",
            "Space complexity",
            "Judge time",  # (ms)",
            "Judge space",  # (MB)",
            "Tags",
            "Categories",
            "Number of tests passed",
            "IsTemplate?"
        ]
        submission_status_dict = {
            "Accepted": "#009688",
            "Time Limit Exceeded": "",
            "Wrong Answer": "",
            "Memory Limit Exceeded": "",
            "Output Limit Exceeded": "",
            "Runtime Error": "",
            "": "#000000"
        }
        problem_difficulty_dict = {
            "Easy": "rgb(67, 160, 71)",
            "Medium": "rgb(239, 108, 0)",
            "Hard": "rgb(233, 30, 99)",
        }
        for problem in algorithm_problems:
            if problem.is_premium:
                continue
            # print("Checking solutions.cpp for {0}. {1}"
            #       .format(problem.identifier, problem.title))
            is_existing, is_attempted, _, _ = check_file(
                problem, submit_directory, "solutions.cpp",
                root + template_solutions_file_path)
            if is_attempted is True:
                print("Attempted problem: {0}. {1}".format(
                    problem.identifier, problem.title))
                solutions_for_problem = read_solutions_file(problem=problem)
                for solution in solutions_for_problem:
                    readme_solutions.append([
                        "[" + str(problem.identifier) + ". " + problem.title +
                        "](" + problem.url + ")",
                        "<span style=\"color: {0};\">{1}</span>"
                            .format(problem_difficulty_dict[problem.difficulty],
                                    problem.difficulty),
                        str(solution.identifier),
                        "[Link](" + solution.judge_submission_link + ")",
                        "<span style=\"color: {0};\">{1}</span>"
                            .format(submission_status_dict[
                                        solution.judge_submission_status],
                                    solution.judge_submission_status),
                        sanitize(str(solution.time_complexity)),
                        sanitize(str(solution.space_complexity)),
                        solution.judge_runtime_value,
                        solution.judge_memory_usage_value,
                        ",".join(solution.tags),
                        ",".join(solution.categories),
                        solution.judge_testcase_status,
                        "No"
                    ])
        line, underline = "|", "|"
        for column in heading_list:
            line += column + "|"
            underline += '-' * len(column) + "|"
        problems_file_handle.write(line + "\n")
        problems_file_handle.write(underline + "\n")
        for solution in readme_solutions:
            line = "|"
            for column in solution:
                line += column + "|"
            problems_file_handle.write(line + "\n")
        problems_file_handle.close()
