from mail import send_mail
from db import *
import requests
from datetime import datetime


def query_services():

    services = get_all_services() 
    for service in services:
        result = requests.get(service.get('url'))
        #print(result.status_code)
    
        print(result.elapsed.total_seconds())
        currentTime=datetime.now()
        print(result.text)
        if result.elapsed.total_seconds() > 5:

            send_mail(service.get('name'), service.get('url'),'timeout')
            create_log(service.get('name'), service.get('url'),'timeout', currentTime.strftime("%d/%m/%Y %H:%M:%S"))
        elif result.status_code!='200': 
            send_mail(service.get('name'), service.get('url'),str(result.status_code))  
            create_log(service.get('name'), service.get('url'),str(result.status_code), currentTime.strftime("%d/%m/%Y %H:%M:%S"))