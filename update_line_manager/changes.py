#!/usr/bin/env python3
# Author: Joshua Musiyarira
# Date: 09/06/22
# Version: 0.0.1
# When deployed remotely, agent needs to be connected to Global Protect VPN 


# modules
import pandas as pd 
from time import sleep
from pyperclip import copy
import os


# open "Line Manager" worksheet within "Changes Report.xlsx" workbook. Downloaded locally and purged later 
lm_sheet = pd.read_excel(r"C:\Users\Joshua.Musiyarira\Downloads\Changes Report.xlsx", sheet_name="Line Manager", skiprows=9, usecols=[3, 4, 5, 6])


class CHANGES_REPORT:
    """
    Initially created to complete the line manager change process, but will have additional tasks added to it, such as job title changes an name changes - fully automated. 
    """

    def __init__(self, dataframe):
        self.dataframe = dataframe 

    def uname_validation(self, fname, sname):
        """
        @fname=Firstname and @sname=Surname columns from "Changes report.xlsx" workbook, "Line Manager" sheet input.
        Name is formatted as <firstname.lastname> for querying in active directory by a powershell script
        """

        # user name formatted for active directory search. Schema: <firstname.lastname> 
        formatted_user_name = f"{fname}.{sname}"
        return formatted_user_name

    def lmanager_name_validation(self, prev_lm, new_lm):
        """
        @prev_lm=previous line manager and @new_lm = new line manager column from "Changes report.xlsx" sheet.
        Formats line manager names in schema <firstname.lastname> if @prev_lm and @new_lm are different
        """

        # slicing "(510210) Simon Smith", into "Simon.Smith". 
        prev_lm_sliced = prev_lm[9:]
        new_lm_sliced = new_lm[9:]

        name = [] # stores line managers name in format <firstname.lastname>

        # confirming previous and new line manager fiels are different 
        if prev_lm_sliced != new_lm_sliced:

            for letter in range(len(new_lm_sliced)):
                if new_lm_sliced[letter] == " ":
                    fname = new_lm_sliced[:letter]
                    sname = new_lm_sliced[letter+1:]
                    name.append(fname)
                    name.append(sname)

            # formatting new line manager name as <firstname.lastname>
            formatted_names = ".".join(name)
            return formatted_names

    def main(self):
        print(f"### Original Data Frame:\n {self.dataframe}")
        
        # applying employee name validation and line manager field validation functions for each row of data. \n
        # formatted data stored in new fields: "employeeName" and "newLineManager"
        self.dataframe["employeeName"] = self.dataframe.apply(lambda  row: self.uname_validation(row[0], row[1]), axis=1) 
        self.dataframe["newLineManager"] = self.dataframe.apply(lambda row: self.lmanager_name_validation(row[2], row[3]), axis=1)
        # deleting the original line manager column by index value
        self.dataframe = self.dataframe.drop(self.dataframe.columns[3], axis=1)
        # saving the ammended dataframe as a csv file
        self.dataframe.to_csv("applied-changes.csv", index=False)
        
        # opening powershell script as admin and launching script 
        print(f" ### ENTER ADMIN CREDENTIAL FOR RMG-JMU \n")
        # opens powershell as admin. Required for powershell commands to be executed. 
        os.system("powershell Start-Process powershell -Verb runAs") 

        launch_script_args = r"cd C:\Users\Joshua.Musiyarira\Documents\python\mini-projects\line_manager_change"
        copy(launch_script_args)
        print(f"### Press CTRL+V IN POWERSHELL ADMIN SHELL") # paste filepath for script to the executed in the terminal
        sleep(5) # explicit wait for above command
        execute_script = ".\lm_change.ps1"
        copy(execute_script) # copies script launch command to clipboard to be pasted into the terminal and launched 
        print(f"### Press CTRL+V IN POWERSHELL ADMIN SHELL") 
        sleep(5) # # explicit wait for above command to complete 


        # deleting changes report and applied changes spreadsheet 
        changes_report_fpath = r"C:\Users\Joshua.Musiyarira\Downloads\Changes Report.xlsx"
        applied_changes_fpath = r".\applied-changes.csv"
        if os.path.exists(f"{changes_report_fpath}") and os.path.exists(f"{applied_changes_fpath}"): 
            os.remove(f"{changes_report_fpath}")
            os.remove(f"{applied_changes_fpath}")
        else:
            print(f"The {changes_report_fpath} does not exist")
            print(f"The {applied_changes_fpath} does not exist")



if __name__ == "__main__":
    run = CHANGES_REPORT(lm_sheet)
    run.main()
