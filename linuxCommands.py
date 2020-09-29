#!/usr/bin/python3

print("content-type: text/html")
print()

import cgi
_input = cgi.FieldStorage()
name = _input.getvalue("name")
cmd = _input.getvalue("cmd")

print("Hello <b>",name,"</b><br/>")
print("Good Morning  <br/>")
import subprocess as sp
if cmd != "add user":
    op = sp.getstatusoutput(cmd)
    op = list(op)
    if op[0] == 0:
        print("<br/>",op[1],"<br/>")
        print("<br/> I hope all your Requirements are fullfilled. <br/>")
        print("<t/>or do you wanna ")
    else:
        #print("<br/>",op[0],"<br/>")
        #print("<br/>",op[1],"<br/>")
        print("<br/> Couldnt complete your request right now <br/>")
else:
    op = sp.getstatusoutput("sudo useradd {}".format(name))
    if op[0] == 0:
        print("<br/>User \'{}\' created Successfully.<br/>".format(name))
    elif op[0] == 9: #exit is 9 when a user with the name given already exists...!
        print("<br/>User with name \'{}\' already Exists. <br/>".format(name))

print("<form action=\"/LinuxCommands.html\"><br/><input type=\'submit\' value=\'Execute more Linux Commands\'/> </form>")
print("<form action=\"/index.html\"><input type=\'submit\' value=\'Back to Main MENU\'/> </form>")
