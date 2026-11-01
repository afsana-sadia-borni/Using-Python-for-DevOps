import os
import datetime
def run_command(command):
    return os.system(command)
def show_date():
    return datetime.datetime.today()

#run_command("date")
#run_command("df -h")
today=show_date()
print(today)