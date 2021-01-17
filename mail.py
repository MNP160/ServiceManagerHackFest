import smtplib, ssl
from email.message import EmailMessage


def send_mail(name, url, status):
    port=465
    message = EmailMessage()

    sender_email = "bg_00@abv.bg"  
    message['From']=sender_email
    message['To']="mpenev13@gmail.com"  
    message['Subject']='service with name '+ name + ' bad status'  
    body="service with name " + name + " at url "+ url + " received faulty status "+ status
    message.set_content(body)      
        
    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.abv.bg', port, context) as server:
       # server.ehlo()
        #server.starttls()
        #server.ehlo()
        server.login(sender_email, 'mladen13')

       #server.sendmail(sender_email, receiver_email, message)  
        server.send_message(message)


#send_mail('webapi2', 'localhost:8083', '500')

