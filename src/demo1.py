#!/usr/bin/env python
print('some innocuous code output')
print('some innocuous code output')
print('some innocuous code output')


###import re
###import string
###
###import commands
###template_vars['output'] = commands.getstatusoutput('/usr/bin/process_soemthing')
###
###
####Typing in an expression like 2 * 3 will result in Result = 6 , which is the desired outcome. A malicious user, on the other hand, could type in something like __import__(‘os’).system(‘rm –rf /’)  as input. And this results in a deletion of all files and directories in the script’s folder if the process has enough privileges. 
###
###compute = input('\nYour calculation? => ')
###if not compute:
###    print ("No input")
###else:
###    print ("Result =", eval(compute))
   
#To prevent such a thing from happening, we need to validate the expressions input by a user. Something like this: 
#def validate(untrusted_input):
#    match = re.search(r'[^0-9().*/+\-]', untrusted_input)   
#    if match:
#        print('match')
#    else: 
#        print('no!')
#    return match
#
#compute = input('\nYour calculation? => ')
#if not compute:
#   print ("No input")
#else:
#    if validate(compute):
#        print ("Result =", eval(compute))
#    else:
#        print ("Error")                                           #'[^a-z]+', '^[0-9()+\-*/.]+', '^(0-9()+\-*/.)'g