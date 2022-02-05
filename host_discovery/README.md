# Host Discovery
Within the context of this project, the purpose of host discovery is to locate other hosts' ip addresses on the network and discover what operating system they're runing on.
Although threading can be implemented to increase the processing speed of the script, running nmap as a stand-alone application would achieve greater effecieny. 
***DO NOT ATTEMPT HOST DISCOVERY OR OS DETECTION ON A NETWORK THAT YOU DO NOT OWN. ZimCanIT ACCEPTS NO LIABILITY FOR ANY DAMAGES CAUSED. THIS IS PURELY FOR EDUCATIONAL PURPOSES.***

### Workflow
1. Setup a virtual network using VirtualBox with 3 or more guest VMs, virtual machines
* Refer to this video guide on the installation of a [NAT network in VirtualBox](https://www.youtube.com/watch?v=rjlTz6KHS4U&t=5s)
* Refer to this guide on the [installation of kali linux in virtual box](https://github.com/ZimCanIT/Kali-linux/tree/main/reconfiguring%20kali) as well as the post-installation configuration steps required.
2. Create a python3 script that incorporates the "nmap" module in order to ectract methods for host discovery and os version detection 
3. Launch the script and ensure that all information created is stored in a `hosts_discovered.txt` file
4. Exfilitrate the `hosts_discovered.txt` file stored on a machine on a separate network owned by the attacker. Either via DNS exfiltration or email (less effective)

### Project setup (assuming you're using Ubuntu 
1. Update repositories with latest upstream package updates: `sudo apt-get update`
2. Install mousepad text editor: `sudo apt install mousepad -y`
3. Install pip for python3.x: `sudo apt install python3-pip -y`
4. Install python-nmap: `sudo python3-pip install nmap -y`
* Note: if you wish to run nmap as a standalone application enter: `sudo apt install nmap -y`

### Network topology

### Demonstration 
