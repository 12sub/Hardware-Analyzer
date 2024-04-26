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
    subprocess.call(['python', 'procinfo.py', '-o', 'output.json', '-c', 'columns,data_usage,memory_usage,name,username,num_threads,s_nice,status', '-s', 'memory_usage', '-n', '15', '-u'], shell=True)
    print("==================")
def process_usage():
    print("Process Usage")
    print("="*50)
    subprocess.run(['python', 'nicusage.py'], shell=True)
    print("="*50)
    
def process_system():
    print("Process System")
    print("="*50)
    subprocess.run(['python', 'procsys.py'], shell=True)
    print("="*50)

def process_packet():
    print("Process Packet")
    print("="*50)
    subprocess.run(['python', 'nicproc.py'], shell=True)
    print("="*50)
    
print("Welcome to Process hacker" + "\n" +""+"*"*50 + "Please select an option")
print("1. Process Information\n")
print("2. Process Usage\n")
print("3. Process System\n")
print("4. Process Packet\n")

decide = input("Enter your choice: ")
if decide == "Process Information" or decide == "1":
    process_information()
elif decide == "Process Usage" or decide == "2":
    process_usage()
if decide == "Process System" or decide == "3":
    process_system()
if decide == "Process Packet" or decide == "4":
    process_packet()