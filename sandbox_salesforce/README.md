# Sandbox accounts

### Intrdouction - service desk workflow
1. As part of the starter flow, service desk agents are required to create sandbox accounts for property managers and customer service advisors
2. Sandbox takes a snapshot of the live salesforce application and is used for training purposes.
3. Service desk agents currently have to manually provision sandbox accounts; a time consuming and tedious process.

### Script `sandbox_create.py` worfklow
1. Trigger script: `python.exe sandbox_create.py`
2. Accepted input: full email address of user account to create in sandbox and user to clone from, with an existing sanbox account
3. Authenticate to sanbox
4. Verify a user account has not been created already within sanbox
5. Pull the data to be cloned from the original user in sanbox and store it in variables
6. Open the sandbox user creation page
7. Ammend all the data
8. Send a password reset link to the user

### Sources for learning
1. Simple salesforce API:
* https://www.mydatahack.com/salesforce-api-with-simple-salesforce-for-python/
* https://pydigger.com/pypi/simple-salesforce
* https://github.com/simple-salesforce/simple-salesforce
* https://stackoverflow.com/questions/25130278/python-simple-salesforce
  