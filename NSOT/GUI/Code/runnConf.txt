from napalm import get_network_driver
import os
from datetime import datetime


def saveConf(data, folder, filename):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    f_path = os.path.join(folder, filename)
    
    with open (f_path, 'w') as file:
        file.write(data)



def runConf(ip, usr, pwd):
    driver = get_network_driver('ios')

    device = driver(hostname=ip, username=usr, password=pwd)

    device.open()
    print("Connected successfully")

    sh_int = device.cli(['sh run', 'sh run | sec hostname'])
    out_conf= sh_int['sh run']
    out_host = sh_int['sh run | sec hostname'].split(" ")[1]

    timest = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    file_name = f"{out_host}_{timest}.txt"

    saveConf(out_conf, "Config", file_name)
    print(file_name +"created in Config directory")

    device.close()
    print("Disconnected from the device")

    return(file_name)

#if __name__ == "__main__":
    #runConf()