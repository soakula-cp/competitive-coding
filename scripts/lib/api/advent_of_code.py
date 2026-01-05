import logging
from typing import Dict, List

from tabulate import tabulate
from bs4 import BeautifulSoup

from lib.api.base import BaseApi
from lib.problem.advent_of_code import AdventOfCodeProblem
from lib.utils.enums import JudgeEnum, SourceTypeEnum
from lib.utils.functions import make_api_call


class AdventOfCodeApi(BaseApi):
    """
    Class handling requests to Codechef API
    """

    def __init__(self,
                 source_type: SourceTypeEnum = SourceTypeEnum.CONTEST):
        """

        Args:
            source_type:
        """
        super().__init__(
            source_type=source_type,
            levels=[],
            colors=[])
        # Specific problem
        # Input: Contest name (year of contest), Problem Slug
        self.problem_url = \
            "https://www.adventofcode.com/{0}/day/{1}"
        # Filenames for cache
        # Input: For a specific question
        # Input: Contest name, Problem Slug
        self.filename_question = "logs/adventofcode/questions/{0}/{1}.html"

    def get_question_info(self, problem: AdventOfCodeProblem,
                          force: bool = False) -> Dict:
        """
        Download description for the given problem
        Args:
            problem: Input problem
            force: If API usage is to be forced

        Returns:
            Problem description as a dictionary
        """
        if problem.judge != JudgeEnum.ADVENTOFCODE:
            print("This Api can be used only for Advent Of Code problems")
            exit(1)
        response = make_api_call(
            url=self.problem_url.format(
                problem.contest_identifier, problem.identifier),
            filename=self.filename_question.format(
                problem.contest_identifier, problem.identifier),
            force=force)
        if response is None:
            print("Question data for {0}. {1} could not be retrieved".format(
                problem.contest_identifier, problem.identifier))
        if "content" not in response:
            print("Failed to retrieve the page for the problem.")
            return {}
        soup = BeautifulSoup(response["content"], 'html.parser')
        # Find the article element containing the problem description
        article = soup.find('article', class_='day-desc')
        # Extract the problem title from the h2 tag
        title = article.find('h2').text.strip()
        # Extract the problem description from all p tags within the article
        description = '\n'.join([p.text.strip() for p in article.find_all('p')])
        return {
            "contest_identifier": problem.contest_identifier,
            "identifier": problem.identifier,
            "title": title,
            "description": description
        }

    def get_algorithm_problems(self,
                               contest_identifier: str = "",
                               force: bool = False) -> (
        List[AdventOfCodeProblem], Dict[str, AdventOfCodeProblem]):
        """
        Get all problems in a given contest
        Args:
            contest_identifier: Identifier for the contest to be used in URL
            force: If API usage is to be forced

        Returns:
            List of all problems, Dictionary keyed on problem identifier
        """
        problems = []
        id_problem_dict = {}
        return problems, id_problem_dict

    @staticmethod
    def print_problems(problems: List[AdventOfCodeProblem], count: int = 4):
        count = len(problems) if count == -1 else count
        logging.info(f"Printing {count} problems")
        list_of_problems = []
        for problem in problems[:count]:
            list_of_problems.append(problem.convert_to_dictionary())
        print(tabulate(list_of_problems, headers="keys", tablefmt="grid"))
