# log-parser
This is python script which generates log for 1000 servers consisting of 2 CPUs each and then parses through it to give the user log details for the desired server within a given time period.

## This project has two main files.
1. log-generator - It generates log files for 1000 server machines and each server has 2 CPUs within. It generates logs for one whole day. It takes around 30 mins to generate all log files for each server.
2. log-reader - This file starts an interactive console tool which reads the desired logs from the desired server machine file within a second.

## Log Format --> Timestamp: (Unixtimestamp), CPU_id: (0 or 1), CPU: (ip_address), %usage: (between 1-100)

### Technologies / Concepts used:
Python - File Handling




