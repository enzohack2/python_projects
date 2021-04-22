# Generating a SHA-256 checksum with python!

### Introduction
You may be wondering, what is a checksum? Or perhaps you're wondering, why would I bother hardcode a SHA-256 checksum generating script in python? Aren't there are applications that can automitcally handle hashing for me? Firstly, coding is fun. If that answer doesn't suffice, then learning new programming skills is a fantastic way to enhance your tech know-how. With the "why" out the way, let's tackle the "what". 

What is a checksum? A checksum is the result of running a cryptographic hashing function on a piece of data. Checksums are usually generated on application installer files, .exe file extension on windows, for the purpose of verfying the integrity of a download. Ensuring the downloaded file hasn't beeen corrupted during transmission by comparing the download source checksum and he checksum generated on the downloaded application installer file once it's on the host machine. There are various checksum generating algorithms and in today's case, we'll be work with the SHA-256 algorithm.

### Python Script explained
The interactive python script below functions by asking a user for two forms of input. Input no.1: The download source checksum, this is the chekcusm from the source page where they've downloaded their executable file. Input no.2: An **ABSOLUTE** filepath that directs the python script to where the downloaded installer file is on the host machine.

The script then makes use of python's built-in [hashlib](https://docs.python.org/3/library/hashlib.html) module by generating a sha256 hash object and updating it with bytes-like objects from the file given in the filepath by the user (Input no.2). We take advantage of python's context mamanger in order to acheive this process. The script then uses [exception handling]() and the [assert]() keyword to compare the download source checksum (Input no.1) and the genrated checksum. If the checksums don't match then an [AssertionError]() is raised and the user is informed. Otherwise, we have a match, the user can imply that the data within the application installer file is complete and can call it a day. Simples. 

Within the "Script in use" section, the file installed on the host machine for the purposes of generating a SHA-256 checksum and is the virtual box package, [a general-purpose full virtualizer for x86 hardware, targeted at server, desktop and embedded use.](https://www.virtualbox.org/wiki/VirtualBox) In other words, a virtual machine manager that allows you to run different guest operating systems on top of your existing host OS as a type 2 hypervisor. 

### Error free example usage

1. User downloads virtual box package (in this case it's saved on the desktop)

![image](https://user-images.githubusercontent.com/77082071/115679383-70c81400-a34a-11eb-977c-0983e3405b1f.png)

![image](https://user-images.githubusercontent.com/77082071/115680064-22ffdb80-a34b-11eb-847e-197741f29da5.png)

2. User copies download source SHA-256 checksum from virtual box SHA-256 checksum page 

![image](https://user-images.githubusercontent.com/77082071/115679433-7cb3d600-a34a-11eb-831b-7ab19acd44a8.png)


3. User runs the script in terminal `sha256gen.py` and enters required input.
* Script generates a checksum and then compares it to the source checksum 
* User is then informed if checksums match or don't. In this case they do and we can call it a day :D

![image](https://user-images.githubusercontent.com/77082071/115680104-2bf0ad00-a34b-11eb-9f71-e316b1a40873.png)

### Example output when an error occurs (incorrect source checksum)

![image](https://user-images.githubusercontent.com/77082071/115680130-327f2480-a34b-11eb-8f78-18005f038b68.png)

### Conclusion 
Voilà! We now have seen how checksums can be generated using python's hashlib module, context management and some simple programming logic. And again, the code is within this repository: "sha256gen.py". Feel free to improve upon the code as you wish and happy coding. 

### Useful links
1. Checksum explained on [HowToGeek.com](https://www.howtogeek.com/363735/what-is-a-checksum-and-why-should-you-care/)
