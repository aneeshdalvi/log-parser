import logging
import random
import time
import datetime


PATH = 'test.log'
logging.basicConfig(filename=PATH, level=logging.INFO,
                    format=f'%(message)s')


# getting cpus and random usage
SERVERID = 0
cpustr = '192.168.1.'
cpuid1 = 0
cpuid2 = 1
SERVERS = 1000
MINUTES_A_DAY = 1440

# start date initialized
dateTime = datetime.datetime(2014, 10, 31, 0, 0, 0)
# print(dateTime.date().day)
unixtime1 = int(time.mktime(dateTime.timetuple()))
# print(unixtime1)


# 1440 minutes in a day
for i in range(MINUTES_A_DAY):
    # add a minute
    dateTime = dateTime + datetime.timedelta(minutes=1)
    unixtime2 = int(time.mktime(dateTime.timetuple()))
    print(unixtime2)
    SERVERID = 0
    # each server should generate a log every minute with 2 CPUs
    for i in range(SERVERS):
        randomUsage1 = random.randint(0, 100)
        logging.info(f'Timestamp: {unixtime2}, CPU: {cpustr + str(SERVERID)} , CPU_id: {cpuid1} , %usage: {randomUsage1}')
        randomUsage2 = random.randint(0, 100)
        logging.info(f'Timestamp: {unixtime2}, CPU: {cpustr + str(SERVERID)} , CPU_id: {cpuid2} , %usage: {randomUsage2}')
        SERVERID += 1
