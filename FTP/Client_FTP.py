from ftplib import FTP
import os
import fileinput

ftp = FTP('')
ftp.connect('IP_DEST',1026)
ftp.login()
ftp.cwd('?????') #replace with your directory - The destination place, the root is the server place!
ftp.retrlines('LIST')

def uploadFile():
 filename = '?????' #replace with your file in your folder - The source file
 ftp.storbinary('STOR '+ os.path.basename(filename), open(filename, 'rb'))
 ftp.quit()

def downloadFile():
 filename = '?????' #replace with your file in the directory ('directory_name')
 localfile = open(filename, 'wb')
 ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
 ftp.quit()
 localfile.close()

#uploadFile()
downloadFile()
