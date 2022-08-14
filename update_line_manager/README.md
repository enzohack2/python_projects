# Update line manager

### Introduction - Changes report process
1. Changes report ticket comes in from Kirsty Mcdonald with an excel sheet containing changes to be implemented
2. There is a sheet within the excel workbook dedicated to line manager changes
3. Service desk agent has to raise a reqest for all non-westminster based staff for a line manaager change
4. Once request ticket is generated,, service desk agent has to coomplete all the tasks for the line manager change
5. Once the line manager change process if complete in active directory ONLY, the service desk agent has to \n 
	assign the request ticket the status of "closed complete"
	>) Close the ticket, assuming the line manager change is the only request necessary 

### Script workflow
1. Save the excel sheet ion local downloads folder 
2. Run python script that reads sheet, formats input and triggers a powershell script to apply changes in AD
3. Powershell script the purges all folders stored locally.

### Notes
1. If implemented in powershell, then all service desk agents can use this script 
2. Otherwise, python intereter and required modules must be installed 
