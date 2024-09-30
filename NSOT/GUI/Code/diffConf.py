from napalm import get_network_driver
import os


def fetchDir(device, d_path):
    for filename in os.listdir(d_path):
        if device in filename:
            final_path = os.path.join(d_path, filename)
            if os.path.isfile(final_path):
                return(final_path)
    


def difConf(ip, usr, pwd):
    driver = get_network_driver('ios')

    device = driver(hostname=ip, username=usr, password=pwd)

    device.open()
    print("Connected successfully")

    sh_int = device.cli(['sh run | sec hostname'])
    out_host = sh_int['sh run | sec hostname'].split(" ")[1]


    current_dir = os.getcwd()
    destination_dir = os.path.join(current_dir, "Config")


    final = fetchDir(out_host, destination_dir)
    #if final:
       # with open(final,'r') as file:
            #cont = file.read()
    #print(cont)


    device.load_merge_candidate(filename=final)
    diff = device.compare_config
    diff_string = diff()

    device.close()
    print("Disconnected from the device")

    if diff_string:
        print(diff_string)
        return diff_string
    else:
        return "NA"




#if __name__ == "__main__":
    #runConf()