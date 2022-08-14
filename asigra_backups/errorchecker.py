#!/usr/bin/env python3

import re, os, smtplib, time 
from email.message import EmailMessage

body = open("example_body.txt")

def scrape_errors(email_message_body, before_index=5, after_index=4):
  """Scrapes errrors from email message body"""
  message_body_strip = [line.rstrip() for line in email_message_body]
  message_body_strip = [line for line in message_body_strip if line != ""]
  errors_only = [] 

  for index, line in enumerate(message_body_strip):
    if re.match('^Errors:\s([1-9]|[1-9][0-9]|100)', line):  
        errors_only.extend(message_body_strip[index-before_index:index+after_index])  
        errors_only.insert(index+4, "")
        with open("errors.txt", "w") as f:
          for line in range(len(errors_only)):
            f.write(f"{errors_only[line]}\n")


def validate():
  """Ensures the errors log is outputted correctly"""
  with open("errors.txt", "r") as f:
    data = f.readlines()
    first_line = data[0][:]
      
  if re.match("^Backup Set:\s", first_line):
    print(f"### Correct formatting. No further action required")
  else:
    print("\n ### Incorrect regex indexing. Re-running script... \n")  
    body = open("example_body.txt")
    scrape_errors(body, before_index=6, after_index=3)

def send_email():
  """Email the IT Service Desk to register a ticket for the errors that require investigation"""
  with open("errors.txt") as ds_client_errors:
    msg = EmailMessage()
    msg.set_content(ds_client_errors.read())

  msg["Subject"] = "Asigra errors - DS-Client"
  msg["From"] = f"{os.getenv('asigra_errors_mail')}"
  msg["To"] = f"{os.getenv('asigra_errors_recipient')}"

  mailserver = smtplib.SMTP(f"{os.getenv('asigra_errors_smtp_server')}", port=587)
  mailserver.starttls() 
  mailserver.login(f"{os.getenv('asigra_errors_mail')}", f"{os.getenv('asigra_errors_pwd')}")
  mailserver.send_message(msg)
  mailserver.quit()
  
def main():
  scrape_errors(body)
  time.sleep(10)
  validate()
  send_email()

if __name__ == "__main__":
  main()