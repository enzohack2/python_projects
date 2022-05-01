#!/usr/bin/env python3 



# Author: Joshua Musiyarira
# Version 0.21
# Date: 01/05/2022



import re
import pyperclip
import sys 
from time import sleep


class ASIG_BACKUPS:


    def clipboard_log(self):
        
        """
        Reads the content in the clipboard when the program is execuetd.
        Saves copied log information from clipboard to a variable called log information.
        """

        backup = pyperclip.paste()

        return backup


    def write_log(self):
        """
        Writes the entire asigra log backup as on the incident ticket to the asigra_backup.txt file.
        Reads the log information from the clipboard.
        """

        data = self.clipboard_log()

        with open("asigra_backup.txt", "w") as f:
            f.write(data)

    
    def write_errors(self):
        """
        Opens file containing Asigra backup logs, "asigra_backup.txt",  and returns a list of all errors within the log.
        Uses a regular expression match conditional on each line within the asigra backup log file. Error number range is 1 - 100.
        Formats errors log by appending a space every 10th element in the errors log list.txt
        Writes formatted error log to a file in current directory: "asigra_errors.txt"
        """

                # "asigra_backup.txt" contains log information from the performed backup. 
        with open('asigra_backup.txt', "r") as f:


            spaced_log = [line.rstrip() for line in f]
            backup_log = [line for line in spaced_log if line != ""]


            # empty list that is appended with errors found in the log
            errors = []

            for i, line in enumerate(backup_log):

                # regular expression 
                if re.match('^Errors:\s([1-9]|[1-9][0-9]|100)', line):  

                    # appending the next two errors, and the previous 6 errors for the associated backup 
                    errors.extend(backup_log[i-6:i+3]) 
                    errors.insert(i+4, "")

                    with open("asigra_errors.txt", "w") as e:

                        for line in errors: 
                            e.write(f"{line}\n")   


    def paste_clipboard(self):
        """
        Copies asigra errors from asigra_errors.txt file and pastes them to clipboard for user to then paste into work notes.
        """

        # reading the entire asigra_errors.txt file 
        asig_errors = open("asigra_errors.txt", "r").read() #

        # paste to clipboard
        pyperclip.copy(asig_errors)



def main():
    
    print(f"# You have 5 seconds to copy an asigra backup log from a ticket! \n")

    sleep(5)


    x = ASIG_BACKUPS()
    x.write_log()
    x.write_errors()
    x.paste_clipboard()

    print(f"# Graciously exiting: {sys.exit(1)}")
   


if __name__ == "__main__":
    main()
    