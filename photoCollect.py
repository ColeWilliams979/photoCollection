# This code will collect photos and download them
import os
import paramiko


server = "10.1.10.147"
username = "xacademy"
password = "Gauss5050"

photo_command = "libcamera-still -t 1 -o test{iteration}.jpg"
download_command = "scp {username}@{server}:/home/xacademy/test{iteration}.jpg /Users/X\" \"Academy/photos"


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(server, username=username, password=password)


for i in range(10):
    
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(photo_command.format(iteration=i))
    os.system(download_command.format(username=username, server=server, iteration=i))














