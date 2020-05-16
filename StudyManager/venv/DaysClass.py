import csv
import time


class DaysClass:
    def __init__(self, logFile):
        self.logFile = logFile

    def ShowInfo(self):
        # studyTime = time.strptime("0:00:00" , "%H:%M:%S")
        with open(self.logFile, 'r') as csv_file:
            csv_reder = csv.reader(csv_file, delimiter='\t')

            for row in csv_file:
                print(row)
                print(row[0])
                # studyTime += time.strptime(row[3], "%H:%M:%S")
            # print(studyTime)
