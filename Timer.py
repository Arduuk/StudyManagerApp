import datetime
import time


def main():
    timebool = True
    starttime = datetime.datetime.now()
    while(timebool == True):
        currenttime = datetime.datetime.now()
        passedtime = currenttime - starttime
        time.sleep(1)
        print(passedtime)
        









if __name__ =='__main__':
    main()
