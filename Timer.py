import datetime
import time


def main():
    timebool = True
    starttime = datetime.datetime.now()
    while(timebool == True):
        currenttime = datetime.datetime.now()
        passedtime = currenttime - starttime
        time.sleep(0.8)
        print(passedtime , end = "\r")



def StopTimer():
    while True:
        i = input()
        timebool = False

if __name__ =='__main__':
    main()
