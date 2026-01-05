from functools import total_ordering

from lib.problem.base import Problem
from lib.utils.enums import JudgeEnum


@total_ordering
class AdventOfCodeProblem(Problem):
    def __init__(self,
                 identifier: str,
                 title: str,
                 question_slug: str,
                 contest_identifier: str = ""):
        """
        Constructor for CodeChef problem
        Args:
            identifier: Unique identifier for the problem
            title: Title of the problem
            question_slug: Slug portion of the url
            contest_identifier: Identifier for the contest in which the problem
                                appeared. Empty if source_type is not Contest
        """
        problem_url = "https://adventofcode.com/"
        problem_url += f"/{contest_identifier}/day/{question_slug}"
        super().__init__(
            judge=JudgeEnum.ADVENTOFCODE,
            identifier=identifier,
            title=title,
            problem_url=problem_url,
            problem_slug=question_slug,
            contest_identifier=contest_identifier.upper(),
            problem_directory=identifier
        )
        # Reference: https://discuss.codechef.com/t/are-any-compiler-flags-set-on-the-online-judge/1866/2
        self.compile_command = \
            "g++ solution.cpp -std=c++23 " \
            "-lm -fomit-frame-pointer -pthread -O2 " \
            "-o solution.exe"

    def __del__(self):
        pass
