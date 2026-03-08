from enum import Enum


class AllureEpic(str, Enum):
    LMS = "LMS service"
    STUDENT = "STUDENT SERVICE"
    ADMINISTRATION = "Administration service"
    