from napalm import get_network_driver
from threading import Thread


def push(ip, usr, pwd, PID, AID, loop, dvc, cost):
    driver = get_network_driver('ios')

    device = driver(hostname=ip, username=usr, password=pwd)
    device.open()
    print("Connected successfully")

    if dvc == "R1":
        ospf_config = [
            f"router ospf {PID}",
            "network 198.51.101.0 0.0.0.255 area 1",  
            f"network {loop} 0.0.0.0 area 1" 
        ]
    elif dvc =="R2":
        ospf_config = [
            f"router ospf {PID}",
            "network 198.51.101.0 0.0.0.255 area 1", 
            f"network 172.16.1.0 0.0.0.255 area {AID}", 
            f"network {loop} 0.0.0.0 area {AID}",
            "interface Fast0/0",
            f"ip ospf cost {cost}",
        ]
    
    elif dvc =="R3":
        ospf_config = [
            f"router ospf {PID}",
            f"network 172.16.1.0 0.0.0.255 area {AID}", 
            f"network {loop} 0.0.0.0 area {AID}"
        ]

    elif dvc =="R4":
        ospf_config = [
            f"router ospf {PID}",
            "network 198.51.101.0 0.0.0.255 area 1", 
            f"network 172.16.1.0 0.0.0.255 area {AID}", 
            f"network {loop} 0.0.0.0 area {AID}",
            "interface Fast0/0",
            f"ip ospf cost {cost}"
        ]

    ospf_config_str = '\n'.join(ospf_config)
    print(ospf_config_str)
    device.load_merge_candidate(config=ospf_config_str) 
    diff_str = device.compare_config()
    #print(diff_str)
    device.commit_config()
    device.close()
    print("Disconnected from the device")
    return(diff_str)



def thrdTask(ip, usr, pwd, PID, AID, loop, dvc, cost):   
    threads = []
    thread = Thread(target=push, args=(ip, usr, pwd, PID, AID, loop, dvc, cost))
    thread.start()
    threads.append(thread)

    # Waiting for all threads to complete
    for thread in threads:
        thread.join()


#if __name__ == "__main__":
#    main("198.51.100.1", "ash", "r1win", 1, 1)
