# How to convert a python file, .py, into an executable file, .exe

### Introduction 
 This simple and brief tutorial covers how to convert a python application into an executable file. This process is OS agnotic (it will work on any operating system). The python script, `basicInfo.py` used in the example below simply retrives information about a host machine and displays it to the terminal. The code can also be found within this repository 
 
![pythonCode](https://user-images.githubusercontent.com/77082071/115926637-137fb000-a47b-11eb-91f5-f96192080bef.png)

Code in use:

![codeInUse](https://user-images.githubusercontent.com/77082071/115926733-3c07aa00-a47b-11eb-8f8c-8515b896aceb.png)

### Instructions 

* Install [pyinstaller]() with the [pip package maanger](): `pip install pyinstaller`

![installingPyInstaller](https://user-images.githubusercontent.com/77082071/115926439-c1d72580-a47a-11eb-858c-76ec9b33e59c.png)

* Open powershell or the command line in the same directory storing your python file 

![codeFileLocation](https://user-images.githubusercontent.com/77082071/115926806-5772b500-a47b-11eb-929e-189d63002faf.png)

![openingPowershell](https://user-images.githubusercontent.com/77082071/115926816-5b063c00-a47b-11eb-926b-940d477f19ca.png)

* Within the open terminal, and pyinstaller downloaded, enter `pyinstaller basicInfo.py` 
* Note: simply replace `basicInfo.py` with the name of your python file and don't ignore the .py file extension 
* Pyinstaller will then generate a new folder structure in the active structure 

![newFolders](https://user-images.githubusercontent.com/77082071/115927005-a9b3d600-a47b-11eb-8a20-9e5d0dacddea.png)

* There will now be an executable version of your python file: found in the `dist\<pythonFileName>` folder
* In this case the executable file was found in: `dist\basicInfo\basicInfo.exe`

![findingExecutableFile](https://user-images.githubusercontent.com/77082071/115927160-e4b60980-a47b-11eb-96e1-15114022fd8b.png)

* The file can now be run as an executable in visual studio code, in terminal as is shown below 

![runningExecutableVScode](https://user-images.githubusercontent.com/77082071/115927261-129b4e00-a47c-11eb-9887-4b004bf350ba.png)

![executableOutput](https://user-images.githubusercontent.com/77082071/115927280-17f89880-a47c-11eb-886f-c63f66f88791.png)

![executingFromTerminal1](https://user-images.githubusercontent.com/77082071/115927301-1cbd4c80-a47c-11eb-81d6-a7be3f21467d.png)

![executingFromTerminal2](https://user-images.githubusercontent.com/77082071/115927314-21820080-a47c-11eb-8585-f38505db39ae.png)
