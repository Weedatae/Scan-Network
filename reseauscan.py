# author : Wilson
import socket
import os
import re
import subprocess
import colorama
from colorama import Style, Fore
colorama.init()

print(Fore.RED + "Create by Wilson." + Style.RESET_ALL)
print(Fore.CYAN + '1 - Scan Network' + Style.RESET_ALL)
print(Fore.MAGENTA + 'Choice :' + Style.RESET_ALL)
hosts = []
choice = int(input())
ip = "192.168.0."
x = 0
if choice == 1:
	while x<=30:
		p = subprocess.Popen("ping " + ip + str(x) + ' -n 1' ,stdout=subprocess.PIPE, shell=True)
		out, error = p.communicate()
		out = str(out)
		find = re.search("Destination host unreachable",out)
		if find is None:
			hosts.append(ip+str(x))
			print("[*] Host Found")
		x = x +1
print('HOST :')
for host in hosts:
	try:
		name, a ,b = socket.gethostbyaddr(host)
	except:
		name = "Not found"
	print('| ' + host + " | " + name)