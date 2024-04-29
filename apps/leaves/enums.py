
from enum import Enum
class Leaveduration(Enum):
    Singleday = "Singleday"
    Multipledays = "Multipledays"
    Hours = "Hours"


    @classmethod
    def leavedurations(cls):
        return tuple((i.name, i.value) for i in cls)


class Leavetype(Enum):
    CasualLeave = "Casual Leave"
    MedicalLeave = "Medical Leave"
    PaidLeave  = "Paid Leave"
    @classmethod
    def leavetypes(cls):
        return tuple((i.name, i.value) for i in cls)



class LeaveHours(Enum):
    ONE_HOUR = "1"
    TWO_HOURS = "2"
    THREE_HOURS = "3"
    FOUR_HOURS = "4"
    FIVE_HOURS = "5"
    SIX_HOURS = "6"
    SEVEN_HOURS = "7"
    EIGHT_HOURS = "8"

    @classmethod
    def leave_hours(cls):
        return tuple((i.name, i.value) for i in cls)



