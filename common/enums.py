from enum import Enum


class GroupType(Enum):
    HOUR = "hour"
    DAY = "day"
    MONTH = "month"


class RequestType(Enum):
    DT_FROM = "dt_from"
    DT_UPTO = "dt_upto"
    GROUP_TYPE = "group_type"
