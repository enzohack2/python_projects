#!/usr/bin/env python3

import imaplib # used to establish connection to email server
import os # used to get environment variables in current directory
from pathlib import Path # used to state path of environment
from dotenv import load_dotenv # used to load the environment variables 

# parse server, email address and associated email password from .env file

env_path = Path(".") / ".env" 
load_dotenv(dotenv_path=env_path)

server = os.getenv("SERVER")
user = os.getenv("EMAIL_ADDRESS")
passwd = os.getenv("PASSWD")


# connect to server

def server_connect(server, email_add, pword):
    """Connects to an email address given the email's server, address and associated password"""
    conn = imaplib.IMAP4_SSL(server) # connecting to email server over an encrypted SSL connection
    conn.login(user=email_add, password=pword) # identifying the client to login to
    return conn

# delete email

def email_deletion(inst, mail_id):
    """Delete an email given it's instance, @inst, of which is fetched by it's given ID, @mail_id."""
    type_, del_response = inst.fetch(mail_id, "(FLAGS)") # Fetch (parts of) messages 
    type_, response = inst.store(mail_id, "+FLAGS", r"(\Deleted)")

    # printing response - verbose output 
    print(del_response)
    print(response)

# function that purges email instance. Run once an email has been deleted. 
def mail_purge(inst):
    typ_, response = inst.expunge() # Permanently remove deleted items from selected mailbox 
    print(response)


# list of keywords to be searched for and found in the body of emails.
# mu test email is from -Walter
# email search list

email_search = ["Walter", "walter", "-Walter"]

# iterating over keyword list for every email in 
for kword in email_search:
    conn = server_connect(server, user, passwd)

    # seleecting email folder to search for, in this instance, the inbox
    conn.select("inbox")

    # searching email body's text for keyword 
    typ_, msg = conn.search(None, 'BODY "' + kword + '")')
    print(msg) 
    msg = msg[0].split()

    for email_id in msg:
        print(email_id) # email id
        email_deletion(conn, email_id)

    mail_purge(conn)
    print("Deletion complete!")


# imaplib documentation: https://docs.python.org/3/library/imaplib.html 
