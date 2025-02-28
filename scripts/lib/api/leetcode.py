import json
import logging
import os.path
from typing import Dict, List

from lib.api.base import BaseApi
from lib.problem.leetcode import LeetCodeProblem
from lib.utils.enums import ApiEnum, DifficultyEnum, JudgeEnum, SourceTypeEnum
from lib.utils.functions import make_api_call
from slugify import slugify
from tabulate import tabulate


class LeetCodeApi(BaseApi):
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
                DifficultyEnum.EASY, DifficultyEnum.MEDIUM, DifficultyEnum.HARD
            ],
            colors=[
                'rgb(67, 160, 71)', 'rgb(239, 108, 0)', 'rgb(233, 30, 99)'
            ])
        # URLs
        self.headers = {
            'authority': 'leetcode.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'x-newrelic-id': 'UAQDVFVRGwEAXVlbBAg=',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
            'content-type': 'application/json',
            'sec-gpc': '1',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': 'csrftoken=SYt4auAHmprCYhMeGDZwbnE0hWoSLKRLHb0A7mMpbvoAEPvjYcIdL5LtaWhQJv6B; __cfduid=dc8614cf2c524abada1e54cfa8e118d271619065816; __cf_bm=08dec7596eec629845d4f3f39086483d491e2c40-1619324757-1800-AYKgjE4h5oPn/k7bslI317JZOCKGqrKvRQEJSKFM8EyY57yFeDgrM0KTqzs/c5RUfzN8A7VceydacsvxJjrmrp4=',
        }
        # All problems - Practice
        self.url_graphql = 'https://leetcode.com/graphql'
        self.practice_problems_url = \
            'https://leetcode.com/api/problems/algorithms/'
        self.contest_problems_url = 'https://leetcode.com/contest/api/info/{0}/'
        # Input: Problem slug
        self.graphql_questionData = '{{"operationName":"questionData","variables":{{"titleSlug":\"{0}\"}},"query":"query questionData($titleSlug: String!) {{\\n  question(titleSlug: $titleSlug) {{\\n    questionId\\n    questionFrontendId\\n    boundTopicId\\n    title\\n    titleSlug\\n    content\\n    translatedTitle\\n    translatedContent\\n    isPaidOnly\\n    difficulty\\n    likes\\n    dislikes\\n    isLiked\\n    similarQuestions\\n    exampleTestcases\\n    contributors {{\\n      username\\n      profileUrl\\n      avatarUrl\\n      __typename\\n    }}\\n    topicTags {{\\n      name\\n      slug\\n      translatedName\\n      __typename\\n    }}\\n    companyTagStats\\n    codeSnippets {{\\n      lang\\n      langSlug\\n      code\\n      __typename\\n    }}\\n    stats\\n    hints\\n    solution {{\\n      id\\n      canSeeDetail\\n      paidOnly\\n      hasVideoSolution\\n      paidOnlyVideo\\n      __typename\\n    }}\\n    status\\n    sampleTestCase\\n    metaData\\n    judgerAvailable\\n    judgeType\\n    mysqlSchemas\\n    enableRunCode\\n    enableTestMode\\n    enableDebugger\\n    envInfo\\n    libraryUrl\\n    adminUrl\\n    __typename\\n  }}\\n}}\\n"}}'
        # Filenames for cache
        # Input: For a specific question
        # Input: Source type, Premium?, Contest name/Difficulty, Problem Slug
        self.filename_question = "logs/leetcode/questions/{0}/{1}{2}/{3}.json"
        # For list of problems in a contest
        # Input: Source type, Contest name/Problem category
        self.filename_problems = "logs/leetcode/categories/{0}/{1}.json"
        self.filename_all_problems = \
            "logs/leetcode/categories/practice/all.json"

    def get_question_info(self, problem: LeetCodeProblem,
                          force: bool = False) -> Dict:
        """
        Download description for the given problem
        Args:
            problem: Input problem for Leetcode
            force: If API usage is to be forced

        Returns:
            Problem description as a dictionary
        """
        if problem.judge != JudgeEnum.LEETCODE:
            print("This Api can be used only for LeetCode problems")
            exit(1)
        response = \
            make_api_call(
                url=self.url_graphql,
                filename=self.filename_question.format(
                    str(self.source_type).lower(),
                    ""
                        if self.source_type != SourceTypeEnum.PRACTICE
                        else (
                            "premium/" if problem.is_premium is True
                            else "non-premium/"),
                    str(problem.difficulty).lower()
                        if problem.source_type == SourceTypeEnum.PRACTICE
                        else problem.contest_identifier.lower(),
                    f"{problem.identifier}__{problem.problem_slug}"),
                api_type=ApiEnum.GRAPHQL, headers=self.headers,
                data=self.graphql_questionData.format(problem.problem_slug),
                force=force)
        if response is None:
            print("Question data for {0}. {1} could not be retrieved".format(
                problem.identifier, problem.title))
        question = response['data']['question']
        # markdown = md(question['content'], heading_style="ATX")
        # content = question['content']
        # exampleTestcases = question['exampleTestcases']
        # codeSnippets = question['codeSnippets'][0]['code']
        # difficulty = question['difficulty']
        # topicTags = question['topicTags']
        # hints = question['hints']
        return question

    def get_algorithm_problems(self,
                               explore_identifier: str = "",
                               contest_identifier: str = "",
                               force: bool = False) -> tuple[
        List[LeetCodeProblem], Dict[str, LeetCodeProblem]]:
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
        url = \
            self.practice_problems_url \
                if self.source_type == SourceTypeEnum.PRACTICE \
                else self.contest_problems_url.format(contest_identifier)
        response = make_api_call(url=url,
                                 filename=self.filename_problems.format(
                                     str(self.source_type).lower(),
                                     ("algorithms"
                                      if self.source_type == SourceTypeEnum.PRACTICE
                                      else contest_identifier.lower())),
                                 force=force)
        if response is None:
            print("Could not retrieve problems list")
            return
        for item in response['stat_status_pairs']:
            problem = LeetCodeProblem(
                identifier=item['stat']['frontend_question_id'],
                title=item['stat']['question__title'],
                question_slug=item['stat']['question__title_slug'],
                difficulty=self.levels[item['difficulty']['level'] - 1],
                difficulty_color=self.colors[item['difficulty']['level'] - 1],
                source_type=self.source_type,
                contest_identifier=contest_identifier,
                explore_identifier=explore_identifier,
                solution_url=item['stat']['question__article__slug'],
                status='na' if item['status'] is None else item['status'],
                is_premium=item['paid_only']
            )
            id_problem_dict[str(problem.identifier)] = problem
            problems.append(problem)
        print("There are total {0} problems in LeetCode Practice "
              "in Algorithms category".format(len(problems)))
        return problems, id_problem_dict

    @staticmethod
    def print_problems(problems: List[LeetCodeProblem], count: int = 4):
        list_of_problems = []
        for problem in problems[:count]:
            list_of_problems.append(problem.convert_to_dictionary())
        print(tabulate(list_of_problems, headers="keys", tablefmt="grid"))
