from enum import Enum

from enum import Enum
from datetime import datetime, timedelta
# class AppointmentDuration(Enum):
#     MINUTES_15 = '15 minutes'
#     MINUTES_30 =  '30 minutes'
#     MINUTES_45 = '45 minutes'
#     HOURS_1 =  '1 hour'

#     @classmethod
#     def appointment_time(cls):
#         return tuple((i.name, i.value) for i in cls)
    

class AppointmentDuration(Enum):
    @classmethod
    def appointment_time(cls):
        current_time = datetime.strptime('00:00', '%H:%M')
        end_time = datetime.strptime('23:59', '%H:%M')
        intervals = []
        while current_time <= end_time:
            intervals.append((current_time.strftime('%H:%M'), current_time.strftime('%H:%M')))
            current_time += timedelta(minutes=15)
        return tuple(intervals)




class UserType(Enum):
    Patient = "Patient"
    Doctor = "Doctor"
    Staff = "Staff"


    @classmethod
    def usertypes(cls):
        return tuple((i.name, i.value) for i in cls)

