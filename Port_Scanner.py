import socket
import pyfiglet
from datetime import datetime

## Banner
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)
print("_"*70)

## Get info from user
hostname = input("Enter Domain or Hostname: ")
ip = socket.gethostbyname(hostname)
print("The IP Address is :", ip)
print("Scanning started at:" + str(datetime.now()))
print("_"*70)

## Start and end IP Address
port_range_start = int(input("Port Range (Start): "))
port_range_end = int(input("Port Range (End): "))
print()

## Port Scanner loop
for port in range(port_range_start, port_range_end + 1):
    print("scanning on {0}:{1}".format(ip, port))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((ip, port))
    if result == 0:
        print("port {0} is open ...".format(port))
    s.close()

