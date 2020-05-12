import csv
import datetime
from StudyBlock import StudyBlock
import time


def main():
    studySub = input("Please enter the subject of study: ")
    input("Please enter when you start: ")
    startTime = datetime.datetime.now()
    print(startTime)

    input("Please enter when your are finished:")
    finishTime = datetime.datetime.now()
    print(finishTime)

    studyblock = StudyBlock(studySub,startTime.date(),startTime,finishTime)

    StudyLogMaker(studyblock)

def StudyLogMaker(studyLog):
    studyInfo = [studyLog.type,studyLog.date.strftime('%x'),studyLog.startTime.strftime('%X'),studyLog.finishTime.strftime('%X'),studyLog.StudyTime()]


    with open(studyLog.date.strftime('%b')+studyLog.date.strftime('%d')+'.csv' , 'a') as csv_file:
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(studyInfo)



if __name__ =='__main__':

    main()
