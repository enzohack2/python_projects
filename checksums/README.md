# Generating a SHA-256 checksum with python!

### Introduction
You may be wondering what is a checksum? Or perhaps you're wondering, why would I bother hardcode a SHA-256 checksum hashing script in python when there are applications that can automitcally handle hashing for me? Firstly, coding s fun. If that answer doesn't suffice, learning new programming skils is a fantastic way to enhance you tech know-how. With the why out the way, let's tackle the "what". 

What is a checksum? A checksum is the result of running a cryptographic hash function on a piece of data in order to encrypt the data. Checksums are usually generated on application installer files, .exe on windows. They can be used to verify the integrity of a download by comparing a generated checksum off a file, with that of the download source checkusm. This is the process we see in the script below "sha256Generator". The executable file is the virtual box package. With virtual box being a: [general-purpose full virtualizer for x86 hardware, targeted at server, desktop and embedded use.](https://www.virtualbox.org/wiki/VirtualBox) In other words, a virtual machine manager that allows you to run different guest operating systems as a type 2 hypervisor. 

The code in the usage section below is interactive. It requires 2 forms of input from the user: a sha256 from the download source and a 

### Script Usage on a windows machine

1. User downloads virtual box package (can be any form of executable)
2. User copies download source SHA-256 checksum
3. User launches program in terminal and enters given ipnut
4. Script generates a checksum and then compares it to the source checksum 
5. User is informed if checksums match or don't 

### Conclusion 
Voilà! We now have seen how checksums can be generated using python, the code is within this repository: "sha256Generator.py". Feel free to improve upon the code as you wish and happy coding. Some useful links below:

### Links
1. Checksum explained on [HowToGeek.com](https://www.howtogeek.com/363735/what-is-a-checksum-and-why-should-you-care/)
