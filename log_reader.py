import os
import ast
import datetime
import time
import sys

# need to have this directory which have log files
os.chdir('.\\testLogs')

# take user input
# print(sys.argv)
# 192.168.1.09 1 2014-10-31 00:00 2014-10-31 00:05
flag = 0
while True:
    if flag != 0:
        i = input('Do you want to continue?(Y/N): ')
        if i.lower() == 'y':
            inputFile = input('Enter ip address: ')
            inputFile = inputFile.strip()
            cpuID = input('Enter cpuID: ')
            cpuID = cpuID.strip()
            starttime = input('Enter start datetime: ')
            starttime = starttime.strip()
            endtime = input('Enter end datetime: ')
            endtime = endtime.strip()
            # print(inputFile, cpuID, starttime, endtime)

            try:

                start_date_time = datetime.datetime.strptime(starttime, "%Y-%m-%d %H:%M")
                end_date_time = datetime.datetime.strptime(endtime, "%Y-%m-%d %H:%M")
                # print("date and time:", date_time.hour)

                startdateTime = datetime.datetime(start_date_time.year, start_date_time.month, start_date_time.day, start_date_time.hour, start_date_time.minute)
                startunixtime = int(time.mktime(startdateTime.timetuple()))
                # print(startunixtime)

                enddateTime = datetime.datetime(end_date_time.year, end_date_time.month, end_date_time.day, end_date_time.hour, end_date_time.minute)
                endunixtime = int(time.mktime(enddateTime.timetuple()))
                # print(endunixtime)

                # check if cpuID is either 1 or 0
                if cpuID != '1' and cpuID != '0':
                    raise Exception

                with open(inputFile + ".log", "r") as f:
                    # showing the user details as expected
                    print(f"CPU{int(cpuID)} usage on {inputFile}:")

                    for line in f:
                        line = ''.join(line)
                        line = line.rstrip()

                        line = line.split(',')
                        # print(line)

                        timestamp = line[0].split('Timestamp: ')
                        timestamp = ''.join(timestamp)
                        timestamp.strip()
                        # print(timestamp)

                        cpu = line[1].split(' CPU: ')
                        cpu = ''.join(cpu)
                        cpu.strip()
                        # print(cpu)

                        cpu_id = line[2].split(' CPU_id: ')
                        cpu_id = ''.join(cpu_id)
                        cpu_id.strip()
                        # print(cpu_id)

                        usage = line[3].split(' %usage: ')
                        usage = ''.join(usage)
                        usage.strip()
                        # print(usage)

                        # check start time and end time
                        if startunixtime > endunixtime:
                            raise Exception

                        # check unixtime logic
                        # check if timestamp is between start and end time
                        if startunixtime <= int(timestamp) <= endunixtime:
                            # print(startunixtime, timestamp, endunixtime)
                            ans = {
                                'timestamp': timestamp,
                                'cpu_id': cpu_id,
                                'usage': usage
                            }

                            # check for CPU id..
                            if int(ans['cpu_id']) == int(cpuID):
                                readableDate = datetime.datetime.fromtimestamp(int(ans['timestamp']))
                                print(f"({readableDate}, {ans['usage']}%)", end=' ', flush=True)
                    print()
            except Exception:
                print('\nError: Wrong input given. Please check your input values')
        # if user clicks 'N'
        else:
            exit = input('\nPlease type "EXIT" to quit from this tool.. ')
            if exit.lower() == 'exit':
                sys.exit()
            else:
                pass
    # for the first run
    else:

        inputFile = input('Enter ip address: ')
        inputFile = inputFile.strip()
        cpuID = input('Enter cpuID: ')
        cpuID = cpuID.strip()
        starttime = input('Enter start datetime: ')
        starttime = starttime.strip()
        endtime = input('Enter end datetime: ')
        endtime = endtime.strip()
        # print(inputFile, cpuID, starttime, endtime)

        try:

            start_date_time = datetime.datetime.strptime(starttime, "%Y-%m-%d %H:%M")
            end_date_time = datetime.datetime.strptime(endtime, "%Y-%m-%d %H:%M")
            # print("date and time:", date_time.hour)

            startdateTime = datetime.datetime(start_date_time.year, start_date_time.month, start_date_time.day, start_date_time.hour, start_date_time.minute)
            startunixtime = int(time.mktime(startdateTime.timetuple()))
            # print(startunixtime)

            enddateTime = datetime.datetime(end_date_time.year, end_date_time.month, end_date_time.day, end_date_time.hour, end_date_time.minute)
            endunixtime = int(time.mktime(enddateTime.timetuple()))
            # print(endunixtime)

            # check if cpuID is either 1 or 0
            # print(cpuID != '1' or)
            if cpuID != '1' and cpuID != '0':
                raise Exception

            with open(inputFile + ".log", "r") as f:

                # showing the user details as expected
                print(f"CPU{int(cpuID)} usage on {inputFile}:")

                for line in f:
                    line = ''.join(line)
                    line = line.rstrip()

                    line = line.split(',')
                    # print(line)

                    timestamp = line[0].split('Timestamp: ')
                    timestamp = ''.join(timestamp)
                    timestamp.strip()
                    # print(timestamp)

                    cpu = line[1].split(' CPU: ')
                    cpu = ''.join(cpu)
                    cpu.strip()
                    # print(cpu)

                    cpu_id = line[2].split(' CPU_id: ')
                    cpu_id = ''.join(cpu_id)
                    cpu_id.strip()
                    # print(cpu_id)

                    usage = line[3].split(' %usage: ')
                    usage = ''.join(usage)
                    usage.strip()
                    # print(usage)

                    # check start time and end time
                    if startunixtime > endunixtime:
                        raise Exception

                    # check unixtime logic
                    # check if timestamp is between start and end time
                    if startunixtime <= int(timestamp) <= endunixtime:
                        # print(startunixtime, timestamp, endunixtime)
                        ans = {
                            'timestamp': timestamp,
                            'cpu_id': cpu_id,
                            'usage': usage
                        }

                        # check for CPU id..
                        if int(ans['cpu_id']) == int(cpuID):
                            readableDate = datetime.datetime.fromtimestamp(int(ans['timestamp']))
                            print(f"({readableDate}, {ans['usage']}%)", end=' ', flush=True)
                print()
                flag += 1
        except Exception:
            print('\nError: Wrong Input given. Please check your input values')
