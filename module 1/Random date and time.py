import random

import time

def getRandomDate(startDate, endDate): # Generate a random date and time
    print("Printing random date between",startDate,"and",endDate)
    randomGenrater= random.Random()
    dateFormat = '%m,%d,%y '

    startTime   = time.mktime(time.strptime(startDate, dateFormat))
    endTime     = time.mktime(time.strptime(endDate, dateFormat))
    randomTime  = startTime+randomGenrater.randint(0, endTime - startTime)
    randonDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randonDate

print("Ramdom Date =", getRandomDate('01,01,2020', '12,31,2025'))