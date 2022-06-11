import os
import time

name='Main.ipynb' #Name of the file that is being downloaded
path="C:\\Users\\User\\Downloads" #Download folder path


def find(name, path): #this function retiurns True/False based on the existence of the file
    for root, dirs, files in os.walk(path):
        if name in files:
            return True
        else:
            return False

while True:
    x=find(name, path)
    print("code is checking for the file.")
    time.sleep(5)
    if(x):
        print("file found....\nshutting down")
        break
    else:
        continue
    
shutdown_time=30 #Number of seconds before shutdown and after download completes
os.system(f'shutdown /s /t {shutdown_time}')