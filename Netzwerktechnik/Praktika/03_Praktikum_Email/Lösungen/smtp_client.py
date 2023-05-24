import smtplib
import ssl

port = 465
smtp_server = "smtp.immerda.ch"
sender_email = "teko@fabianhirter.ch"
receiver_email = "fabian.hirter@edu.teko.ch"
password = input("Type your password and press enter:")
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
