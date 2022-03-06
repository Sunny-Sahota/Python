import smtplib, ssl

port = 465 # For ssl

password = input("Type your password and press enter. ")

#Create a ssl context

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context-context) as server:
    server.login("development2048@gmail.com", password)