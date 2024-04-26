from enum import Enum


class UserType(Enum):
    Patient = "Patient"
    Doctor = "Doctor"
    Staff = "Staff"


    @classmethod
    def usertypes(cls):
        return tuple((i.name, i.value) for i in cls)