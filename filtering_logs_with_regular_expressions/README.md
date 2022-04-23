# Backup error logs filter

### Information
* Author: Joshua Musiyarira
* Current version: 0.1
* Date created: 23/04/2022
* Requirements: python 3.x and a txt file in the same directory as the python file: "asigra_errors01.py"
* Python modules: `import re, itertools, time, sys`

### Introduction
* A company performs overnight differential backups in Asigra and has a log of each backup sent to it's IT Service desk team.
* Service desk analysts are required to manually read through each log and report on any erorrs found in the backup log to the infrastructure team.
* This requires pressing: `CTRL+F, Errors: [inputting a value starting from 1]` and copying and pasting each errors found in a separate work note on tickets logged to the service desk.
* As it can take more than 5 minutes to complete reviewing a log that has many errors and when 8+ tickets of backup logs come in this consumes valuable time that the service desk analysts can deploy elsewhere to increase service desk value to clients. This would take a single agent 40 minutes to copmlete a systematic task.
* This time consuming process has been automated via the use of pythonic logic and regular expressions. 
* An agent is required to copy the entire log information, excluding the initial daily summary and paste it in the "asigra_backup.txt" file.
* The agent then runs the python script: `asigra_errors.py`
* The script outputs the file `asigra_errors.txt`, of which contains all errors found in the log
* The agent has to simoply copy the errors in the log and then 


### Example usage when errors are present
1. Refer to the input file containing the error log: `asigra_backup.txt` and output file `asigra_errors.txt`


### Example usage when no errors are present
1. Refer to the `asigra_backup_no_errors.txt` file.
2. When the above log containing no errors is ran with te python script: `asigra_errors.py`, it returns the below output to the terminal:

`
No errors found
Gracefully exiting
`

### Future improvemments
1. Web scraping could be implemented in order to automatically scrape the asigra backup tixket that is sent to the service desk team
* This would reomve the potential for human error when copying  a log information from a ticket to the `asigra_backup.txt` file
2. The script could be onverted into a single click application where the script monitors the queue for incoming service desk tickets.
* The script would then scrape the page and if errors are found, perfrom the needful and alert the infrastructure team of errors found via email.
* If no errors where found the script would simply close the asigra backup ticket. 
* This could be acheived via a serveless implementation of web-sraping with selenium. 
