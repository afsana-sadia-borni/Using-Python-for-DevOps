import os
import datetime
import shutil
def backup_files(source,destination):
    today=datetime.date.today()
    backup_file_name=os.path.join(destination,f"backup_{today}.tar.gz")
    shutil.make_archive(backup_file_name.replace('.tar.gz',''),'gztar',source)
source="/Users/apple/Documents/cpu"
destination="/Users/apple/Documents/cpu/backups"
backup_files(source,destination)