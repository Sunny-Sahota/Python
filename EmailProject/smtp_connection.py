import smtplib, ssl

port = 465 # For ssl 
password = input("Type password and press enter: ")
sender_email = "development2048@gmail.com"
receiver_email = "developmentrecive12@gmail.com"

message = """ """

#Create a ssl context 
#This value indicates that the context may be used to authenticate web servers (therefore, it will be used to create client-side sockets).
context = ssl.create_default_context() 

with smtplib.SMTP_SSL("smtp.gmail.com", port , context= context) as server:
    server.login(sender_email, password)

    server.sendmail()



    
    #Email information 
    