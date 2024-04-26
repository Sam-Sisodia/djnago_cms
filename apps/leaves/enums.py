
from enum import Enum
class Leaveduration(Enum):
    Singleday = "Singleday"
    Multipledays = "Multipledays"
    hours = "hours"


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
