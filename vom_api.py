#!/usr/bin/python
#===========================
#Author : - Aniket Gole
#Email : - roshan3133@gmail.com
#==========================
import sys
import argparse
from logger import log as logger
from flask import Flask,request
import requests
import commands
import subprocess
import os 

#==== Below three parameter need to change as per VOM server API details
domain="vom-vcs-monitor"
#cert_filename="VOM-VCS-MONITOR.crt"
port="14161"
#================================
def Call_Api(url, host, port, method, session, data=None):
  make_url = "https://"+host+":"+port+url 
  if method == "POST":
    out = requests.post(make_url, cookies=session, data=data, verify=False)
    return out.json()
  if method == "GET":
    logger.info("URL genrated successfully %s" % (make_url))
    out = requests.get(make_url, cookies=session, verify=False)
    return out.json()
  return False

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-username", "--Username", type=str, default=None, help="Please Prvide XLS dir name with full path.")
  parser.add_argument("-passwod", "--Password", type=str, default=None, help="Please Provilde xls filename.")
  parser.add_argument("-vom_server_ip", "--VomServerIp", type=str, default=None, help="Please Provilde IP address of Veritas Operation Manager server.")
  args = parser.parse_args()
  logger.info("Script Executed")
  
  if args.Username and args.Password and args.VomServerIp:
    host=args.VomServerIp
    user=args.Username
    passwd=args.Password
    call_url="https://"+host+":"+port+"/vom/api/"
    login_url="https://"+host+":"+port+"/vom/api/login"
    logout_url="https://"+host+":"+port+"/vom/api/logout"
    getcert_url="https://"+host+":"+port+"/vom/api/gencert"
    #get_login_cmd = "curl -g -k -F certfile=@"+cert_filename+" "+login_url
    get_cert_cmd = "curl -g -k -d user="+user+" -d password="+passwd+" -d domain="+domain+" "+getcert_url
    user_login_details = {"user": args.Username,"password":args.Password, "domain":domain}
    try:
      auth = requests.post(login_url, data=user_login_details, verify=False)
      key = auth.json()
    except:
      print "You enter wrong password"
      logger.error("You enter wrong password")
    if auth.status_code == 200:
      logger.info("Login successfully.")
    else:
      print "You enter wrong password"
      logger.error("You enter wrong password")
      sys.exit(0)
    session = {key["cookie"].split("=")[0] : key["cookie"].split("=")[1].replace(";", "")}
    print session
    out = Call_Api("/vom/api/query/server/host", host, port, "GET", session, data=None)
    #if final_out.status_code == 200:
    f = open("final_out.txt", "w")
    f.write(str(out))
    f.close()
    #else:
    #  print "Need to check" 
    #  sys.exit(0)
    #all_host = "curl -g -k -X POST -b \""+key["cookie"]+"\" "+call_url+"/query/server/host"
    #host_cmd = "curl -g -k -X POST -b \""+key["cookie"]+"\" "+"https://"+host+":"+port+"/vom/api/query/server/host" 
  else:
    logger.warn("Please use proper commandline parameter.")
    parser.print_help()
    sys.exit(1)
