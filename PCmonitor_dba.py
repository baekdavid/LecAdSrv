# Author: DavidBAEK
# Date: 08/09/2022
# System information to save in /tmp/test

import psutil
import platform
import sys


# K/M/GByte arrondi a 2 decimal
def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

print("CPU_count:", psutil.cpu_count(logical=False))
# CPU usage/Nbre, utilisation du CPU
print(f"CPU_usage: {psutil.cpu_percent()}%")
# Disk Information
svdisk= psutil.disk_usage('/')
print(f"Disk_Percentage: { svdisk.percent }%")

# Memory Information
# K/M/GByte arrondi a 2 decimal
svmem = psutil.virtual_memory()
print(f"Virtual_memory_Total: {svmem.total}")
print(f"Virtual_memory_Total: {get_size(svmem.total)}")
print(f"Virtual_memory_Used: {svmem.used}")
print(f"Virtual_memory_Used: {get_size(svmem.used)}")
print(f"Virtual_memory_Percentage: {svmem.percent}%")

# System information to save in /tmp/test
# patriceF
file_name = sys.argv[1]
d = dict()
with open(file_name, 'w') as f:
    for k, v in d.items():
        line = f"{k}:{v}\n"
        print(line, end="")
        f.write(line)

# original_stdout = sys.stdout # Save a reference to the original standard output
# file_path = 'computerstate.txt'
# sys.stdout = open(file_path, "w")
# sys.stdout = original_stdout
# print("--Successfully saved to computerstate.txt--")





