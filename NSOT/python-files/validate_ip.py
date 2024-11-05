import ipaddress
import re


def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        doubleCheck(ip)
        return True
    except ValueError:
        return False


def doubleCheck(ip):
    mat = re.match(
        r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", ip
    )
    if not bool(mat):
        print(f"Double checked, IP address {ip} is not valid\n")
        return False

    ip_split = ip.split(".")
    for sp in ip_split:
        if int(sp) < 0 or int(sp) > 255:
            print(
                f"Double checked. In {ip}, one or more octets go out of possible range, not valid\n"
            )
            return False

    print(f"Performed all possible checks and {ip} is valid\n")
    return True
