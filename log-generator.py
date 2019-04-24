import logging
import random
import time
import datetime
import os

os.mkdir('.\\testLogs')
os.chdir('.\\testLogs')


# getting cpus and random usage

cpustr = '192.168.'
cpuid1 = 0
cpuid2 = 1
SERVERS = 1000
MINUTES_A_DAY = 1440
serverid = 1
serverid1 = 0

# start date initialized

# print(dateTime.date().day)
# unixtime1 = int(time.mktime(dateTime.timetuple()))
# print(unixtime1)


# each server should generate a log every minute with 2 CPUs
for server in range(SERVERS):
    dateTime = datetime.datetime(2014, 10, 31, 0, 0, 0)
    # add a minute
    for minute in range(MINUTES_A_DAY):
        if dateTime.day == '1' and dateTime.month == '11':
            break

        if serverid1 > 255:
            serverid1 = 0
            serverid += 1

        dateTime = dateTime + datetime.timedelta(minutes=1)
        unixtime2 = int(time.mktime(dateTime.timetuple()))
        # print(unixtime2)

        f = open(cpustr + str(serverid) + "." + str(serverid1) + ".log", "a+")
        randomUsage1 = random.randint(0, 100)
        f.write(f'Timestamp: {unixtime2}, CPU: {cpustr + str(serverid) + "." + str(serverid1)} , CPU_id: {cpuid1} , %usage: {randomUsage1}\n')
        randomUsage2 = random.randint(0, 100)
        f.write(f'Timestamp: {unixtime2}, CPU: {cpustr + str(serverid) + "." + str(serverid1)} , CPU_id: {cpuid2} , %usage: {randomUsage2}\n')

    serverid1 += 1
