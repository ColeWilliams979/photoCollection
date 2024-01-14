# This code will collect photos and download them
import os

IP = input("What is the IP of the pi: ")
password = input("What is the password: ")

os.system("ssh xacademy@" + IP)

os.system(password)


