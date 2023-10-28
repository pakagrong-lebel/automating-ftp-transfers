# Python script to automate FTP file transfers
from ftplib import FTP
def ftp_file_transfer(host, username, password, local_file_path, remote_file_path):
    with FTP(host) as ftp:
        ftp.login(user=username, passwd=password)
        with open(local_file_path, 'rb') as f:
            ftp.storbinary(f'STOR {remote_file_path}', f)



        



