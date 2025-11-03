import psutil
from plyer import notification
import time

# Create our user input variable
frequency = int(input("Enter the frequency (in seconds) for system notifications: "))

while True:
    # Get system info about CPU and RAM percents
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
