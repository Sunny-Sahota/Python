from typing import final
from SuperConnection import ConnectionInformation
from EmailContent import EmailString
import smtplib, ssl

class Email:
    
    def SendSSLEmail(emailContent):  
        #Create a ssl context 
        context = ssl.create_default_context()
        #This value indicates that the context may be used to authenticate web servers (therefore, it will be used to create client-side sockets).
        with smtplib.SMTP_SSL(ConnectionInformation.smtp_server, ConnectionInformation.ssl_port , context= context) as server:
            server.login(ConnectionInformation.sender_email, ConnectionInformation.sender_password)
            server.sendmail(ConnectionInformation.sender_email, ConnectionInformation.receiver_email , emailContent)

    def SendTSLEmail(emailContent):
        #Create a secure SSL context
        context = ssl.create_default_context()

        #Try log in to server and send email
        try:
            server = smtplib.SMTP(ConnectionInformation.smtp_server , ConnectionInformation.tls_port)
            server.ehlo() #Can be omitted
            server.starttls(context = context)
            server.ehlo() #Can be omitted
            server.login(ConnectionInformation.sender_email, ConnectionInformation.sender_password)
            server.sendmail(ConnectionInformation.sender_email, ConnectionInformation.receiver_email , emailContent)
        except Exception as e:
            print(e)
        finally:
            server.quit()


            

    
    
    