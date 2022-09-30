#!/usr/bin/env python3

import shutil
import psutil
import emails

def check_cpu_usage():
   usage = psutil.cpu_percent(1)
   return usage < 80 # return True

def check_disk_space(disk):
    du = shutil.disk_usage(disk)
    free = du.free/du.total*100
    return free > 20 # return True

def check_localhost():
   localhost = socket.gethostbyname("localhost")
   return localhost == "127.0.0.1" #return True

def check_memory():
    # 1MB is == 1024 * 1024
    available = psutil.virtual_memory().available/(1024*1024)
    return available_memory > 500 # return true


if not check_cpu_usage():
    Subject_line = "CPU usage is over 80%"
elif not check_disk_usage('/'):
    Subject_line = "Available disk space is less than 20%"
elif not check_memory():
    Subject_line = "Available memory is less than 500MB"
elif not check_localhost():
    Subject_line = "localhost cannot be resolved to 127.0.0.1"
else:
    pass

# send email if any error reported
if __name__ == "__main__":
    sender = "automation@example.com"
    receiver = "username@example.com"
    subject = "Error - {}".format(Subject_line)
    email_body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_error_report(sender, receiver, subject, email_body)
    emails.send_email(message)
