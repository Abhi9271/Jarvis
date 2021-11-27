# Jarvis
A desktop voice assistant built using Python3.  
I have assumed a working knowledge of Python on VScode for anyone using this project.


## Setup
  1. **Using the Git Command Line:**  
     Copy the repository link from the profile and use the command (without the quotes) -> "git clone [copied link]"  
     OR  
     **Download Zip file and extract**  
       
     **(For this Project I'm using a Python virtual environment so that the base Python installation on the user's system remains unaffected)**
  3. **Go inside the Jarvis or Jarvis-main directory and open a powershell window**  
     Press Shift + Right Click -> Open Powershell Window Here
  4. **Type the following command in the powershell window -> "pip install virtualenv"**  
  5. **Now type "virtualenv [env_name]"**
  6. **Once the virtual environment has been created, activate it using ".\env_name\Scripts\activate"**
  7. **The powershell prompt will now change to something like this: (env_name)**
  8. **Now install all the dependencies for Jarvis using "pip install -r .\requirements.txt"**  
     This will install all dependencies except pyaudio.  
     Note: Do not download the latest version of pyaudio as it will not work!
  9. **Installing Pyaudio:**  
     1. Check your python version by typing 'python' in powershell
     2. Also check whether your system is using a 32-bit version of python or 64-bit
     3. According to the python version, download the correct version from pyaudio from here:
        https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
     4. Paste the downloaded file into the Jarvis-main folder and type the following command:  
        "pip install [package_name].whl"
     5. After the appropriate version of Pyaudio is installed, the voice assistant is good to go!!
     

    
