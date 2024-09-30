import subprocess

def check_ping(ip):
    try:
        pin = subprocess.check_output(['ping', '-c 2', ip], stderr=subprocess.STDOUT)
        output=pin.decode('utf-8')
        print(output)
        return(output)

    except subprocess.CalledProcessError as ex:
        # This will catch the CalledProcessError
        err_out = "Ping failed. Error output:", ex.output.decode('utf-8')
        print(err_out)
        return(err_out)

    except Exception as ex:
        # Handle any other exceptions 
        err_out = "An unexpected error occurred:", str(ex)
        print(err_out)
        return(err_out)
