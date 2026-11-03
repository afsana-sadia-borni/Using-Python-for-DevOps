# Python Backup to AWS S3

A small Python for DevOps practice project. It backs up a project folder into a compressed archive and uploads that archive to an AWS S3 bucket.

## How it works

1. **Create a backup:** `backup.py` compresses every file in the project folder into a `.tar.gz` archive and saves it in the `backups/` folder. The archive name includes the date, for example `backup_2026-10-31.tar.gz`.
2. **Upload to S3:** `s3_backup.py` uses `boto3` (the AWS SDK for Python) to upload the backup archive to an S3 bucket.

## Files

| File | Description |
|---|---|
| `backup.py` | Creates a dated `.tar.gz` backup of the project folder with `shutil.make_archive`. |
| `s3_backup.py` | Lists S3 buckets, creates a bucket and uploads the backup file to S3 with `boto3`. |
| `utils.py` | Prints system information: disk usage (`df -h`), uptime and load average, and total RAM (`sysctl hw.memsize`, macOS). |
| `fun_utils.py` | Helper functions to run shell commands and get the current date. |
| `backups/` | Where the backup archives are stored. |

## Requirements

- Python 3
- `boto3`: `pip install boto3`
- AWS CLI with your credentials set up: `aws configure`

## Usage

```bash
# 1. Create the backup archive
python backup.py

# 2. Upload the archive to S3
python s3_backup.py
```

Before you run `s3_backup.py`, set `bucket_name`, `region`, `file_name` (the path to the backup archive) and `key` (the object name in S3) at the bottom of the script.
