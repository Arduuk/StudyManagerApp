import datetime

class StudyBlock():
    def __init__(self, subject, type, date, startTime, finishTime, info):
        self.subject = subject
        self.type = type
        self.date = date
        self.startTime = startTime
        self.finishTime = finishTime
        self.info = info

    def StudyTime(self):
        studyLenght = self.finishTime - self.startTime
        return studyLenght
