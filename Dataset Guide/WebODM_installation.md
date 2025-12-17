
## Very scuffed WebODM installation guide 

This guide is for anyone to use. For Windows systems. It is not very detailed, but I hope it is of help. The old ones seemed to be out of date and were unusable for whatever reasons. This guide heavily uses official https://docs.opendronemap.org/installation/ as base and tries to update some basic things to be easier to find/understand. It has images as well, so I will be forgoing those myself. 

### Quick Start 

Following is a link to a paid version of the WebODM installer and support package in case you have the required 60e and are not tech savvy. https://opendronemap.org/webodm/download/#installer 

![image.png](attachment:image.png)

### Requirements 

Official Open Dronemap installation guide specifications have not been updated since 2020, but the listed minimum specs are 

    64bit CPU manufactured after 2010 
    20GB of disck space 
    4GB RAM 

While the recommended specs are 

    Latest Gen CPU 
    100GB disc space 
    16GB RAM 

To install Win 7 OS is required. 
Python, GitBash and Docker as well. 

https://www.docker.com/

### Virtualization 

For this project Docker is a more lightweight VM, on which WebODMlocalhost is based on. But first we need Docker working. 

First we need to check we can Docker can be used. Check your Task Master. This can be done by right clicking Windows Start button and choosing the seventh option from the bottom in your computer’s language. In English Task Master, in Finnish Tehtävienhallinta. 

![image.png](attachment:image.png)

Next in Task Master you will have opened in Processes window (Prosessit window in Finnish). Below that there is a tab called Performance (Suorituskyky in Finnish). Open that and see if virtualization is enabled.

![image-3.png](attachment:image-3.png)

If it is not enabled, you will have to look up your own computer model and how to enable virtualization for it specifically. You are unfortunately on your own on this part. 

When your computer has virtualization enabled we can continue. 

### Next 

Next step in the tutorials there is a "install Python section".
I needed WebODM running for a school project on ICT line so I am not going to run you through how to install Python.

### Memory and CPU Allocation  

#### EDIT: Docker automatically allocates the memory and CPU so we don't need to consider these things on Windows. Check the links to official tutorials for Apple and linux Docker CPU Memory allocation at the bottom of this section.

In the tutorial it is unclear if you need to know how to run Docker and how to work it. For all I understand this only affects performance and how Docker works I did end up using a whole lot of time with it, so I will just say to have Docker installed at this point. Just make sure that webodm file in docker Containers tab is running

![image-4.png](attachment:image-4.png)

Official tutorial was completely wrong on Memory and CPU allocation part. Older version allocated Memory and CPU using Docker. But newest version does not have that option. 

So This might actually be important part, but badly documented here. We need to change the WSL2 to manage CPU and memory limit. CPU cores need to be halved in use for the WebODM and logical processors need to be set to 60-70% of max in use. 

Next you need to install WSL2, a Linux subsystem on Linux. To do that you can simply open PowerShell in admin and type out: 

    wsl --install 

To make sure the installation was correct type 

    wsl --version 

2.6.0.0 version or newer is what I had of Ubuntu. 

    https://learn.microsoft.com/en-us/windows/wsl/install
has manual installers for WSL. 

WSL should be installed by now. 

There should be something called WSL settings? I dont know where I got that one. One of the Windows tutorials for WSL. This is where you can change CPU and memory limit though. 

What I do know is if you manage to find these two programs and open the WSL settings, and see the lil linux bird chilling underneat *Your Computer* you should be fine.

![{1126CE13-2959-44F5-8C37-D8085655595D}.png](attachment:{1126CE13-2959-44F5-8C37-D8085655595D}.png)

![image.png](attachment:image.png)

![image-2.png](attachment:image-2.png)



Anyway following some WSL tutorials that helped me find out what to do, even though I’ve already forgotten how I did it myself: 

    https://learn.microsoft.com/en-gb/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package 

    https://learn.microsoft.com/en-us/windows/wsl/wsl-config#configure-global-options-with-wslconfig 

### Git GUI 

Download Git. If you do not know how to run it, i dont know what to say. My mind is not able to handle this right now. 

Next we will use Git GUI to download the WebODM from GitHub in whole. 
So open *Git GUI* specifically. 

Browse target directories, for easy access, best to save it near the root of the drive.

![{3F9C9F68-E5C2-4869-93BE-629268C91245}.png](attachment:{3F9C9F68-E5C2-4869-93BE-629268C91245}.png)

To clone the repo successfully you need to make sure there is no already existing Folder with the same name.
Choose clone repository and clone this repo:

    https://github.com/OpenDroneMap/WebODM 

If cloning was successful, you should have the image(Docker calls their repo like things inside VMs images, just play along) given by original tutorial. Open repositories and Create DeskTop Icon for easy access. 

![{B7AF3398-510E-467D-A938-325679D8549F}.png](attachment:{B7AF3398-510E-467D-A938-325679D8549F}.png)

If you are unable to create a desktop icon like me, i will tell you how to get the program working anyway with gitBash.

### Launch WebODM 

To launch WebODM you need to have the Docker running before starting the program, or you can’t launch WebODM. This way is mandatory for the first time(and if you didnt get your desktop icon working earlier). 

![image.png](attachment:image.png)

After you have done that open Git Bash. Move to your WebODM folder. C:/WebODM or wherever it is. 

    cd C:/webodm 

Followed by 

    ./webodm.sh start & 

Make sure there is *$* in front of ./webodm.sh start & . For some reason the GitBash keps being funny with me.

This should start the program. To manually find the file, it is in webodm folder called webodm and labeled as Shell Script. As a Desktop Icon webdom.sh would automatically run all the commands it contains in gitbash, but this is how it will be done *manually* for every single time.

Now it will appear as if nothing happened, but by copying 

    127.0.0.1:8000 

Aka localhost:8000 and moving to it on your browser. You SHOULD be transferred to the WebODM “congrats you accessed WebODM welcome page”. If there is an error I do not know why or what it is. I propably forgot to document some stuff anyway. I am sorry.  

Anyway Tutorials you should cross reference if you are having issues with WebODM installation: 

    https://docs.opendronemap.org/installation/
    https://www.geoportti.fi/wp-content/uploads/2023/01/03-Geoportti-oGIIR-Manual-Install-WebODM-on-Windows-10-and-11-2022.pdf

Anyway, Hope this helped, and if it didnt, I am sorry, just ask me for help in class and we can go "oh no" together. Maybe we can get it all working with teamwork. Good luck. 