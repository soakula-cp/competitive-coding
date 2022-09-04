from typing import List

from lib.utils.enums import SourceTypeEnum, DifficultyEnum


class BaseApi(object):
    """
    Base class for API querying for various judges
    """
    def __init__(self,
                 source_type: SourceTypeEnum = SourceTypeEnum.PRACTICE,
                 levels: List[DifficultyEnum] = None,
                 colors: List[str] = None):
        """
        Constructor
        Args:
            source_type: Type of the problem. Default: PRACTICE
            levels: Difficulty level of problem
            colors: Color to highlight the description level
        """
        assert(len(levels) == len(colors))
        self.source_type = source_type
        self.levels = [] if levels is None else levels
        self.colors = [] if colors is None else colors
