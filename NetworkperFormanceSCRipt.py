#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from smtplib import SMTP
from apscheduler.schedulers.blocking import BlockingScheduler
import smtplib
import os



def network_assets(file_path):
    with open(file_path, "r") as files:
         ip_list = files.read().split("\n")
    return ip_list
    

def network_asset_values(ip_list, admin_emails, send_message):
    server = 'smtp.gmail.com'
    port = 465
    for ip in ip_list:
       response = os.system(f"ping -c 1 {ip} | grep 64 ")
       if response == 0:
          pass
       else:
          message = f"{ip}"
          with smtplib.SMTP_SSL(server, port) as serv:
                serv.login(sender, password)
                send_message = f" hello Network admin, the ip address : {message} is down"
                serv.sendmail(sender, admin_emails, send_message)
                



def out_put(file_path):
    network_assets = network_assets(file_path)
    network_values = newtwork_asset_values(network_assets)
    return network_values


admin_emails = input("enter admin email: ")
file_path = input("enter files where network ip addresses of assests to be monitored are stored: ")
sender = input("enter email responsible for sending message: ")
password = input("password of sender email: ")

scheduler = BlockingScheduler()
scheduler.add_job(out_put, 'interval', hours=0.5)
scheduler.start()

