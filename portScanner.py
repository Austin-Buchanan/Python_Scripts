# Script that scans network ports and prints results to the console

import socket
import platform
import os 

def main():
    # get the host IP address
    hostname = socket.gethostname()
    hostIP = socket.gethostbyname(hostname)
    print(hostname)
    print(hostIP)

    # scan ports
    for port in range(65535):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind((hostIP, port))
        except:
            print('Open port: ' + str(port))
            # check port information depending on OS type
            if platform.system() == 'Windows':
                netstat = os.popen('netstat -aon | findstr ' + str(port)).read()
                print(netstat)
                netstatSplit = netstat.split(' ')
                # iterate through netstatSplit, removing  empty strings and spaces
                while '' in netstatSplit:               
                    for element in netstatSplit:
                        if element == '':
                            netstatSplit.remove(element)
                # check which app is using the port by looking up the PID found through netstat
                if len(netstatSplit) >= 1:
                    tasklookup = os.popen('tasklist | findstr ' + netstatSplit[4].strip('\n')).read()
                    print(tasklookup)
        sock.close()

    input('Press any key to continue...')

if __name__ == "__main__":
    main()