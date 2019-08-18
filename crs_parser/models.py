from datetime import datetime

class Subject(object):
    def __init__(self,course="",class_code="",class_name="",credits=0.0,
            schedule=[],instructor="",remarks="",slots_avail=0,slots_total=0,demand=0):
        self.course = course
        self.class_code = class_code
        self.class_name = class_name
        self.credits = credits
        self.schedule = schedule
        self.instructor = remarks
        self.remarks = remarks
        self.slots_avail = slots_avail
        self.slots_total = slots_total
        self.demand = demand

    def __str__(self):
        return ("course: " + self.course + 
            "\nclass_code: " + self.class_code + 
            "\nclass_name: " + self.class_name + 
            "\ncredits: " + str(self.credits) + 
            "\nschedule: " + self.str_sched() + 
            "\ninstructor: " + self.instructor + 
            "\nremarks: " + self.remarks + 
            "\nslots_avail: " + str(self.slots_avail) + 
            "\nslots_total: " + str(self.slots_total) + 
            "\ndemand: " + str(self.demand))

    def str_sched(self):
        return '; '.join(list(map(str, self.schedule)))

class Schedule(object):
    def __init__(self,days="",start_time=None,end_time=None,venue=""):
        self.days = days.replace("Th","H")
        self.start_time = start_time
        self.end_time = end_time
        self.venue = venue

    def __str__(self):
        return (self.days +
                " " + (self.start_time.strftime('%I:%M%p') if self.start_time != None else "TBA") +
                " - " + (self.end_time.strftime('%I:%M%p') if self.end_time != None else "TBA") +
                " " + self.venue)

    @classmethod
    def parse(cls, sched):
        sched = sched.strip()

        # Sample format: WF 4-5:30PM lec TBA
        # If TBA, return an empty Schedule
        if (sched == 'TBA'):
            return Schedule()
        days, se_time, *venue_list = sched.split()
        venue = ' '.join(venue_list)
        start_str, end_str = se_time.split('-')

        # Clean up the format of start_str and end_str
        # Add AM or PM to the start time
        if start_str[-1] != 'M':
            start_str = start_str + end_str[-2:]

        # strptime depending on whether or not the minute is present
        start_format = '%I:%M%p' if ':' in start_str else '%I%p'
        end_format = '%I:%M%p' if ':' in end_str else '%I%p'

        return Schedule(
                days,
                datetime.strptime(start_str, start_format),
                datetime.strptime(end_str, end_format),
                venue
                )
