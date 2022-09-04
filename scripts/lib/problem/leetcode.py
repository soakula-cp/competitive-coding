from functools import total_ordering

from slugify import slugify

from lib.problem.base import Problem
from lib.utils.enums import JudgeEnum, SourceTypeEnum, DifficultyEnum, \
    WriteContentEnum
from lib.utils.functions import get_filename


@total_ordering
class LeetCodeProblem(Problem):
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
                 video_solution_url: str = "",
                 is_premium: bool = False,
                 status: str = ""):
        """
        Constructor for LeetCode problem
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
            is_premium: If the problem belongs to subscription
            status:
        """
        problem_url = "https://www.leetcode.com"
        problem_url += ("/problems/" if source_type == SourceTypeEnum.PRACTICE
                        else ("/" + contest_identifier.upper())) + question_slug
        super().__init__(
            judge=JudgeEnum.LEETCODE,
            identifier=identifier,
            title=title,
            problem_url=problem_url,
            problem_slug=question_slug,
            difficulty=difficulty,
            difficulty_color=difficulty_color,
            source_type=source_type,
            contest_identifier=contest_identifier.lower(),
            explore_identifier=explore_identifier.lower(),
            solution_url=solution_url,
            video_solution_url=video_solution_url,
            problem_directory=f"{identifier}__{question_slug}"
        )
        self.is_premium = is_premium
        self.status = status
        self.compile_command = "clang11 --std=c++17 -O2"

    def __del__(self):
        pass

    def get_output_filename(
        self,
        write_type: WriteContentEnum) -> str:
        """
        Get the output filename (solution/description) for the specific write
        type
        Args:
            write_type: Type of file to be written

        Returns:
            Name of the output file with the relative path from root directory
        """
        filename, _ = get_filename(write_type)
        premium_str = "premium/" if self.is_premium is True else "non-premium/"
        if self.source_type == SourceTypeEnum.PRACTICE:
            answer = self.submit_directory + "/" \
                   + slugify(str(self.difficulty)).lower() + "/" \
                   + premium_str \
                   + self.problem_directory + "/" + filename
            return answer
        if self.source_type == SourceTypeEnum.CONTEST:
            return self.submit_directory + "/" \
                   + self.contest_identifier + "/" \
                   + premium_str \
                   + self.problem_directory + "/" + filename
        return self.submit_directory + "/" \
               + self.explore_identifier + "/" \
               + self.contest_identifier + "/" \
               + premium_str \
               + self.problem_directory + "/" + filename
