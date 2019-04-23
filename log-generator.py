import logging
import random
import time
import datetime
import os


os.chdir('.\\testLogs')


# getting cpus and random usage

cpustr = '192.168.1.'
cpuid1 = 0
cpuid2 = 1
SERVERS = 10
MINUTES_A_DAY = 20

# start date initialized

# print(dateTime.date().day)
# unixtime1 = int(time.mktime(dateTime.timetuple()))
# print(unixtime1)


# each server should generate a log every minute with 2 CPUs
for serverid in range(SERVERS):
    dateTime = datetime.datetime(2014, 10, 31, 0, 0, 0)
    # add a minute
    for minute in range(MINUTES_A_DAY):
        if dateTime.day == '1' and dateTime.month == '11':
            break

        dateTime = dateTime + datetime.timedelta(minutes=1)
        unixtime2 = int(time.mktime(dateTime.timetuple()))
        print(unixtime2)

        f = open(cpustr + str(serverid) + ".log", "a+")
        randomUsage1 = random.randint(0, 100)
        f.write(f'Timestamp: {unixtime2}, CPU: {cpustr + str(serverid)} , CPU_id: {cpuid1} , %usage: {randomUsage1}\n')
        randomUsage2 = random.randint(0, 100)
        f.write(f'Timestamp: {unixtime2}, CPU: {cpustr + str(serverid)} , CPU_id: {cpuid2} , %usage: {randomUsage2}\n')
