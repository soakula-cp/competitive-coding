import os

from lib.file.base import BaseFileWrite
from lib.file.codechef import CodeChefFileWrite
from lib.file.leetcode import LeetCodeFileWrite
from lib.problem.base import Problem
from lib.problem.codechef import CodeChefProblem
from lib.problem.leetcode import LeetCodeProblem
from lib.utils.enums import JudgeEnum, DifficultyEnum, SourceTypeEnum, \
    WriteContentEnum


def write_template_file(
        judge_file_write: BaseFileWrite,
        root_dir: str,
        problem: Problem,
        template_type: WriteContentEnum):
    """

    :param judge_file_write:
    :param root_dir:
    :param problem:
    :param template_type:
    :return:
    """
    template_filename = \
        os.path.join(root_dir, problem.get_template_filename(template_type))
    print(f"Creating template file: {template_filename}")
    judge_file_write.create_template_file(
        template_filename, problem, template_type,
        should_overwrite=True)


if __name__ == "__main__":
    template_root_directory = os.path.join("..", "templates", "final_merged")
    judge = JudgeEnum.LEETCODE
    judge_file_write : BaseFileWrite = None
    if judge == JudgeEnum.CODECHEF:
        judge_file_write = CodeChefFileWrite(template_root_directory)
    elif judge == JudgeEnum.LEETCODE:
        judge_file_write = LeetCodeFileWrite(
            template_root_directory,
            solution_include_and_using=False,
            solution_base_class=False,
            solution_main=False)
    else:
        print(f"Judge '{judge}' not supported")
        exit(1)

    problems = {
        JudgeEnum.CODECHEF: [
            CodeChefProblem(
                "", "", "", DifficultyEnum.BEGINNER, "",
                source_type=SourceTypeEnum.PRACTICE),
            CodeChefProblem(
                "", "", "", DifficultyEnum.BEGINNER, "",
                source_type=SourceTypeEnum.EXPLORE),
            # CodeChefProblem(
            #     "", "", "", DifficultyEnum.BEGINNER, "",
            #     source_type=SourceTypeEnum.CONTEST),
        ],
        JudgeEnum.LEETCODE: [
            LeetCodeProblem(
                "", "", "", DifficultyEnum.BEGINNER, "",
                source_type=SourceTypeEnum.PRACTICE),
            LeetCodeProblem(
                "", "", "", DifficultyEnum.BEGINNER, "",
                source_type=SourceTypeEnum.EXPLORE),
            LeetCodeProblem(
                "", "", "", DifficultyEnum.BEGINNER, "",
                source_type=SourceTypeEnum.CONTEST),
        ]
    }

    write_types = [WriteContentEnum.SOLUTION, WriteContentEnum.DESCRIPTION, WriteContentEnum.TESTCASES]
    for key in problems.keys():
        list_of_problems = problems[key]
        for problem in list_of_problems:
            for write_type in write_types:
                write_template_file(judge_file_write, template_root_directory, problem, write_type)
