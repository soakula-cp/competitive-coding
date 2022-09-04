from functools import total_ordering

from slugify import slugify

from lib.problem.base import Problem
from lib.utils.enums import JudgeEnum, SourceTypeEnum, DifficultyEnum, \
    WriteContentEnum
from lib.utils.functions import get_filename


@total_ordering
class CodeChefProblem(Problem):
    def __init__(self,
                 identifier: str,
                 title: str,
                 question_slug: str,
                 difficulty: DifficultyEnum,
                 difficulty_color: str,
                 source_type: SourceTypeEnum = SourceTypeEnum.PRACTICE,
                 contest_identifier: str = "",
                 explore_identifier: str = "",
                 solution_url: str = "",
                 video_solution_url: str = ""):
        """
        Constructor for CodeChef problem
        Args:
            identifier: Unique identifier for the problem
            title: Title of the problem
            question_slug: Slug portion of the url
            difficulty: Level of difficulty of the problem
            difficulty_color: Color of difficulty of the problem
            source_type: Practice/Contest/Explore
            contest_identifier: Identifier for the contest in which the problem
                                appeared. Empty if source_type is not Contest
            explore_identifier: Identifier for the explore
            solution_url: Link for codechef solution article (if exists)
            video_solution_url: Video link for codechef solution article
                                (if exists)
        """
        problem_url = "https://www.codechef.com"
        problem_url += "" if source_type == SourceTypeEnum.PRACTICE else f"/{contest_identifier.upper()}"
        problem_url += f"/problems/{question_slug}"
        super().__init__(
            judge=JudgeEnum.CODECHEF,
            identifier=identifier,
            title=title,
            problem_url=problem_url,
            problem_slug=question_slug,
            difficulty=difficulty,
            difficulty_color=difficulty_color,
            source_type=source_type,
            contest_identifier=contest_identifier.upper(),
            explore_identifier=explore_identifier.upper(),
            solution_url=solution_url,
            video_solution_url=video_solution_url,
            problem_directory=identifier
        )
        # Reference: https://discuss.codechef.com/t/are-any-compiler-flags-set-on-the-online-judge/1866/2
        self.compile_command = \
            "g++ solution.cpp -std=c++17 " \
            "-lm -fomit-frame-pointer -pthread -O2 " \
            "-o solution.exe"

    def __del__(self):
        pass
