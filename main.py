import os
import time

file_name='Main.ipynb' #Name of the file that is being downloaded
path="C:\\Users\\User\\Downloads" #Download folder path


def watch_file(file_name, path): #this function retiurns True/False based on the existence of the file
    for root, dirs, files in os.walk(path):
        if file_name in files:
            return True
        else:
            return False

while True:
    x=watch_file(file_name, path)
    print("Checking for the file: Not found")
    time.sleep(5)
    if(x):
        print("file found....\nshutting down")
        break
    else:
        continue
    
# SHUTDOWN CODE BLOCK 
shutdown_time=30 #Buffer time(seconds) between download completion and shutdown 
os.system(f'shutdown /s /t {shutdown_time}')


# SLEEP CODE BLOCK 
# uncomment the next two lines and comment out the previous two lines to send your pc to sleep mode instead of shutdown upon download completion
# os.system("POWERCFG /HIBERNATE OFF")
# os.system("RUNDLL32.EXE powrprof.dll,SetSuspendState 0,1,0")