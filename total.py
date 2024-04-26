import subprocess
import sys
import os 
import time
import nicproc
import nicusage
import procinfo
import procsys
import pyfiglet

process_Hacker = pyfiglet.figlet_format("Process Hacker")
print(process_Hacker)

def process_information():
    print("Process Information")
    print("==================")
    subprocess.call(['python', 'procinfo.py', '-o', 'output.json', '-c' 'columns,data_usage,memory_usage,name,username,num_threads', '-s', 'memory_usage', '-n', '15', '-u'], shell=True)
    print("==================")
def process_usage():
    print("Process Usage")
    print("="*50)
    subprocess.call(['python', 'nicusage.py'], shell=True)
    print("="*50)
    
def process_system():
    print("Process System")
    print("="*50)
    subprocess.call(['python', 'procsys.py'], shell=True)
    print("="*50)

def process_packet():
    print("Process Packet")
    print("="*50)
    subprocess.call(['python', 'nicproc.py'], shell=True)
    print("="*50)