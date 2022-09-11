import datetime
import pandas as pd
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

#Date and time
today = datetime.datetime.now()
date = today.strftime('%m/%d/%Y')
time = today.strftime('%H:%M:%S')
#CPU/HDD/RAM/
cpu_cnt = psutil.cpu_count()
cpu_pnt = psutil.cpu_percent()
svdisk= psutil.disk_usage('/')


# Memory Information
# K/M/GByte arrondi a 2 decimal
svmem = psutil.virtual_memory()

print(f"Virtual_memory_Percentage: {svmem.percent}%")
sysStatus = {
         "DATE": [date], "TIME": [time], "CPU_count": [cpu_cnt], "CPU_percent": [cpu_pnt],
            "HDD_usage": [svdisk.percent],"V-RAMtotal":[get_size(svmem.total)], "V-RAMused":[get_size(svmem.used)],
                "V-RAMpercent":[get_size(svmem.percent)]
            }

df = pd.DataFrame(sysStatus)
print(df)
df.to_csv('monitoring.csv', encoding='utf8', sep=';')
