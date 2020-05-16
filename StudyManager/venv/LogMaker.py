import datetime
import os
import csv

def StudyLogMaker(studyLog):
    studyInfoHeader = ['Subject','Type','date','StartTime','FinishTime','Length','Info']

    studyInfo = [studyLog.subject, studyLog.type, studyLog.date.strftime('%x'), studyLog.startTime.strftime('%X'),
                 studyLog.finishTime.strftime('%X'), studyLog.StudyTime(), studyLog.info]


    fileExistsBool = False
    log_dir = os.path.dirname(os.path.realpath(__file__)) + "/StudyLogs"

    for root, dir, files in os.walk(log_dir):
        if studyLog.date.strftime('%b') + studyLog.date.strftime('%d') + '.csv' in files:
            fileExistsBool = True


    if fileExistsBool == False:
        with open("StudyLogs/" + studyLog.date.strftime('%b') + studyLog.date.strftime('%d') + '.csv', 'a') as csv_file:
             csv_writer = csv.DictWriter(csv_file, fieldnames=studyInfoHeader)

             csv_writer.writeheader()
             #adding study info to studyblock
             item = 0
             log_Dict = {}
             for key in studyInfoHeader:
                 log_Dict[key] = studyInfo[item]
                 item +=1
             csv_writer.writerow(log_Dict)

    else:
         with open("StudyLogs/" + studyLog.date.strftime('%b') + studyLog.date.strftime('%d') + '.csv', 'a') as csv_file:
             csv_writer = csv.DictWriter(csv_file, fieldnames=studyInfoHeader)

             item = 0
             log_Dict = {}
             for key in studyInfoHeader:
                 log_Dict[key] = studyInfo[item]
                 item +=1
             csv_writer.writerow(log_Dict)
