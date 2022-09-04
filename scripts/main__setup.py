import argparse
import logging
import sys
from datetime import datetime

from lib.api.codechef import CodeChefApi
from lib.api.leetcode import LeetCodeApi
from lib.file.codechef import CodeChefFileWrite
from lib.file.leetcode import LeetCodeFileWrite
from lib.utils.enums import JudgeEnum, SourceTypeEnum, WriteContentEnum, \
    LogLevelEnum
from lib.utils.functions import create_empty_file


def setup_logs():
    log_filename = "logs\\run_logs\\main__setup__{0}.log" \
        .format(datetime.now().strftime("%Y-%m-%d--%H-%M-%S-%f"))
    create_empty_file(log_filename)
    # Reference: https://docs.python.org/3/library/logging.html#logrecord-attributes
    log_format = "%(asctime)s::%(levelname)s::%(module)s::%(funcName)s::%(message)s"
    logging.basicConfig(filename=log_filename, filemode='w', encoding='utf-8',
                        format=log_format, level=int(input_arguments.log_level))
    # logFormatter = logging.Formatter(log_format)
    # rootLogger = logging.getLogger()
    # fileHandler = logging.FileHandler(log_filename)
    # fileHandler.setFormatter(logFormatter)
    # rootLogger.addHandler(fileHandler)
    #
    # consoleHandler = logging.StreamHandler()
    # consoleHandler.setFormatter(logFormatter)
    # rootLogger.addHandler(consoleHandler)


def validate_args(args: argparse.Namespace) -> bool:
    """
    Validate arguments passed as input to the program
    Args:
        args:

    Returns:
        True if the arguments are correct
        False if the arguments are incorrect
    """
    if args.source_type == SourceTypeEnum.CONTEST and \
        len(args.contest_identifier) == 0:
        print("Invalid arguments for {0}".format(args.source_type))
        return False
    if args.source_type == SourceTypeEnum.EXPLORE and \
        len(args.contest_identifier) == 0 and \
        len(args.explore_identifier) == 0:
        print("Invalid arguments for {0}".format(args.source_type))
        return False
    return True


def command_help(judge: JudgeEnum = None):
    # Reference: https://stackoverflow.com/questions/50886471/simulating-argparse-command-line-arguments-input-while-debugging/50886791#50886791
    commands = []
    if judge == JudgeEnum.CODECHEF:
        commands = [
            # CodeChef commands
            "main__setup.py show -j CODECHEF -s EXPLORE -e LP0TO1 -c LP0TO101 "
            "-l DEBUG",
            "main__setup.py setup -j CODECHEF -s PRACTICE -l DEBUG -p EMAILREM "
            "-p ANUARM --overwrite -w SOLUTION -w DESCRIPTION",
            "main__setup.py setup -j CODECHEF -s EXPLORE -e LP1TO2 -c LP1TO201 "
            "-l DEBUG -p HOOPS --overwrite -w SOLUTION -w DESCRIPTION",
            "main__setup.py setup -j CODECHEF -s EXPLORE -e LP0TO1 -c LP0TO101 "
            "-l DEBUG -p START01 --overwrite -w SOLUTION -w DESCRIPTION",
            "main__setup.py setup -j CODECHEF -s EXPLORE -e LP0TO1 -c LP0TO101 "
            "-l DEBUG -w SOLUTION -w DESCRIPTION",
            "main__setup.py show -j CODECHEF -s CONTEST -c START54D",
            "main__setup.py show -j CODECHEF -s PRACTICE -l DEBUG",
            "main__setup.py setup -j CODECHEF -s PRACTICE -l DEBUG -p FLOW001 "
            "--overwrite -w SOLUTION -w DESCRIPTION",
        ]
    elif judge == JudgeEnum.LEETCODE:
        commands = [
            # LeetCode commands
            "main__setup.py show -j LEETCODE -s PRACTICE -l DEBUG --force",
            "main__setup.py setup -j LEETCODE -s PRACTICE -l DEBUG -p 1929 "
            "-w SOLUTION -w DESCRIPTION",
        ]
    else:
        print(f"Unknown value for judge '{judge}'. Using default help setup")
        commands = [
            # Help commands
            "main__setup.py -h",
            "main__setup.py show -h",
            "main__setup.py setup -h"
        ]
    sys.argv = commands[-1].split(' ')


