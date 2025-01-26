import os.path
from datetime import datetime
from typing import List

from tabulate import tabulate

from lib.api.codechef import CodeChefApi
from lib.api.leetcode import LeetCodeApi
from lib.parser.submission.base import SubmissionParser
from lib.parser.submission.leetcode import LeetCodeSubmissionParser
from lib.utils.enums import JudgeEnum, SourceTypeEnum, WriteContentEnum


def get_readme_file_path(root_directory,
                         judge: JudgeEnum,
                         source_type: SourceTypeEnum,
                         explore_identifier: str,
                         contest_identifier: str):
    output_directory = os.path.join(root_directory, "judges", str(judge).lower(),
                                    str(source_type).lower())
    if len(explore_identifier) > 0:
        output_directory = os.path.join(output_directory, explore_identifier)
    if len(contest_identifier) > 0:
        output_directory = os.path.join(output_directory, contest_identifier)
    return os.path.join(output_directory, "README.md")


def readme_for_submissions(root_directory: str, judge: JudgeEnum,
                           source_type: SourceTypeEnum,
                           explore_identifier: str,
                           contest_identifier: str,
                           problem_ids: List[str] = None,
                           force: bool = False):
    judge_api = None
    parser = None
    # Api initialization
    if judge == JudgeEnum.LEETCODE:
        judge_api = LeetCodeApi(source_type=source_type)
        parser = LeetCodeSubmissionParser()
    elif judge == JudgeEnum.CODECHEF:
        judge_api = CodeChefApi(source_type=source_type)
        parser = SubmissionParser()
    # List problems
    algorithm_problems, dictionary_of_problems = \
        judge_api.get_algorithm_problems(
            explore_identifier=explore_identifier,
            contest_identifier=contest_identifier,
            force=force)
    all_problem_ids = [str(problem.identifier) for problem in algorithm_problems]
    problem_ids = \
        all_problem_ids \
            if problem_ids is None or len(problem_ids) == 0 \
            else problem_ids
    headings = [
        'Problem Identifier',
        'Problem Title',
        'Solution Id',
        'Submission link',
        'Time complexity',
        'Space complexity',
        'Tags',
        'Categories',
        'Runtime',
        'Memory usage']
    table = []
    for problem_id in problem_ids:
        problem = dictionary_of_problems[problem_id]
        output_file_path =(
            os.path.join(root_directory,
                         problem.get_output_filename(write_type=WriteContentEnum.SOLUTION)))
        if not os.path.exists(output_file_path):
            continue
        print(f"Including {output_file_path} in README ...")
        submissions = parser.extract_submission(problem, output_file_path)
        for submission_id, submission in enumerate(submissions):
            row = [f"[{problem.identifier}]({problem.problem_url})",
                   f"{problem.title}",
                   f"{submission_id + 1}",
                   f"[Link]({submission.judge_metadata.url})",
                   f"{submission.algorithm_metadata.time_complexity}",
                   f"{submission.algorithm_metadata.space_complexity}",
                   f"{submission.algorithm_metadata.categories}",
                   f"{submission.algorithm_metadata.tags}",
                   f"{submission.judge_metadata.runtime}",
                   f"{submission.judge_metadata.memory}"]
            table.append(row)
    return headings, table


def create_readme_for_submissions(root_directory: str, judge: JudgeEnum,
                                  source_type: SourceTypeEnum,
                                  explore_identifier: str,
                                  contest_identifier: str,
                                  problem_ids: List[str] = None,
                                  force: bool = False):
    readme_file_path = get_readme_file_path(root_directory, judge, source_type,
                                            explore_identifier,
                                            contest_identifier)
    print(readme_file_path)
    with open(readme_file_path, 'w') as file_handle:
        table = []
        file_handle.write("---\n")
        if len(explore_identifier) > 0:
            file_handle.write(f"Explore name: {explore_identifier}\n")
        if len(contest_identifier) > 0:
            file_handle.write(f"Contest name: {contest_identifier}\n")
        file_handle.write(f"Last updated: {datetime.today()}\n")
        file_handle.write("---\n\n")
        file_handle.write("# README\n\n")
        file_handle.write(
            "> **Note:** Please do not modify this file. This file is "
            "generated using `main__generate_readme.py`. Manual edits to "
            "this file will be lost.\n\n")
        file_handle.write("## Problems\n\n")
        headings, table = readme_for_submissions(root_directory, judge,
                                                 source_type,
                                                 explore_identifier,
                                                 contest_identifier,
                                                 problem_ids,
                                                 force=force)
        file_handle.write(tabulate(table, headers=headings, tablefmt="github"))
