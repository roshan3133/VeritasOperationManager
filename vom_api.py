import sys
import argparse
from logger import log as logger
from flask import Flask,request
import requests
import commands
import subprocess
import os 

domain="vom-vcs-monitor"
cert_filename="cert.txt"
port="14161"

def get_session_id(out):
    for i in out[1].split():
      if "cookie" in i:
	for ses in  i.split('"'):
	  if "JSESSIONID" in ses:
	    return ses
    else:
      return False
  
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-username", "--Username", type=str, default=None, help="Please Prvide XLS dir name with full path.")
  parser.add_argument("-passwod", "--Password", type=str, default=None, help="Please Provilde xls filename.")
  parser.add_argument("-vom_server_ip", "--VomServerIp", type=str, default=None, help="Please Provilde IP address of Veritas Operation Manager server.")
  args = parser.parse_args()
  
  if args.Username and args.Password and args.VomServerIp:
    host=args.VomServerIp
    user=args.Username
    passwd=args.Password
    call_url="https://"+host+":"+port+"/vom/api/"
    login_url="https://"+host+":"+port+"/vom/api/login"
    logout_url="https://"+host+":"+port+"/vom/api/logout"
    getcert_url="https://"+host+":"+port+"/vom/api/gencert"
    get_login_cmd = "curl -g -k -F certfile=@"+cert_filename+" "+login_url
    get_cert_cmd = "curl -g -k -d user="+user+" -d password="+passwd+" -d domain="+domain+" "+getcert_url
    all_host = "curl -g -k -X POST -b \""+session+"\" "+call_url+"/query/server/host"
    #user_login_details = {"user": "%s","password":"%s", "domain":"%s"} % (args.Username[0], args.Password[0], domain)
    #user_login_details = {"user": args.Username[0],"password":args.Password[0], "domain":domain} 
    #print login_url, user_login_details, type(user_login_details) 
    #requests.packages.urllib3.disable_warnings()
    #auth = requests.post(getcert_url, user_login_details)
    #files = open('cert.txt', 'rb').read()
    #auth = requests.api.request('post', login_url, data=user_login_details, cert="VOM-VCS-MONITOR.crt")
    get_cert_cmd = "curl -g -k -d user="+args.Username+" -d password="+args.Password+" -d domain="+domain+" "+ getcert_url
    #print get_cert_cmd
    #cert = commands.getstatusoutput(get_cert_cmd)
    login_out = commands.getstatusoutput(get_login_cmd)
    session = get_session_id(login_out)
    if session == False:
      print "Certificate expired, please regenrate cert in cert.txt file"
      logger.error( "Certificate expired, please regenrate cert in cert.txt file")
      sys.exit(0)
    print session 
    host_cmd = "curl -g -k -X POST -b \""+session+"\" "+"https://"+host+":"+port+"/vom/api/query/server/host" 
    host_out = commands.getstatusoutput(host_cmd)
    f = open("all_host.txt", "w")
    f.write(str(host_out[1])) 
    f.close()
  else:
    parser.print_help()
    sys.exit(1)

