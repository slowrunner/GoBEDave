# FIRST GoPiGo3 (Python) Program Using Native VS Code

This is an exploration of code development for the GoPiGo3 robot  
using Visual Studio Code running native on the Raspberry Pi 3B+  
of the GoPiGo3 robot.

The main components of an IDE:   
- Explorer: allows visual folder navigation and creation 
- Editor: provide context sensitive help to create and maintain code
- Compiler/linker: build all the parts of an application
- Debugger: allow inspection and control of a running application
- Terminal shell: allows interacting with the operating system without leaving the IDE
- Extension marketplace: find and manage capability extensions for the IDE
- Version control extension: team specific codebase managment with history and access control
- Remote development extension: Allows cross platform compilation with remote execution and debug

(For most Python applications, the compiler/linker component is not usually needed.)  

VSCode is one of the most popular Integrated Development Environments  
in use today, and can require significant processor and memory resources  
depending on how much of the IDE features are used.

Using VSCode for developing Python code to run on the GoPiGo3's Raspberry Pi 3B or 3B+ processor  
is possible in two forms:
- native: Everything runs on the robot's Raspberry Pi processor
- remote: The VSCode IDE runs on a laptop or desktop computer,  communicating and controlling  
  the remote robot's code and execution.

Remote Development with VSCode is ideal but is more complicated to install and configure,  
while Native development with VSCode is simple to install and configure,  
but will not be as quick to respond and may not leave sufficient processor and memory  
resources for development of complex GoPiGo3 programs.  

This is an exploration of installing and running VSCode native on the GoPiGo3 Raspberry Pi 3B+  
with the Legacy Pi OS.  

Legacy Pi OS or GoPiGo3 OS are the operating system environments currently supported by Modular Robotics.

Note: Official support for the GoPiGo3 robot is at support@modrobotics.com  
and a user forum is avaliable at forum.dexterindustries.com 

This exploration assumes the following have been previously performed:
- Legacy Pi OS installed on SDcard
- WiFi networking configured and working
- Remote desktop access to the robot's Raspberry Pi desktop working
  1920x1080 resolution configured and available to remote desktop viewer
- GoPiGo3 software installed (both GoPiGo3 and DI Sensors) and tested working

# Installation: Native VSCode for Python3 development on the GoPiGo3

Log into the GoPiGo3 robot's desktop via VNC/Remote Desktop.

Open a terminal/command shell interface

```
free -m
        total        used        free        shared  buff/cache    available
Mem:      871         182         392            19         297          612

Note: the "available memory":  approx. 612 MB on my robot after boot up
```

Now lets install VS Code:

```
sudo apt update
sudo apt install code -y
```

When that completes type:
```
code
```
or using the mouse:
* Desktop->Raspberry Icon->Programming->Visual Studio Code


Get Started opens automatically:
1) Choose a look.  I chose "Light"
2) Close the Get Started panel  
  Note: If want to start over:  MenuBar:Help->Get Started

Installing a Python language extension:
1) Click the bottom icon on "Sidebar" (left side) - Extensions
2) Type Python in the search bar
3) Select first option "Python"
   - Click Install - go do laundry or eat lunch


This completes the minimum install to develop Python code for the GoPiGo3



# First GoPiGo3 Program


