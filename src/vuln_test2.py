#!/usr/bin/env python
print("some random code")
import requests, subprocess, shlex, hashlib  

address = requests.request("get", "http://127.0.0.1/nothinghere")

cmd = "ping -c 1 %s" % address
subprocess.Popen(cmd, shell=True)

#The loophole is glaring, and any command that we put in as an address is executed on the application server. All an attacker has to do is add a semi-column and then put in whatever commands they want. For example, google.com ; ls -la. Fixing this is easy, though, because Python provides built-in functions to remedy this. 
#Python
#
#address = request.args.get("address")

#command = "ping -c 1 {}".format(address)
#args = shlex.split(command)
#subprocess.Popen(args)

###



#################################



####TWITTER_OAUTH_TOKEN = "dkedjekdjekldjekldje"
####TWITTER_OAUTH_SECRET = "dkejkdjekdjkejdkjekdjekjdkjed"
####
####
####hashedPass = hashlib.md5(requests.request.params['fooey']).hexdigest()
####hashedPass2 = hashlib.md5(requests.request.params['fooey2']).hexdigest()
####hashedPass3 = hashlib.md5(requests.request.params['fooey3']).hexdigest()
####
####
####hashedPass31 = hashlib.md5(requests.request.params['fooey31']).hexdigest()
####hashedPass32 = hashlib.md5(requests.request.params['fooey32']).hexdigest()
####hashedPass33 = hashlib.md5(requests.request.params['fooey33']).hexdigest()
####hashedPass34 = hashlib.md5(requests.request.params['fooey34']).hexdigest()



#####################################################


#A Directory Traversal Attack is also caused by improper user input validation. This can lead to sensitive files to be exposed and even to remote code execution. It arises if the path of file access by Python script is not properly checked. An attacker can manipulate the file path for example to something like /etc/passwd…

####import os
####
####file_location = input('\nType location: ') # /Users/christophervandermade/../area51.txt
####
##### open and read file
####file = open(file_location, "r")
####print(file.read())

#How can you solve it? 
#
#This can be solved by Sanitizing the user input using for example “shlex”. Also, you can maintain an allowed list of files that the user can access or set up a static safe directory. Try to avoid the usage of direct paths. You can also use the `os.path.realpath` function to clean up a path and return its canonical form (absolute path): 

#import os
#
#file_location = input('\nType location: ') # /Users/christophervandermade/../area51.txt
#print(f"File path before: {file_location}\n")
#real_path = os.path.realpath(file_location)
#print(f"File path before: {real_path}")

# open and read file
#file = open(file_location, "r")
#print(file.read())