#!/usr/bin/env python3 

# author: Joshua Musiyarira
# Version 0.2
# Date: 28/04/2022

import re
from itertools import chain
from time import perf_counter
import sys 

class ASIG_BACKUPS:


    def errors_to_file(self):
        """
        Opens file containing Asigra backup logs, "asigra_backup.txt",  and returns a list of all errors within the log.
        Uses a regular expression match conditional on each line within the asigra backup log file. Error number range is 1 - 100.
        Formats errors log by appending a space every 10th element in the errors log list.txt
        Writes formatted error log to a file in current directory: "asigra_errors.txt"
        """

        # "asigra_backup.txt" contains log information from the performed backup. 
        with open('asigra_backup.txt', "r") as f:

            # removing new line character 
            stripped_text = [line.rstrip() for line in f]  

            # empty list that is appended with errors found in the log
            error_log = []

            for i, line in enumerate(stripped_text):

                # regular expression 
                if re.match('^Errors:\s([1-9]|[1-9][0-9]|100)', line):  

                    # appending the next two error_log, and the previous 6 error_log for the associated backup 
                    error_log.extend(stripped_text[i-6:i+3]) 
                    error_log.insert(i+4, "")
    
                    with open("asigra_errors.txt", "w") as e:

                        for i, line in enumerate(error_log): 
                            e.write(f"{line}\n")   



def main():
    start = perf_counter()

    x = ASIG_BACKUPS()
    x.errors_to_file()
    
    # script runtime
    runtime = perf_counter() - start

    print(f"Script runtim: {runtime}")



if __name__ == "__main__":
    main()
    