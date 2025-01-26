from typing import List

from lib.problem.base import Problem
from lib.utils.enums import SubmissionStatusEnum


class AlgorithmMetadata(object):
    def __init__(self,
                time_complexity: str = "",
                space_complexity: str = "",
                tags: List[str] = None,
                categories: List[str] = None):
        """

        Args:
            time_complexity: time complexity of the submission
            space_complexity: space complexity of the submission
            tags: tags related to the submission
            categories: categories related to the submission
        """
        self.time_complexity = time_complexity
        self.space_complexity = space_complexity
        self.tags = tags
        self.categories = categories

    def __str__(self):
        answer = "--- Algorithm Metadata ---\n"
        answer += " Time complexity: '{0}'\n".format(self.time_complexity)
        answer += "Space complexity: '{0}'\n".format(self.space_complexity)
        answer += "            Tags: '{0}'\n".format(",".join(self.tags))
        answer += "      Categories: '{0}'\n".format(",".join(self.categories))
        return answer


class JudgeMetadata(object):
    def __init__(self,
                url: str = "",
                status: SubmissionStatusEnum = SubmissionStatusEnum.UNKNOWN,
                runtime: str = "",
                memory: str = "",
                runtime_performance: str = "",
                memory_performance: str = ""):
        """

        Args:
            url:
            status: Accepted/TLE/RE/Compile Error etc.,
            runtime:
            memory:
            runtime_performance:
            memory_performance:
        """
        self.url = url
        self.status = status
        self.runtime = runtime
        self.runtime_performance = runtime_performance
        self.memory = memory
        self.memory_performance = memory_performance

    def __str__(self):
        answer = "--- Judge Metadata ---\n"
        answer += "   Link: '{0}'\n".format(self.url)
        answer += " Status: '{0}'\n".format(self.status)
        answer += "Runtime: '{0}'\n".format(self.runtime)
        answer += " Memory: '{0}'\n".format(self.memory)
        return answer


class Submission(object):
    def __init__(self,
                 problem: Problem,
                 identifier: int,
                 code: List[str],
                 algorithm_metadata: AlgorithmMetadata,
                 judge_metadata: JudgeMetadata):
        """

        Args:
            problem: problem info
            identifier: identifier for solution
            code: actual code submission
            judge_submission_status: Accepted/TLE/RE/Compile Error
        """
        self.problem = problem
        self.identifier = identifier
        self.judge_metadata = judge_metadata
        self.algorithm_metadata = algorithm_metadata
        self.code = [] if code is None else code

    def __str__(self):
        answer = "=== Solution {0} ===\n".format(self.identifier)
        answer += str(self.judge_metadata)
        answer += str(self.algorithm_metadata)
        return answer
