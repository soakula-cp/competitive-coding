import os
from functools import total_ordering
from typing import Dict, List

from slugify import slugify

from lib.utils.enums import JudgeEnum, DifficultyEnum, SourceTypeEnum, \
    WriteContentEnum
from lib.utils.functions import get_filename


@total_ordering
class Problem(object):
    """
    Base class for problems from various judges
    """

    def __init__(
            self,
            judge: JudgeEnum,
            identifier: str,
            title: str,
            problem_url: str,
            problem_slug: str,
            source_type: SourceTypeEnum = SourceTypeEnum.PRACTICE,
            difficulty: DifficultyEnum = DifficultyEnum.BEGINNER,
            difficulty_color: str = "rgb(0, 255, 0)",
            contest_identifier: str = "",
            explore_identifier: str = "",
            solution_url: str = "",
            solution_slug: str = "",
            video_solution_url: str = "",
            problem_directory: str = None):
        """

        Args:
            judge: Judge in which problem appeared
            identifier: a string used as a unique identifier for the problem
            title: Title of the problem
            problem_url: Complete url location of the problem on the web
            problem_slug: Slug portion of the url
            source_type: Practice/Contest/Explore
            difficulty: Difficulty level of the problem
            difficulty_color: Color representing difficulty level of the problem
            contest_identifier: Name of the contest in which the problem appeared.
                                Empty if source_type is not Contest/Explore
            explore_identifier: Sub-part of the contest
            solution_url: Complete url location of the solution on the web
            solution_slug: Slug portion of the solution url
            video_solution_url: Video link explaining solution to the problem
            problem_directory: Directory in which problem files like solution
                               would be present
        """
        self.judge = judge
        self.source_type = source_type
        self.identifier = identifier
        self.title = title
        self.problem_url = problem_url
        self.problem_slug = problem_slug
        self.solution_url = solution_url
        self.solution_slug = solution_slug
        self.video_solution_url = video_solution_url
        self.contest_identifier = contest_identifier
        self.explore_identifier = explore_identifier
        self.difficulty = difficulty
        self.difficulty_color = difficulty_color
        self.problem_directory = problem_directory
        self.submit_directory = \
            "judges\\{0}\\{1}".format(
                str(judge).lower(), str(source_type).lower())
        self.compile_command = ""

    def __eq__(self, other):
        """
        Checks whether two objects of BaseProblem are equal or not
        Args:
            other: The second object in comparison

        Returns:
            True if equal else False
        """
        return self.identifier == other.identifier

    def __lt__(self, other):
        """
        Checks whether the current object is less than the other object
        Args:
            other: The second object in comparison

        Returns:
            True if current object < other object else False
        """
        return self.identifier < other.identifier

    def __str__(self):
        """

        Returns:
            String representation of the object
        """
        answer = ""
        answer += "--- Problem ---\n"
        answer += "      ID: {0}\n".format(self.identifier)
        answer += "   Title: {0}\n".format(self.title)
        answer += "     URL: {0}\n".format(self.problem_url)
        return answer

    def get_template_filename(
            self,
            write_type: WriteContentEnum) -> str:
        """
        Get the template filename for the specific write type
        Args:
            write_type: Type of file to be written

        Returns:
            Name of the template file
        """
        _, extension = get_filename(write_type)
        template_file_name =(
            os.path.join(
                str(self.judge).lower(),
                f"{str(write_type).lower()}-{str(self.source_type).lower()}.{extension.lower()}"))
        return template_file_name

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
        if self.source_type == SourceTypeEnum.PRACTICE:
            return os.path.join(
                self.submit_directory,
                slugify(str(self.difficulty)).lower(),
                self.problem_directory,
                filename)
        if self.source_type == SourceTypeEnum.CONTEST:
            return os.path.join(
                self.submit_directory,
                self.contest_identifier,
                self.problem_directory,
                filename)
        return os.path.join(
            self.submit_directory,
            self.explore_identifier,
            self.contest_identifier,
            self.problem_directory,
            filename)

    def convert_to_dictionary(self) -> Dict[str, object]:
        """

        Returns:
            Dictionary representation of the problem
        """
        dictionary = {
            'Identifier': self.identifier,
            'Title': self.title,
            'Difficulty': str(self.difficulty),
            'Question Url': self.problem_url
        }
        return dictionary
