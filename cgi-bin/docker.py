#!/usr/bin/python3
print("content-type: text/html")
print()


import cgi
form = cgi.FieldStorage()
osName = form.getvalue("oName")
imgName = form.getvalue("iName").lower()

#print(osName)
#print(imgName)
import subprocess
command = "sudo docker run -d -i --name {} {}".format(osName,imgName)
op=subprocess.getstatusoutput(command)
print("=========================Launching the OS==========================")
print("<br/>==============================================================<br/>")
if op[0] == 0: 
    #exit code 0 means os is launched successfully...!
    print("<br/>{} OS with name \'{}\' launched successfully. ".format(imgName.upper(),osName.upper()))
elif op[0] == 125:
    #exit code 125 means the os with the name given already exists...!
    print("<br/> {} OS with name \'{}\' already exists. Please launch with another name".format(imgName.upper(),osName.upper()))
else: #any exit code other the above two means failure in launching the OS..
    print("<br/>Couln't launch the OS right now<br/>")

print("<form action=\"/AutomateDocker.html\"><br/><input type=\'submit\' value=\'Go to Docker Dashboard\'/></form>")
print("<form action=\"/index.html\"><input type=\'submit\' value=\'Back to Main MENU\'/><br/> </form> ")
