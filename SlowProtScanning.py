#!/usr/bin/env python
import socket
import subprocess
import sys
import time
import random
from datetime import datetime

class SlowScan(object):
    
    @classmethod
    def slowScanning(self,ip):
        # Clear the screen
        #subprocess.call('clear', shell=True)

        #Input number of seconds are waiting between each group of porters
        secondForWait = input("Enter a number of seconds are waiting between each group of porters: ")

        # Ask for input
        #remoteServer    = raw_input("Enter a remote host to scan: ")
        remoteServer=ip
        remoteServerIP  = socket.gethostbyname(remoteServer)

        # Print a nice banner with information on which host we are about to scan
        print "-" * 60
        print "Please wait, scanning remote host", remoteServerIP
        print "-" * 60

        # Using the range function to specify ports (here it will scans all ports between 1 and 1024)

        # We also put in some error handling for catching errors

        HashMapOfPorts = {}
        port22 = 0
        try:
            for port in range(1,23): 
                if port%10==10:
                 time.sleep(secondForWait)
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((remoteServerIP, port))
                if result == 0:
                    HashMapOfPorts[port] = "Open"
                    print "Port {}:      Open".format(port)
                    if port == 22:
                       port22 = 1 
                else:
                    HashMapOfPorts[port] = "Close"
                    print "Port {}:      Close".format(port)    
                    if port == 22:
                       port22 = 0 
                sock.close()
                
                 #Write the test to file
            
            with open("SlowScanFile.txt", "w") as f:
                f.write('| Port number | Status |\n')
                for key, value in HashMapOfPorts.items():
                    f.write('| %s | %s |\n' % (key, value))
        
        
        except KeyboardInterrupt:
            print "You pressed Ctrl+C"
            sys.exit()
        
        except socket.gaierror:
            print 'Hostname could not be resolved. Exiting'
            sys.exit()
        
        except socket.error:
            print "Couldn't connect to server"
            sys.exit()

        return port22
