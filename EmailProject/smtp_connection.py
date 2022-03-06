import smtplib, ssl

port = 465 # For ssl 
password = input("Type password and press enter: ")
sender_email = "development2048@gmail.com"
receiver_email = "developmentrecive12@gmail.com"

from email_gen import EmailString

message = """\
Subject: Hi there

This message is sent from Python."""

#Create a ssl context 
#This value indicates that the context may be used to authenticate web servers (therefore, it will be used to create client-side sockets).
context = ssl.create_default_context() 

with smtplib.SMTP_SSL("smtp.gmail.com", port , context= context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email , message)
    
    #Handler needed
    #2FA , mfa service 
    #function to retrive server information 
    #EmailString needs to be a list , Json 
    
    