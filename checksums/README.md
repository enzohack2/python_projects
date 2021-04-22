# Generating a SHA-256 checksum with python!

### Introduction
You may be wondering what is a checksum? Or perhaps you're wondering, why would I bother hardcode a SHA-256 checksum generating script in python? Aren't there are applications that can automitcally handle hashing for me? Firstly, coding is fun. If that answer doesn't suffice, then learning new programming skills is a fantastic way to enhance your tech know-how. With the "why" out the way, let's tackle the "what". 

What is a checksum? A checksum is the result of running a cryptographic hashing function on a piece of data. Checksums are usually generated on application installer files, .exe on windows for the purpose of verfying the integrity of a download. Ensuring the downloaded file hasn't beeen corrupted during transmission by comparing the download source checksum and he checksum generated on the downloaded application installer file. There are various checksum generating algorithms and in today's case, we'll be work with the SHA-256 algorithm.

### Python Script explained
The interactive python script below functions by asking a user for two forms of input. Input no.1: The download source checksum, this is the chekcusm from the source page where they've downloaded their executable file. Input no.2: An **ABSOLUTE** filepath that directs the python script to where the downloaded installer file is on the host machine.

The script then makes use of python's built-in [hashlib]() module by generating a sha256 hash object and updating it with bytes-like objects from the file given in the filepath by the user (Input no.2). We take advantage of python's context mamanger in order to acheive this process. The script then uses [exception handling]() and the [assert]() keyword to compare the download source checksum (Input no.1) and the genrated checksum. If the checksums don't match then an [AssertionError]() is raised and the user is informed. Otherwise, we have a match, the user can imply that the data within the application installer file is complete and can call it a day. Simples. 

Within the "Script in use" section, the file installed on the host machine for the purposes of generating a SHA-256 checksum and is the virtual box package, [a general-purpose full virtualizer for x86 hardware, targeted at server, desktop and embedded use.](https://www.virtualbox.org/wiki/VirtualBox) In other words, a virtual machine manager that allows you to run different guest operating systems on top of your existing host OS as a type 2 hypervisor. 

### Script in use

1. User downloads virtual box package (can be any form of executable)
2. User copies download source SHA-256 checksum
3. User launches program in terminal and enters given ipnut
4. Script generates a checksum and then compares it to the source checksum 
5. User is informed if checksums match or don't 

### Conclusion 
Voilà! We now have seen how checksums can be generated using python, the code is within this repository: "sha256Generator.py". Feel free to improve upon the code as you wish and happy coding. Some useful links below:

### Links
1. Checksum explained on [HowToGeek.com](https://www.howtogeek.com/363735/what-is-a-checksum-and-why-should-you-care/)