if __name__ == '__main__':
    command_help(JudgeEnum.CODECHEF)
    # Take arguments as input from the program
    # Reference: https://docs.python.org/3/library/argparse.html
    parser = argparse.ArgumentParser()
    # Commands for the parser program
    # Reference: https://towardsdatascience.com/a-simple-guide-to-command-line-arguments-with-argparse-6824c30ab1c3
    # Create parent subparser. Note `add_help=False` and creation via `argparse.`
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument(
        "-f", "--force", action="store_true",
        default=False,
        help="Force API usage. "
             "Default: False")
    # Reference: https://stackoverflow.com/questions/43968006/support-for-enum-arguments-in-argparse
    parent_parser.add_argument(
        "-l", "--log_level",
        type=LogLevelEnum.from_string,
        default=LogLevelEnum.INFO, required=False,
        choices=list(LogLevelEnum),
        help="Level of logs to be printed? "
             "Note: Input is case-sensitive. Default: INFO.")
    parent_parser.add_argument(
        "-j", "--judge", type=JudgeEnum.from_string,
        default=JudgeEnum.CODECHEF, required=False,
        choices=list(JudgeEnum),
        help="Which online judge the script should run? "
             "Note: Input is case-sensitive. Should be in "
             "capital letters. Default: CODECHEF.")
    parent_parser.add_argument(
        "-s", "--source_type",
        type=SourceTypeEnum.from_string,
        default=SourceTypeEnum.PRACTICE, required=False,
        choices=list(SourceTypeEnum),
        help="What is the source type? "
             "Note: Input is case-sensitive. Should be in "
             "capital letters. Default: PRACTICE.")
    parent_parser.add_argument(
        "-e", "--explore_identifier", type=str,
        required=False,
        default="",
        help="Subpart of the contest. "
             "Note: Input is case-sensitive. Default: ''.")
    parent_parser.add_argument(
        "-c", "--contest_identifier", type=str,
        required=False,
        default="PRACTICE",
        help="Id for the contest. "
             "Note: Input is case-sensitive. Default: PRACTICE.")

    # Create subparsers
    subparser = parser.add_subparsers(
        help='Desired action to perform',
        dest='action')
    show = subparser.add_parser(
        'show', parents=[parent_parser],
        help="Display list of problems for the given parameters")
    setup = subparser.add_parser(
        'setup', parents=[parent_parser],
        help="Setup required files based on the given parameters")
    setup.add_argument(
        "-d", "--root_directory", type=str,
        required=False,
        default="..",
        help="Directory in which the content is to be written")
    # Reference: https://stackoverflow.com/questions/15753701/how-can-i-pass-a-list-as-a-command-line-argument-with-argparse
    setup.add_argument(
        "-p", "--problem_id", action="append", type=str,
        required=False,
        help="List of problem ids for template setup.")
    setup.add_argument(
        "-w", "--write_content_option",
        action="append",
        type=WriteContentEnum.from_string,
        required=True,
        choices=list(WriteContentEnum),
        help="What template file should be setup? "
             "Note: Input is case-sensitive.")
    setup.add_argument(
        "-o", "--overwrite", action="store_true",
        default=False,
        help="Overwrite files even if the file exists. "
             "Default: False")

    # Parse arguments
    input_arguments = parser.parse_args()
    print(input_arguments)
    # Validate arguments
    if validate_args(input_arguments) is False:
        exit(1)

    setup_logs()

    judge = input_arguments.judge
    source_type = input_arguments.source_type
    force = input_arguments.force
    explore_identifier = input_arguments.explore_identifier
    contest_identifier = input_arguments.contest_identifier
    action = input_arguments.action
    write_content_options = []
    problem_ids = []
    overwrite = False
    if action == 'setup':
        write_content_options = input_arguments.write_content_option
        problem_ids = input_arguments.problem_id
        overwrite = input_arguments.overwrite

    judge_api = None
    judge_file_write = None

    # Api initialization
    if judge == JudgeEnum.CODECHEF:
        judge_api = CodeChefApi(source_type=source_type,)
        judge_file_write = CodeChefFileWrite("..\\templates\\final_merged\\")
    elif judge == JudgeEnum.LEETCODE:
        judge_api = LeetCodeApi(source_type=source_type, )
        judge_file_write = LeetCodeFileWrite("..\\templates\\final_merged\\")

    # List problems
    algorithm_problems, dictionary_of_problems = \
        judge_api.get_algorithm_problems(
            explore_identifier=explore_identifier,
            contest_identifier=contest_identifier,
            force=force)
    all_problem_ids = [problem.identifier for problem in algorithm_problems]
    problem_ids = \
        all_problem_ids \
            if problem_ids is None or len(problem_ids) == 0 \
            else problem_ids

    if action.lower() == 'show':
        problems_to_display = 4
        if source_type != SourceTypeEnum.PRACTICE:
            problems_to_display = -1
        judge_api.print_problems(algorithm_problems, count=problems_to_display)
    if action.lower() == 'setup':
        for problem_id in problem_ids:
            problem = dictionary_of_problems[problem_id]
            for write_content_option in write_content_options:
                judge_file_write.create_file_for_problem(
                    problem, "..", write_content_option, should_overwrite=overwrite)
