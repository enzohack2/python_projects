### Previous workflow

1. Service desk agents had to manully screen large backup logs for errors and paste the errors into the worknotes of tickets.
2. The agent then checks the logs for the root cause of the error and then either flags it as not worthy of further investigating or push the error to the infrastructure team.

### Automated workflow for processing asigra errors

1. Leverages VBA for deploying a Jenkins build server that pulls code from a github repository to scrape errors in a log file and email them to the service desk. 
2. The service desk only need to work on getting to the root cause of errors logged by the ds-client
3. Errors log hits an email address that has a rule to launch a shell with VBA in order to execute a command. Errors log example

```
Daily Admin Summary:
Completion: Normal
Database backup: OK
Synchronization check: Not performed
Backup Activities Summary since Jul 28, 2022, 7:00:00 AM
Number of backup activities: 14
Total backup amount: 24,918,014 KB
Total number of files: 10,869
Scheduled backups: 14
Backups not fully completed: 0
Backups with some errors: 7
Backup Activities Details:
Backup Set: UNIX-SSH\rmg-db-04\Backup of MySQL configuration\rmg-asigra
Performed by: Backup Schedule: Weekdays Backup (8pm)
Started at: Jul 28, 2022, 8:00:00 PM
Finished at: Jul 28, 2022, 8:00:14 PM
Completion: Backup completed successfully.
Warnings: 0
Errors: 0
Backed up files: 0
Total amount: 0 KB
Backup Set: UNIX-SSH\rmg-devweb-03\Backup of web code and configuration\rmg-asigra
Performed by: Backup Schedule: Weekdays Backup (8pm)
Started at: Jul 28, 2022, 8:00:00 PM
Finished at: Jul 28, 2022, 8:28:00 PM
Completion: Backup completed with errors.
Warnings: 0
Errors: 4
Backed up files: 4,361
Total amount: 441,780 KB
Backup Set: UNIX-SSH\rmg-web-03\New Backup of /\root
Performed by: Backup Schedule: Weekdays Backup (8pm)
Started at: Jul 28, 2022, 8:00:00 PM
Finished at: Jul 28, 2022, 8:05:25 PM
Completion: Backup completed with errors.
Warnings: 0
Errors: 136
Backed up files: 113
Total amount: 212,981 KB
Backup Set: UNIX-SSH\rmg-sysint-12\Backup of /server and nginx\rmg-asigra
Performed by: Backup Schedule: Weekdays Backup (11pm)
Started at: Jul 28, 2022, 11:00:00 PM
Finished at: Jul 28, 2022, 11:01:55 PM
Completion: Backup completed successfully.
Warnings: 0
Errors: 0
```
4. Code processes data and writes the errors from the log to `errors.txt`. 
5. `errors.txt` file goes through a validation check ensuring the first line startswith `Backup Set:`. 
6. Example of incorrect format:
```
Performed by: Backup Schedule: Weekdays Backup (8pm)
Started at: Jul 28, 2022, 8:00:00 PM
Finished at: Jul 28, 2022, 8:28:00 PM
Completion: Backup completed with errors.
Warnings: 0
Errors: 4
Backed up files: 4,361
Total amount: 441,780 KB
Backup Set: UNIX-SSH\rmg-web-03\New Backup of /\root
```
7. Correct formatting for the `errors.txt` file is acheived via the `validate()` function.
* Reference `errorchecker.py` for the `validate()` function
* Exmaple of correct format of errors for `errors.txt`:
```
Backup Set: UNIX-SSH\rmg-devweb-03\Backup of web code and configuration\rmg-asigra
Performed by: Backup Schedule: Weekdays Backup (8pm)
Started at: Jul 28, 2022, 8:00:00 PM
Finished at: Jul 28, 2022, 8:28:00 PM
Completion: Backup completed with errors.
Warnings: 0
Errors: 4
Backed up files: 4,361
Total amount: 441,780 KB
```
8. Function `send_email()` proceeds to leverage smtp library for message sending and the email.message module for email message handline
* Example email sent once code is ran: `python.exe .\errorchecker.py`



### Sources for learning

1. Mailer module documentation: https://github.com/marrow/mailer
2. https://pypi.org/project/mailer/0.3/
3. Leveraging the email package: https://docs.python.org/3/library/email.examples.html 
4. Sending email with smtplib: https://realpython.com/python-send-email/
5. Set environment variables powershell: https://www.tutorialspoint.com/how-to-set-environment-variables-using-powershell 