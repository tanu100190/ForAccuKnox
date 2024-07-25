import psutil
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.info(f'High CPU usage detected: {cpu_usage}%')
    return cpu_usage

def check_memory():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.info(f'High Memory usage detected: {memory_usage}%')
    return memory_usage

def check_disk():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        logging.info(f'High Disk usage detected: {disk_usage}%')
    return disk_usage

def check_processes():
    processes = [p.info for p in psutil.process_iter(attrs=['pid', 'name', 'username'])]
    logging.info(f'Running processes: {processes}')
    return processes

def main():
    print(f"CPU Usage: {check_cpu()}%")
    print(f"Memory Usage: {check_memory()}%")
    print(f"Disk Usage: {check_disk()}%")
    print(f"Processes: {check_processes()}")

if __name__ == '__main__':
    main()