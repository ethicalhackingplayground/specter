#!/usr/bin/python


import os

def setup():
	print "[+] Installing selenium"
	os.system('pip install selenium')
	print "[+] Installing colorama"
	os.system('pip install colorama')
	print "[+] Installing fileinput"
	os.system('pip install fileinput')
	print "[+] Making password directory"
	os.system('mkdir passwords')
	print "\n[*] done.."

setup()
	
