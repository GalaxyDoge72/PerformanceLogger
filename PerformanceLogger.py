## Install psu tools if not already installed ##
import subprocess
import sys
package_name = "psutil"
try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
    print(f"Successfully installed {package_name}")
except subprocess.CalledProcessError:
    print(f"Failed to install {package_name}")

## Imports ##
import psutil
from datetime import datetime
import time

## Set file name ##
currentDateTime = datetime.now()
formattedDateTime = currentDateTime.strftime("%Y-%m-%d_%H-%M-%S")
fileName = f"PerformanceLog {formattedDateTime}.txt"

## Get system usage stats ##
def cpuUsage():
    return psutil.cpu_percent(0)

def memoryUsage():
    mem = psutil.virtual_memory()
    availableRAM = int(mem.available) / 1000000
    return availableRAM

## Log to a txt file ##
try:
    delay = int(input("How often should the samples be? (e.g 1 = one sample per second) "))
    print(f"Close the window to end the program. \n")
    while True:
        liveTime = datetime.now()
        formattedTime = liveTime.strftime("%H:%M:%S")
        with open(fileName, "a") as file:
            cpu = cpuUsage()
            memory = memoryUsage()
            file.write(f"{formattedTime} | CPU Usage: {cpu}% | Memory Usage: {memory} MB \n")
            print(f"Took sample at {formattedTime}.")
        time.sleep(delay)
except ValueError:
    print("That wasn't a number. Exiting.")
    time.sleep(3)
    sys.exit("Invalid delay")