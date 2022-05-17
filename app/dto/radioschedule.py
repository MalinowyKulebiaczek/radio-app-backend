from app.constants.constants import WeekDays
from app.dto.auditions import auditions_list


class RadioScheduleDTO:
    def __init__(self, auditions):
        self.schedule = RadioScheduleDTO.create_schedule(auditions)

    @staticmethod
    def create_schedule(auditions):
        schedule = {}
        for audition in auditions:
            if audition.day in WeekDays.LIST:  # check if day is properly defined
                if audition.day not in schedule:
                    schedule[audition.day] = []
                schedule[audition.day].append(audition)
        return schedule


radio_schedule_dto = RadioScheduleDTO(auditions_list)
if __name__ == '__main__':
    print(radio_schedule_dto.schedule)
