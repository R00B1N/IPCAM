#!/usr/bin/python
from urllib.request import urlopen
import os
from colorama import Fore, init
from data import *
import socket
import time
import subprocess
init()

print(Fore.MAGENTA)

banner = """
 ___   _______  _______  _______  __   __ 
|   | |       ||       ||   _   ||  |_|  |
|   | |    _  ||       ||  |_|  ||       |
|   | |   |_| ||       ||       ||       |
|   | |    ___||      _||       ||       |
|   | |   |    |     |_ |   _   || ||_|| |
|___| |___|    |_______||__| |__||_|   |_|
"""

def switch():
	os.system('cls')
	print(banner)
	print(Fore.RED)
	print("Created By Blackster")
	time.sleep(1)
	print(Fore.CYAN)
	print("\nThis tool was Created for purposes only")
	pc_name = socket.gethostname()
	ip = socket.gethostbyname(pc_name)
	#print("\nEl nombre del equipo es: "+ pc_name)
	print("The ip of this equipment: "+ ip)
	print("\nUse VPN for still safe and evitate tracking.")
	time.sleep(1)
	menu = """
0-Random Cameras.      4-Italia.
1-Colombia.            5-Francia.
2-Estados Unidos.      6-China.
3-Brazil               
	"""
	print(Fore.GREEN)
	print(menu)

while True:
		switch()
		ask = int(input("Choose an option >> "))
		if ask==0:
			print("\nCharging...")
			print("\n")
			time.sleep(2)
			aleat()
			print("Press any key...")
			input()

		elif ask==1:
			print("\nCharging....")
			print("\n")
			time.sleep(2)
			colombia()
			print("Press any key...")
			input()
			
			os.system('cls')


		elif ask==2:
			print("\nCharging...,")
			time.sleep(2)
			print("\n")
			usa()
			print("Press any key...")
			input()
			os.system('cls')


		elif ask==3:
			print("\nCharging...")
			time.sleep(2)
			print("\n")
			brasil()
			print("Press any key...")
			input()
			os.system('cls')


		elif ask==4:
			print("Charging...")
			time.sleep(2)
			
			print("Press any key...")
			input()
			os.system('cls')

		elif ask==5:
			print("Charging...")
			time.sleep(2)
			
			print("Press any key...")
			input()
			os.system('cls')

		elif ask==6:
			print("Charging...")
			time.sleep(2)
			
			print("Press any key...")
			input()
			os.system('cls')