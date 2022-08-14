# EPOD
Repository containing scripts used to streamline EPOD tasks completed by service desk agents within Residential Management Groups IT department. 

# PASSWRORD RESET TASK

The process of reseting a user's password is simple.
A service desk agent needs to authenticate to their EPOD administrator account, locate the user who is requesting that
their password be reset and then reset their password.

The current password policy for and EPOD user account, requires 8 characters of alphanumeric text with at least 1 upper-case letter and 
1 special character.

Once reset, a service desk agent needs to inform the user that their password has been reset, leaving a worknote of the actoin they have just performed.

The `password-reset.py` script leverages the selenium package to perform the above-mentioned actions in a headless environment.

Reference `requirements.txt` for further information on dependencies.

### Example use-case (with my dummy EPOD account: "joshua musiyarira")
1. A service desk agent triggers the EPOD script in the terminal, enters the EPOD admin password during runtime and the full email address of the user who has requested a password reset.
2. The script launches a headless chrome browser, authenticates to EPOD with admin credentials.
3. The script proceeds to locate the user in question, and reset their password by performing actions within EPOD.
4. Once reset, the script pastes a worknote an resolution note to the clipboard of the device that launched the script.
5. The service desk agent actioning the script needs to confirm that they have pasted both worknotes and reslution notes to the terminal.
6. The script authenticates to the account of the user who has had their EPOD password reset and saves a screenshot to the Downloads folder of the account that has launched the script.
7. The service desk agent has the choice of appending that image to the ticket as proof that the EPOD password works.

![command_line_workflow](https://user-images.githubusercontent.com/77082071/179038647-c5298eef-0350-4ce1-a1d4-631129f49338.png)

![image](https://user-images.githubusercontent.com/77082071/179039038-4014263a-2042-4ba6-af41-b357668ff974.png)

![image](https://user-images.githubusercontent.com/77082071/179039227-58fc5b23-48a2-452c-93e8-ab77acab2783.png)

* Assuming a user enters the wrong EPOD Admin password or incorrectemail address for a user in EPOD, the script advises the service desk agent on some troubleshooting steps.
* In the below example, I've input an incorrect admin password and an email address that is not found within the EPOD user pool database. 

![image](https://user-images.githubusercontent.com/77082071/179064098-fcc06795-6e47-419f-9701-2567bdec3d5a.png).




