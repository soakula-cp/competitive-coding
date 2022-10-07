import enum


class ApiEnum(enum.Enum):
    """
    Enum for request type
    """
    DEFAULT = 1
    GRAPHQL = 2


class JudgeEnum(enum.Enum):
    """
    Enum for judges
    """
    CODECHEF = 1
    LEETCODE = 2

    def __str__(self):
        return self.name

    @staticmethod
    def from_string(s):
        try:
            return JudgeEnum[s]
        except KeyError:
            raise ValueError()


class SourceTypeEnum(enum.Enum):
    """
    Enum for source type
    """
    PRACTICE = 1
    CONTEST = 2
    EXPLORE = 3

    def __str__(self):
        return self.name

    @staticmethod
    def from_string(s):
        try:
            return SourceTypeEnum[s]
        except KeyError:
            raise ValueError()


class WriteContentEnum(enum.Enum):
    """
    Enum for write content type
    """
    SOLUTION = 1
    DESCRIPTION = 2
    TESTCASES = 3

    def __str__(self):
        return self.name

    @staticmethod
    def from_string(s):
        try:
            return WriteContentEnum[s]
        except KeyError:
            raise ValueError()


class DifficultyEnum(enum.Enum):
    """
    Enum for difficulty type
    """
    UNKNOWN = 0
    BEGINNER = 10
    ONE_STAR__BEGINNER = 11
    ONE_STAR__ADVANCED = 12
    TWO_STAR__BEGINNER = 13
    TWO_STAR__ADVANCED = 14
    THREE_STAR__BEGINNER = 15
    THREE_STAR__ADVANCED = 16
    FOUR_STAR = 17
    FIVE_STAR = 18
    SIX_STAR = 19
    SEVEN_STAR = 20
    EASY = 30
    MEDIUM = 31
    HARD = 32

    def __str__(self):
        string_mapping = {
            self.UNKNOWN: "Unknown",
            self.BEGINNER: "Beginner",
            self.ONE_STAR__BEGINNER: "1* Beginner",
            self.ONE_STAR__ADVANCED: "1* Advanced",
            self.TWO_STAR__BEGINNER: "2* Beginner",
            self.TWO_STAR__ADVANCED: "2* Advanced",
            self.THREE_STAR__BEGINNER: "3* Beginner",
            self.THREE_STAR__ADVANCED: "3* Advanced",
            self.FOUR_STAR: "4*",
            self.FIVE_STAR: "5*",
            self.SIX_STAR: "6*",
            self.SEVEN_STAR: "7*",
            self.EASY: "Easy",
            self.MEDIUM: "Medium",
            self.HARD: "Hard"
        }
        # Reference: https://stackoverflow.com/questions/23951641/how-to-convert-int-to-enum-in-python
        return string_mapping[DifficultyEnum(self.value)]


class SubmissionStatusEnum(enum.Enum):
    """
    Enum for submission status
    """
    UNKNOWN = 0
    CORRECT_ANSWER = 1
    PARTIALLY_CORRECT_ANSWER = 2
    WRONG_ANSWER = 3
    TIME_LIMIT_EXCEEDED = 4
    MEMORY_LIMIT_EXCEEDED = 5
    OUTPUT_LIMIT_EXCEEDED = 6
    RUNTIME_ERROR = 7
    COMPILE_ERROR = 8


class LogLevelEnum(enum.IntEnum):
    """
    Enum for log level

    Reference: https://stackoverflow.com/questions/6060635/convert-enum-to-int-in-python
    """
    CRITICAL = 50
    ERROR = 40
    WARNING = 30
    INFO = 20
    DEBUG = 10
    NOTSET = 0

    def __str__(self):
        return self.name

    @staticmethod
    def from_string(s):
        try:
            return LogLevelEnum[s]
        except KeyError:
            raise ValueError()
