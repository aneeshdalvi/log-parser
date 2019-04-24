# log-parser
This is python script which generates log for 1000 servers consisting of 2 CPUs each and then parses through it to give the user log details for the desired server within a given time period.

## This project has two main files.
1. log-generator - It generates log files for 1000 server machines and each server has 2 CPUs within. It generates logs for one whole day. It takes around 30 mins to generate all log files for each server.
2. log_reader - This file starts an interactive console tool which reads the desired logs from the desired server machine file within a second. The tool can be stopped with an 'Exit' command.

### Log Format -
Timestamp: (Unixtimestamp), CPU_id: (0 or 1), CPU: (ip_address), %usage: (between 1-100)

## Instructions to Run:
* Run the log-generator.py file - 
```
python log-generator.py
```
- This will generate a new directory "testLogs" and generate a log file for each of 1000 servers.

* Once all the logs are generated successfully (around 30 mins later), run the log_reader.py file

```
python log_reader.py
```
After you use the above command the tool will ask you several inputs which you need to enter it correctly to get the desired logs from the server log files.

### Inputs needed to enter by the user - 

1. Server IP address - It must be exactly same as the servername generated on the log file
2. CPU_ID - It can either be 0 or 1
3. Start Time - It must follow (YYYY-MM-DD HH:MM) format
4. End Time - It must follow (YYYY-MM-DD HH:MM) format

- If the user enters all the above details correctly, he/she will get the desired log details for the given time period within a second.
- If the users fails to give correct input, the user will get an error message by the tool saying that user has entered wrong input.
- The tool will keep continuing to fetch log details until the user denys to continue 
- The tool stops when user types 'exit' command.
  
### Technologies / Concepts used:
Python - File Handling




