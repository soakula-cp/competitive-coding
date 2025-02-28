import json
import logging
import os.path
from typing import Dict, List

from lib.api.base import BaseApi
from lib.problem.codechef import CodeChefProblem
from lib.utils.enums import DifficultyEnum, JudgeEnum, SourceTypeEnum
from lib.utils.functions import make_api_call
from slugify import slugify
from tabulate import tabulate


class CodeChefApi(BaseApi):
    """
    Class handling requests to Codechef API
    """

    def __init__(self,
                 source_type: SourceTypeEnum = SourceTypeEnum.PRACTICE):
        """

        Args:
            source_type:
        """
        super().__init__(
            source_type=source_type,
            levels=[
                DifficultyEnum.BEGINNER,
                DifficultyEnum.ONE_STAR__BEGINNER,
                DifficultyEnum.ONE_STAR__ADVANCED,
                DifficultyEnum.TWO_STAR__BEGINNER,
                DifficultyEnum.TWO_STAR__ADVANCED,
                DifficultyEnum.THREE_STAR__BEGINNER,
                DifficultyEnum.THREE_STAR__ADVANCED,
                DifficultyEnum.FOUR_STAR,
                DifficultyEnum.FIVE_STAR,
                DifficultyEnum.SIX_STAR,
                DifficultyEnum.SEVEN_STAR
            ],
            colors=[
                "#666666", "#666666", "#666666",
                "#1E7D22", "#1E7D22",
                "#3366CC", "#3366CC",
                "#684273", "#FFBF00", "#FF7F00", "#D0011B"
            ])
        # URLs
        # All problems - Practice
        self.practice_problems_url = \
            "https://www.codechef.com/api/list/problems?" \
            "start_rating={0}&end_rating={1}&"
        self.sort_criteria = \
            "page=0&limit=1300&sort_by=difficulty_rating&" \
            "sort_order=asc&search=&category=rated&"
        self.ratings = [
            0, 1000, 1200, 1400, 1500, 1600, 1700, 1800, 2000, 2200, 2500, 5001]
        self.ratings_description = [
            "Beginner", "1* Beginner", "1* Advanced", "2* Beginner",
            "2* Advanced",
            "3* Beginner", "3* Advanced", "4*", "5*", "6*", "7*"]
        assert (len(self.ratings) - 1 == len(self.ratings_description))
        self.practice_url_problems = []
        for idx, description in enumerate(self.ratings_description):
            self.practice_url_problems.append(
                "{0}{1}".format(
                    self.practice_problems_url.format(self.ratings[idx] + 1,
                                                      self.ratings[idx + 1]),
                    self.sort_criteria))
        # All problems - Contest
        # Input: Contest name
        self.contest_problems_url = "https://www.codechef.com/api/contests/{0}/"
        # Specific problem
        # Input: Contest name (PRACTICE is the Contest name for
        #        PRACTICE problems), Problem Slug
        self.problem_url = \
            "https://www.codechef.com/api/contests/{0}/problems/{1}"
        # Filenames for cache
        # Input: For a specific question
        # Input: Source type, Contest name/Difficulty, Problem Slug
        self.filename_question = "logs/codechef/questions/{0}/{1}/{2}.json"
        # For list of problems in a contest
        # Input: Source type, Contest name/Difficulty
        self.filename_problems = "logs/codechef/categories/{0}/{1}.json"
        self.filename_all_problems = "logs/codechef/categories/practice/all.json"

    def get_question_info(self, problem: CodeChefProblem,
                          force: bool = False) -> Dict:
        """
        Download description for the given problem
        Args:
            problem: Input problem
            force: If API usage is to be forced

        Returns:
            Problem description as a dictionary
        """
        if problem.judge != JudgeEnum.CODECHEF:
            print("This Api can be used only for CodeChef problems")
            exit(1)
        response = make_api_call(
            url=self.problem_url.format(
                problem.contest_identifier.upper(), problem.identifier),
            filename=self.filename_question.format(
                str(problem.source_type).lower(),
                slugify(str(problem.difficulty)).lower()
                if problem.source_type == SourceTypeEnum.PRACTICE
                else problem.contest_identifier.upper(),
                problem.identifier),
            force=force)
        if response is None:
            print("Question data for {0}. {1} could not be retrieved".format(
                problem.identifier, problem.title))
        return response

    def get_algorithm_problems(self,
                               explore_identifier: str = "",
                               contest_identifier: str = "PRACTICE",
                               force: bool = False) -> tuple[
        List[CodeChefProblem], Dict[str, CodeChefProblem]]:
        """
        Get all problems in a given contest/practice
        Args:
            explore_identifier: Identifier for the explore content
            contest_identifier: Identifier for the contest to be used in URL
            force: If API usage is to be forced

        Returns:
            List of all problems, Dictionary keyed on problem identifier
        """
        problems = []
        id_problem_dict = {}
        if self.source_type == SourceTypeEnum.PRACTICE:
            if os.path.exists(self.filename_all_problems) and force is False:
                response = None
                with open(self.filename_all_problems, 'r') as read_file:
                    response = json.load(read_file)
                for item in response['data']:
                    difficulty_rating = int(item['difficulty_rating'])
                    difficulty_idx = 0
                    for i in range(len(self.ratings) - 1):
                        if self.ratings[i] < difficulty_rating <= self.ratings[i+1]:
                            difficulty_idx = i
                    problem = CodeChefProblem(
                        identifier=item['code'],
                        title=item['name'],
                        question_slug=item['code'],
                        source_type=self.source_type,
                        contest_identifier=contest_identifier,
                        explore_identifier=explore_identifier,
                        difficulty=self.levels[difficulty_idx],
                        difficulty_color=self.colors[difficulty_idx],
                        solution_url=item['editorial_link']
                        if 'editorial_link' in item else "")
                    id_problem_dict[problem.identifier] = problem
                    problems.append(problem)
                return problems, id_problem_dict
        url_problems = \
            self.practice_url_problems \
                if self.source_type == SourceTypeEnum.PRACTICE \
                else [
                self.contest_problems_url.format(contest_identifier.upper())]
        difficulty_categories = \
            self.ratings_description \
                if self.source_type == SourceTypeEnum.PRACTICE else [
                contest_identifier.upper()]
        combined_response = None
        for idx, (url, category) in enumerate(
            zip(url_problems, difficulty_categories)):
            current_problems = []
            response = make_api_call(
                url=url,
                filename=self.filename_problems.format(
                    str(self.source_type).lower(), slugify(category).lower()),
                force=force)
            if response is None:
                print(f"Could not retrieve problems list for {category}")
                return 255
            if combined_response is None:
                combined_response = response
            else:
                combined_response['data'].extend(response['data'])
            data = \
                response['data'] \
                    if self.source_type == SourceTypeEnum.PRACTICE \
                    else response['problems']
            for item in data:
                item = item \
                    if self.source_type == SourceTypeEnum.PRACTICE \
                    else data[item]
                problem = CodeChefProblem(
                    identifier=item['code'],
                    title=item['name'],
                    question_slug=item['code'],
                    source_type=self.source_type,
                    contest_identifier=contest_identifier,
                    explore_identifier=explore_identifier,
                    difficulty=""
                    if self.source_type != SourceTypeEnum.PRACTICE
                    else self.levels[idx],
                    difficulty_color=""
                    if self.source_type != SourceTypeEnum.PRACTICE
                    else self.colors[idx],
                    solution_url=item['editorial_link']
                    if 'editorial_link' in item else "")
                id_problem_dict[problem.identifier] = problem
                current_problems.append(problem)
            logging.info(
                "There are total {0} problems in CodeChef {1} - {2}".format(
                    len(current_problems),
                    str(self.source_type).lower().capitalize(),
                    category))
            problems += current_problems
        if self.source_type == SourceTypeEnum.PRACTICE:
            with open(self.filename_all_problems, 'w') as write_file:
                json.dump(combined_response, write_file)
        return problems, id_problem_dict

    @staticmethod
    def print_problems(problems: List[CodeChefProblem], count: int = 4):
        count = len(problems) if count == -1 else count
        logging.info(f"Printing {count} problems")
        list_of_problems = []
        for problem in problems[:count]:
            list_of_problems.append(problem.convert_to_dictionary())
        print(tabulate(list_of_problems, headers="keys", tablefmt="grid"))
