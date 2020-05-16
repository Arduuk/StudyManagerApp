import csv
import datetime
from StudyBlock import StudyBlock
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

    StudyLogMaker(studyblock)


def StudyLogMaker(studyLog):
    studyInfo = [studyLog.subject, studyLog.type, studyLog.date.strftime('%x'), studyLog.startTime.strftime('%X'),
                 studyLog.finishTime.strftime('%X'), studyLog.StudyTime(), studyLog.info]

    with open("StudyLogs/" + studyLog.date.strftime('%b') + studyLog.date.strftime('%d') + '.csv', 'a') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter="\t")

        csv_writer.writerow(studyInfo)


if __name__ == '__main__':
    main()
