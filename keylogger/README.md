# Keylogger (for educational prposes only)

### Introduction
* A keystrke logger, aka, spyware, is surveillance software that monitors and logs keys struck on your keyboard.
* Performs surveilance behind-the-scences so that the end user is unaware of their key strokes being monitored.
* Used with malicious intent to steal unauthroised data; passwords, banking credentials, identity theft and more.
* Also used for the surveillance of minors as seen in a guardian:child relationship or when employers want to track employee activity at work.
* Functions when a user installs, usually without knowing, a malicious program masked to be of benefit to the user e.g. a game or production software. The application has malicous code that masks itself to the OS and then executes as a background process. 
* Certain sites can be infected and result in the installation of a keylogger as well.



### Assumptions 
* The assumption is that the keylogger has been installed on a victim machine with poorly or non-existent antivirus software.
* Keylogger tested in windows 7, windows 10 and kali linux machines operating systems only, but confident operates in macOs
* Assumed that user has [pynput](https://pynput.readthedocs.io/en/latest/) module on their machine or that attacker can install the module on the victim machine
* `pip3 install pynput `

### Implementation 
* Uses module [pynput](https://pynput.readthedocs.io/en/latest/) that allows monitoring of input devices 
* Pynput is OS AGNOSTIC. Interacts with the backend engine of macOs, linux and windows operating systems 

Keylogger version 0.0.1

[![Keylogger 0.0.1](https://i.ytimg.com/vi_webp/xNErVYfnJB4/maxresdefault.webp)](https://www.youtube.com/watch?v=xNErVYfnJB4)

* Process followed in above video 
1. Run keylogger0.0.1.py `python3 keylogger001.py`
2. User heads over to a login page
3. Enters in credentials
4. User input is output to the terminal 

### Versions
Keylogger: `keylogger001.py`
* A simple implementation that tracks keystrokes on a macOs, windows or linux machine that has a poorly configure antivirus software 
* Simply displays how a keylogger works 

Keylogger: `keyloger002.py`
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
* [Keylogger code tutroial](https://www.youtube.com/watch?v=XKoTwepEzPI)
