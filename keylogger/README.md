# Keylogger

### Introduction
* A keystrke logger, aka, spyware, is surveillance software that monitors and logs keys struck on your keyboard.
* Performs surveilance behind-the-scences so that the end user is unaware of their key strokes being monitored.
* Used with malicious intent to steal unauthroised data; passwords, banking credentials, identity theft and more.
* Also used for the surveillance of minors as seen in a guardian:child relationship or when employers want to track employee activity at work.
* Functions when a user installs, usually without knowing, a malicious program masked to be of benefit to the user e.g. a game or production software. The application has malicous code that masks itself to the OS and then executes as a background process. 
* Certain sites can be infected and result in the installation of a keylogger as well.



### Assumptions 
* The assumption is that the keylogger has been installed on a victim machine with poorly or non-existent antivirus software.
* The keylogger was tested in VirtualBox on a windows 7 machine  

### Implementation 
Version 0.0.1

* NOTE: embed a video of deploying the key logger 
* Process followed in above video 
1. User received an email from a "friend" telling them to check out a new game
2. Nothing happened so user goes about their day
3. User logins in to a fishing webiste, the beggining of the end
4. Keylogger, of which is running as a background process is stealthily capturing keystrokes 


### Versions
Python file: `keylogger001.py`
* A simple implementation that tracks keystrokes on a macOs, windows or linux machine that has a poorly configure antivirus software 
* Simply displays how a keylogger works 

Python file `keyloger002.py`
* More advnaced implementation
* Once active on a victim machine, log files are sent to the attacker's machine
* Attacker's machine has a server running on an open port 
* Receives the log files via DNS exfiltration 
* Requires attacker to have performed port enumeration so as to know which ports on the victim's machine allow for outbound traffic
* Assumption is that victim machine has a poorly configured firewall

### Sources
* [What is a keylogger?](https://www.mcafee.com/blogs/consumer/family-safety/what-is-a-keylogger/)
* [Converting a python file ".py" to an application ".exe"](https://www.simplifiedpython.net/convert-python-to-exe-tutorial/)
* [Installing Windows 7 in VirtualBox](https://www.buildsometech.com/install-windows-7-on-virtualbox-machine/)
