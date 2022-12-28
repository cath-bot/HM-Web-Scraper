import subprocess
import random
import json

def ip_creator(interface_id):
    position_1 = random.randint(0,255)
    position_2 = random.randint(0,255)

    ip = f'192.168.{position_1}.{position_2}'
    command = f'sudo ifconfig {interface_id} {ip} up'
    subprocess.call(command, shell = True)
    subprocess.call(
        'sudo /sbin/ifdown wlan0 && sleep 10 && sudo /sbin/ifup --force wlan0',
         shell=True)
    print(ip)

ip_creator('ens33')