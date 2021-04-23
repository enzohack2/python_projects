#!/usr/bin/env python3

import platform, sys

print("[#] Retreiving available system information...")

sys_info = platform.system()
release_version = platform.version()
processor = platform.processor()
python_build = platform.python_build()

goodbye_message = "Ciao for now :D"

print(f"[#] System information found: \n\t OS: {sys_info}, \n\t Release version: {release_version}, \n\t Processor name: {processor}")  
print(f"[#] Python build (if applicable): {python_build}")
print(f"[#] Thanks for using this service: {goodbye_message}")

sys.exit(1)