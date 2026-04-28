from datetime import datetime
from datetime import timedelta

class Timer:
    def __init__(self, maxSeconds):
        self.__before = datetime.now()
        self.__maxSeconds = maxSeconds

    def hasEnded(self):
        dateTimeBeforeDelta = self.__before + timedelta(seconds = self.__maxSeconds)
        dateTimeNow = datetime.now()

        return dateTimeBeforeDelta < dateTimeNow

    def reset(self):
        self.__before = datetime.now()

    def getRemaingTime(self):
        dateTimeLimit = self.__before + timedelta(seconds=self.__maxSeconds)
        dateTimeNow = datetime.now()

        return int((dateTimeLimit - dateTimeNow).total_seconds()) + 1
        

#Uso da classe:
shootTimer = Timer(4)

if shootTimer.hasEnded():
    shootTimer.reset()
    #acontece algo