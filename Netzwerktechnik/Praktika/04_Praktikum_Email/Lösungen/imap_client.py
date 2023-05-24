import imaplib


port = 993
imap_server = "imap.immerda.ch"
sender_email = "teko@fabianhirter.ch"
receiver_email = "fabian.hirter@edu.teko.ch"
password = input("Type your password and press enter:")
mailbox = "INBOX"

with imaplib.IMAP4_SSL(imap_server) as server:
    server.login(sender_email, password)
    mailboxes = server.list()
    server.select(mailbox)

    typ, data = server.search(None, 'ALL')
    for num in data[0].split():
        typ, data = server.fetch(num, '(RFC822)')
        print('Message %s\n%s\n' % (num, data[0][1]))
