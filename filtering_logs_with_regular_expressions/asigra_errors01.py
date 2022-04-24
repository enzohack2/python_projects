#!/usr/bin/env python3 

# authhor: Joshua Musiyarira
# Version 0.1
# Date: 23/04/2022

import re
from itertools import chain
from time import perf_counter
import sys 



class ASIG_BACKUPS:


    def errors_to_file(self):
        """
        Opens file containing Asigra backup logs, "asigra_backup.txt",  and returns a list of all errors within the log.
        Uses a regular expression match conditional on each line within the asigra backup log file. Error number range is 1 - 100 
        Formats errors log by appending a space every 10th element in the errors log list.txt
        Writes formatted error log to a file in current directory: "asigra_errors.txt"
        """

        # "asigra_backup.txt" contains log information from the performed backup. 
        with open('asigra_backup.txt', "r") as f:

            # removing the \n newline character in "asigra_backup.txt" file
            lines0 = [line.rstrip() for line in f]  

            # empty list that is appended with errors found in the log
            lines = []

            for i, line in enumerate(lines0):

                # regular expression seerching for backups with errors ranging from 1 > 100 
                if re.match('^Errors:\s([1-9]|[1-9][0-9]|100)',line):  
                    lines.extend(lines0[i:i+9]) 
                  

        # script stops running if no errors are found
        
        if len(lines) == 0: 
            print("No errors found")
            print("Gracefully exiting")
            sys.exit(1)

        k = ''
        N = 9

        # itertools chain source: https://www.geeksforgeeks.org/python-itertools-chain/
        formatted_errors = list(chain(*[lines[i : i+N] + [k] 
                    if len(lines[i : i+N]) == N 
                    else lines[i : i+N] 
                    for i in range(0, len(lines), N)]))


        with open("asigra_errors.txt", "w") as e:

            for i, line in enumerate(formatted_errors): 
                e.write(f"{line}\n")   



def main():
    start = perf_counter()

    x = ASIG_BACKUPS()
    x.errors_to_file()
    
   
    runtime = perf_counter() - start
    print(f"Script runtime: {runtime}")



if __name__ == "__main__":
    main()
    
