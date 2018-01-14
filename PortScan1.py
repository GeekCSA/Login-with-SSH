'''
Created on Dec 27, 2017

@author: Moshe
'''
import socket
import subprocess
import sys
import time
import random
import SlowProtScanning
import RandomPortScanning
import EffectivePortScanning

class PortScanning(object):

	@classmethod
	def scan(self,ip):

		#Input choice from user to do slow, random or effective scanning
		print "-" * 60
		print "* For slow scanning type 1"
		print "* For random scanning type 2"
		print "* For effective scanning type 3"
		print "-" * 60
		userChoice = input("Enter your choose: ")

		while (userChoice != 1 and userChoice != 2 and userChoice != 3):
    			userChoice = input("\tPlease enter a number between 1 to 3: ")
		print "\n"
		if userChoice == 1:
			y = SlowProtScanning
			x = y.SlowScan
			return x.slowScanning(ip)   
		elif userChoice == 2:
			y = RandomPortScanning
			x = y.RandomScan
			return x.randomScanning(ip)
		elif userChoice == 3:
			y = EffectivePortScanning
			x = y.EffectiveScan
			return x.effectiveScanning(ip)
		else:
    			print "Illegal input"
    
