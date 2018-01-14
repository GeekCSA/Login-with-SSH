# Project Launch Instructions:

When we run the code ?? Was asked to enter an IP address of the destination computer, hostname, track of a file with passwords for the logon and port experiment.

The program will check which ports are open, and output a file with the ports and whether each is open or closed.

If Port 22 is open, the program tries to enter the destination computer using passwords

If the entrance is successful, access to the destination terminal will be possible.

Then we will move the FTP server to the destination by command:

scp Dest_name @ Dest_IP: File_from_dest Location_in_the_sorce

(The command copy file from dest to sorce)

Then run the server at the destination.

When the server is activated with the target, we will activate the client with us and request a file from the destination.
