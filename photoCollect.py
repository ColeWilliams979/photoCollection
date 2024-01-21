# This code will collect photos and download them
import os
import paramiko


server = input("What is the IP of the pi: ")
username = input("What is the username of the pi: ")
password = input("What is the password: ")

photo_command = "libcamera-still -t 1 -o test{iteration}.jpg"
download_command = "scp "+username+"@"+server+":/home/xacademy/test.jpg /Users/X\" \"Academy/photos"


ssh = paramiko.SSHClient()
ssh.connect(server, username=username, password=password)


for i in range(10):
    
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(photo_command.format(iteration=i))
    os.system(downlaod_command)
    











