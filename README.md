Python Backup to AWS S3:

How it works: backup.py packs the folder into a dated .tar.gz file, then s3_backup.py uploads that file to S3 with boto3.
Files: a table saying what each file does.
Requirements: Python 3, boto3, and running aws configure first.
Usage: which commands to run, and which variables to set in s3_backup.py.


backup.py diye project folder er sob file ek sathe .tar.gz archive kore backups/ folder e rakha hoy, file er naam e date thake.
s3_backup.py diye (Python + boto3) oi backup file ta AWS S3 bucket e upload kora hoy. Age aws configure diye credentials set korte hobe.
Er sathe utils.py ar fun_utils.py e system monitoring (disk, uptime, RAM) ar shell command chalanor helper function ache.




