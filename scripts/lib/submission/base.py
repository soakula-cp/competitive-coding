from typing import List

from lib.problem.base import Problem
from lib.utils.enums import SubmissionStatusEnum


class Submission(object):
    def __init__(self,
                 problem: Problem,
                 identifier: int,
                 tags: List[str] = None,
                 categories: List[str] = None,
                 code: List[str] = None,
                 time_complexity: str = "",
                 space_complexity: str = "",
                 judge_submission_status: SubmissionStatusEnum =
                 SubmissionStatusEnum.ACCEPTED):
        """

        Args:
            problem: problem info
            identifier: identifier for solution
            tags: tags related to the solution
            categories: categories related to the solution
            code: actual solution
            time_complexity: time complexity of the solution
            space_complexity: space complexity of the solution
            judge_submission_status: Accepted/TLE/RE/Compile Error
        """
        self.problem = problem
        self.identifier = identifier
        self.tags = [] if tags is None else tags
        self.categories = [] if categories is None else categories
        self.code = [] if code is None else code
        self.time_complexity = time_complexity
        self.space_complexity = space_complexity
        self.judge_submission_status = judge_submission_status

    def __str__(self):
        answer = "--- Solution {0} ---\n".format(self.identifier)
        answer += "               Status: '{0}'\n".format(
            self.judge_submission_status)
        answer += "      Time complexity: '{0}'\n".format(self.time_complexity)
        answer += "     Space complexity: '{0}'\n".format(self.space_complexity)
        answer += "                 Tags: '{0}'\n".format(",".join(self.tags))
        answer += "           Categories: '{0}'\n".format(
            ",".join(self.categories))
        return answer
