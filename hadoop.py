#!/usr/bin/python3

print("content-type: text/html")
print()

import cgi
form = cgi.FieldStorage()
query = form.getvalue("query")

import subprocess

if "start" in query:
    if "name" in query or "namenode" in query:
        #i am starting datanode even though namenode is given, because right now my os is set as datanode
        op = subprocess.getstatusoutput("sudo hadoop-daemon.sh start datanode")
        print("<br/>=============Starting the Hadoop Data Node===============<br/>================================================")
        if op[0] == 0:
            #print(op[0])
            print("<br/>DataNode Started Successfully<br/>")
        elif op[0] == 1:
            #print(op[0])
            print("<br/>DataNode is already running, stop that first<br/>")
        else:
            #print(op[0])
            print("<br/>Cannot Connect to the cluster right now.<br/>")

    elif "data" in query or "datanode" in query:
        op = subprocess.getstatusoutput("sudo hadoop-daemon.sh start datanode")
        print("<br/>=============Starting the Hadoop Data Node===============<br/>================================================")
        if op[0] == 0:
            print("<br/>DataNode Started Successfully <br/>")
        elif op[0] == 1:
            print("<br/>DataNode is already running, stop that first<br/>")
        else:
            print("<br/>Cannot Connect to the cluster right now.<br/>")
    else:
        print("<br/>I Can't Understand what you want, Please type in again.<br/>")

elif "stop" in query:
    if "name" in query or "namenode" in query:
        op = subprocess.getstatusoutput("sudo hadoop-daemon.sh stop datanode")
        print("<br/>=============Stopping the Hadoop Data Node===============<br/>===============================================")
        print("<br/>",op[1],"<br/>")
        print("DataNode stopped successfully<br/>")
    
    elif "data" in query or "datanode" in query:
        op = subprocess.getstatusoutput("sudo hadoop-daemon.sh stop datanode")
        print("<br/>=============Stopping the Hadoop Data Node===============<br/>================================================")
        print("<br/>",op[1],"<br/>")
        print("Datanode Stopped Successfully<br/>")
    else:
        print("<br/>I Can't Understand what you want, Please type in again.<br/>")

elif "report" in query:
    op = subprocess.getstatusoutput("sudo hadoop dfsadmin -report")
    print("<br/>==============Showing the Hadoop Admin Report===============<br/>=================================================")
    if op[0] == 0:
        print("<br/>",op[1],"<br/>")
    else:
        print("Make Sure you are already connected to the Hadoop Cluster")

elif "process" in query or "jps" in query:
    op = subprocess.getstatusoutput("sudo jps")
    if op[0] == 0:
        print("<br/>=============Currently running Java/Hadoop Processes===============<br/>======================================================")
        print("<br/>",op[1],"<br/>")
    else:
        print("<br/>Cannot show the running Java Processes now.")

else:
    print("<br/>I Cannot Understand your Query, Please type in again.")

print("<form action=\"/hadoop.html\"><input type=\'submit\' value=\'Go to Hadoop Dashboard\'/></form>")
print("<form action=\"/index.html\"><input type=\'submit\' value=\'Back to Main MENU\'/></form>")
