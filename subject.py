class Subject(object):
    def __init__(self,course="",class_code="",class_name="",credits=0.0,
            schedule="",instructor="",remarks="",slots_avail=0,slots_total=0,demand=0):
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
            "\nschedule: " + self.schedule + 
            "\ninstructor: " + self.instructor + 
            "\nremarks: " + self.remarks + 
            "\nslots_avail: " + str(self.slots_avail) + 
            "\nslots_total: " + str(self.slots_total) + 
            "\ndemand: " + str(self.demand))
