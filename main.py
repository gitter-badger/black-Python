from modules import disassembler
from modules import test_ping
from modules import decompiler
import os

print ( "-" )
print ('Updating list of scripts for decompiling')

scripts = []

for filename in os.listdir('source'):
    if filename.endswith('.pyc'):
        scripts.append(filename)

test_ = ['localhost', '127.0.0.1','google.com']


while True:
	user_input = raw_input("type help for options or exit to quit >")
	
	if len(user_input) != 0:
	    if user_input == "help":
	        print ("dissasemble , decompile, scripts, test, exit")

	    if user_input == "dissasemble":
	        disassembler.disassemble_list(scripts)
	    if user_input == "decompile":
	        decompiler.decompile_list(scripts)
	    if user_input == "test":
	        test_ping.ping(test_)
	    if user_input == "scripts":
	        print(scripts)
	    if user_input == "exit":
	    	break
	else:
	    break

