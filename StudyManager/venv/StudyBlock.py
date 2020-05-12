import datetime

class StudyBlock():
    def __init__(self,type,date,startTime,finishTime):
        self.type = type
        self.date = date
        self.startTime = startTime
        self.finishTime = finishTime

    def StudyTime(self):
        studyLenght = self.finishTime - self.startTime
        return studyLenght


