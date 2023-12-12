import imaplib
import os
import smtplib
import ssl
import email

import subprocess

import requests


imap_port = 993
imap_server = "imap.immerda.ch"

smtp_port = 465
smtp_server = "smtp.immerda.ch"

account_email = "teko@fabianhirter.ch"

password = input("Type your password and press enter:")
api_key = input("Provide your API key:")

mailbox = "INBOX"

PUBLIC_KEY_FILE = '../public_key.asc'
public_key_file_handler = open(PUBLIC_KEY_FILE, "r")
public_key = public_key_file_handler.readlines()


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
                body = str(part.get_payload(decode=True))
                return from_field, body
            else:
                continue


def send_mail(message, receiver_email):
    context = ssl.create_default_context()

    #encrypted_message = encrypt_message(g_key, data)

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(account_email, password)
        server.sendmail(account_email, receiver_email, message)


def encrypt_message(recipient_mail, message):
    """
    Encrypts data using key.
    """

    temp_message_path = "./tmp.txt"
    temp_message = open(temp_message_path, "w")
    temp_message.writelines(message)

    # gpg --recipient 6B0AC064EA829F61F730447DEF62CA8C485DEE52 --batch -o- --encrypt <(printf "foo")
    status = subprocess.check_call([
        "gpg",
        "--recipient", recipient_mail,
        "--batch",
        "--encrypt", temp_message_path
    ])

    temp_message_path_encrypted = f"{temp_message_path}.gpg"

    if status == 0:
        with open(temp_message_path_encrypted, mode='rb') as file:
            encrypted_message = file.read()

        os.remove(temp_message_path)
        os.remove(temp_message_path_encrypted)

        return encrypted_message


def get_coordinates(address):
    url = f"https://api.openrouteservice.org/geocode/search?api_key={api_key}&text={address}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["features"][0]["geometry"]["coordinates"]
    else:
        print(f"Request failed with status code {response.status_code}")


sender, address = get_latest_new_email()
coordinates = get_coordinates(address)
message = ''.join(str(coordinate) for coordinate in coordinates)
send_mail(message, sender)