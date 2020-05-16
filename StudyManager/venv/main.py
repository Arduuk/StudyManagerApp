import datetime
from StudyBlock import StudyBlock
import LogMaker
#from DaysClass import DaysClass
import time



def main():
    studySub = input("Please enter the subject of study: ")
    studyType = input("Please enter the study type: ")
    input("Please enter when you start: ")
    startTime = datetime.datetime.now()
    print(startTime)

    input("Please enter when your are finished:")
    finishTime = datetime.datetime.now()
    print(finishTime)

    studyInfo = input("PLease enter the study details: ")

    studyblock = StudyBlock(studySub,studyType, startTime.date(), startTime, finishTime, studyInfo)

    LogMaker.StudyLogMaker(studyblock)



if __name__ == '__main__':
    main()
