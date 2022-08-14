# Powershell script that iteratively changes the line manager property of an employee in active directory based on the "Changes Report" process
# Date: 09/06/22
# Version: 0.0.1
# Author: Joshua Musiyarira

# importing line manager changes csv
$Users = Import-CSV -Path ".\applied-changes.csv"

# outputting table to the terminal 
$Users | Format-Table 

# iterating over each row in applied changes spreadsheet 
ForEach ( $User in $Users) {

    # employee in active directory from the imported spreadsheet 
    $employee  = $User.employeeName 

    # liine manager from ad spreadsheet  
    $lineManager = $User.newLineManager

    try {
        # setting the line manager property for the searched employee to be the name of the $lineManager from the imported excel sheet
        Set-ADUser $employee -Manager $lineManager
    }
    catch {
        Write-Output "Identity in AD not found"
        # accessing exception information 
        Write-Output $_
    }   
}

