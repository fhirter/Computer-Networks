import imaplib
import smtplib
import ssl
import email

import requests

imap_port = 993
imap_server = "imap.immerda.ch"

smtp_port = 465
smtp_server = "smtp.immerda.ch"

account_email = "teko@fabianhirter.ch"

password = input("Type your password and press enter:")
api_key = input("Provide your API key:")

mailbox = "INBOX"


def get_latest_new_email():
    with imaplib.IMAP4_SSL(imap_server) as server:
        server.login(account_email, password)
        server.select(mailbox)

        response, data = server.search(None, '(UNSEEN)')

        # get the latest
        data = data[0].split()
        latest = data[-1]

        # mark the email as read
        server.store(latest, '+FLAGS', '\Seen')

        # fetch the email (RFC822) for the ID (latest)
        result, email_data = server.fetch(latest, "(BODY[])")
        raw_email = email_data[0][1].decode("utf-8")
        email_message = email.message_from_string(raw_email)

        # Get the 'From' field
        from_field = email_message['From']

        # print the email body
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                return from_field, body
            else:
                continue


def send_mail(message, receiver_email):
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(account_email, password)
        server.sendmail(account_email, receiver_email, message)


def get_coordinates(address):
    url = f"https://api.openrouteservice.org/geocode/search?api_key={api_key}&text={address}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["features"][0]["geometry"]["coordinates"]
    else:
        print(f"Request failed with status code {response.status_code}")

