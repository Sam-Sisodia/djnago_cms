from enum import Enum


class AppointmentDuration(Enum):
    MINUTES_15 = '15 minutes'
    MINUTES_30 =  '30 minutes'
    MINUTES_45 = '45 minutes'
    HOURS_1 =  '1 hour'

    @classmethod
    def appointment_time(cls):
        return tuple((i.name, i.value) for i in cls)
 



