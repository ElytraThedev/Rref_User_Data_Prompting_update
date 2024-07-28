import os
import sys
import platform
import psutil
import socket
import locale
import getpass
import datetime
import threading
import shutil

def get_detailed_user_info():
    color_codes = [31, 32, 33, 34, 35, 36, 37]  # ANSI color codes for red, green, yellow, blue, magenta, cyan, white
    color_index = 0

    def next_color():
        nonlocal color_index
        color = color_codes[color_index]
        color_index = (color_index + 1) % len(color_codes)
        return color

    info_lines = []
    def add_info(label, info):
        info_lines.append(f"{label}: {info}\n")
    
    add_info("Username", getpass.getuser())
    add_info("System Name", platform.system())
    add_info("System Version", platform.version())
    add_info("Machine Type", platform.machine())
    add_info("Processor Information", platform.processor())
    add_info("CPU Count", os.cpu_count())
    add_info("Boot Time", datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))
    add_info("Disk Usage", shutil.disk_usage("/"))
    add_info("Memory Info", psutil.virtual_memory())
    add_info("Swap Memory Info", psutil.swap_memory())
    add_info("Network Interfaces", psutil.net_if_addrs())
    add_info("Network Connections", psutil.net_connections())
    add_info("Running Processes", [proc.info for proc in psutil.process_iter(['pid', 'name'])])
    add_info("Logged In Users", psutil.users())
    add_info("Hostname", socket.gethostname())
    add_info("IP Address", socket.gethostbyname(socket.gethostname()))
    add_info("Locale Information", locale.getdefaultlocale())
    add_info("Environment Variables", os.environ)
    add_info("Python Version", sys.version)
    add_info("Python Executable Path", sys.executable)
    add_info("Platform Node", platform.node())
    add_info("Python Build Information", platform.python_build())
    add_info("Python Compiler Information", platform.python_compiler())
    add_info("Current Working Directory", os.getcwd())
    add_info("Home Directory", os.path.expanduser("~"))
    add_info("Shell", os.environ.get("SHELL"))
    add_info("System Architecture", platform.architecture())
    add_info("Python Path", sys.path)
    add_info("Current Time", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    add_info("CPU Times", psutil.cpu_times())
    add_info("Virtual Memory", psutil.virtual_memory())
    add_info("Swap Memory", psutil.swap_memory())
    add_info("Disk Partitions", psutil.disk_partitions())
    add_info("Disk IO Counters", psutil.disk_io_counters())
    add_info("Network IO Counters", psutil.net_io_counters())
    add_info("Network Stats", psutil.net_if_stats())
    add_info("Battery Status", psutil.sensors_battery())
    add_info("Number of Active Threads", threading.active_count())
    add_info("Thread Names", [t.name for t in threading.enumerate()])
    add_info("Current Python Module", __name__)
    add_info("Parent Process ID", os.getppid())
    add_info("Process ID", os.getpid())
    add_info("Uptime", datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time()))
    add_info("Current Working Directory Contents", os.listdir(os.getcwd()))
    add_info("Home Directory Contents", os.listdir(os.path.expanduser("~")))
    add_info("Is Windows", os.name == 'nt')
    add_info("Is Unix-like", os.name == 'posix')
    add_info("Is MacOS", sys.platform == 'darwin')
    add_info("System Platform", sys.platform)
    add_info("File System Encoding", sys.getfilesystemencoding())
    add_info("Default Locale", locale.getdefaultlocale())
    add_info("Preferred Encoding", locale.getpreferredencoding())
    add_info("CPU Frequency", psutil.cpu_freq())
    add_info("Physical CPU Count", psutil.cpu_count(logical=False))
    add_info("Logical CPU Count", psutil.cpu_count(logical=True))
    add_info("CPU Stats", psutil.cpu_stats())
    add_info("CPU Percent Usage", psutil.cpu_percent())
    add_info("System Load Average (Windows)", "N/A")  # Not available on Windows
    add_info("Python Executable", sys.executable)
    add_info("Python Implementation", platform.python_implementation())
    add_info("Python Version Info", sys.version_info)
    add_info("Current Python File", __file__)
    add_info("Process Environment Variables", os.environ)
    add_info("Process Priority", psutil.Process().nice())
    add_info("Process Status", psutil.Process().status())
    add_info("Process Memory Info", psutil.Process().memory_info())
    add_info("Process Open Files", psutil.Process().open_files())
    add_info("Process Connections", psutil.Process().connections())
    add_info("Process Threads", psutil.Process().threads())
    add_info("Process CPU Times", psutil.Process().cpu_times())
    add_info("Process CPU Affinity", psutil.Process().cpu_affinity())
    add_info("Process IO Counters", psutil.Process().io_counters())
    add_info("Process Creation Time", datetime.datetime.fromtimestamp(psutil.Process().create_time()).strftime("%Y-%m-%d %H:%M:%S"))
    add_info("Process Memory Percent", psutil.Process().memory_percent())
    add_info("Process Name", psutil.Process().name())
    add_info("Process Executable", psutil.Process().exe())
    add_info("Process Command Line", psutil.Process().cmdline())
    add_info("Process PID", psutil.Process().pid)
    add_info("Process Parent PID", psutil.Process().ppid())
    add_info("Process Username", psutil.Process().username())
    add_info("Process Children", psutil.Process().children())
    add_info("Process Suspend", "Supported (psutil.Process().suspend())")
    add_info("Process Resume", "Supported (psutil.Process().resume())")
    add_info("Process Kill", "Supported (psutil.Process().kill())")
    add_info("Process Wait", "Supported (psutil.Process().wait())")
    add_info("Process Is Running", psutil.Process().is_running())
    add_info("Process Is Stopped", psutil.Process().status() == psutil.STATUS_STOPPED)
    add_info("Process Termination Status", "Supported (psutil.Process().terminate())")
    add_info("Process Wait Timeout", "Supported (psutil.Process().wait(timeout=3))")
    add_info("Process Terminate", "Supported (psutil.Process().terminate())")
    add_info("Process Suspend", "Supported (psutil.Process().suspend())")

    return info_lines

# Get the detailed user information
user_info = get_detailed_user_info()

# Specify the name of the text file
filename = "detailed_user_info.txt"

# Open the file in write mode and write the collected information to it
with open(filename, "w") as file:
    file.writelines(user_info)

print(f"Detailed user information written to {filename}")
