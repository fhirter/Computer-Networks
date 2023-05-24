# Praktikum E-Mail
## Lernziele

## Aufgabenstellung
Schreibe in Python einen einfachen E-Mail-Client, der eine E-Mail über smtp versendet und über imap empfängt.

Nutze einen eigenen Mailserver oder den zur Verfügung gestellten. 
Dessen Verbindungsangaben findest du hier:
https://docs.immerda.ch/de/services/email/clients/

## E-Mail Senden
Nutze folgende Befehle der smtplib um E-Mails zu versenden. Konfiguriere die verwendeten Variablen entsprechend.
```python
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
```

Erstelle die Nachricht so, dass Subject, Absender- und Empfängeradresse gesetzt werden.

## E-Mail Empfangen
Empfange die Mails mit IMAP:

```python
with imaplib.IMAP4_SSL(imap_server) as server:
    server.login(sender_email, password)
    mailboxes = server.list()
    server.select(mailbox)

    typ, data = server.search(None, 'ALL')
    for num in data[0].split():
        typ, data = server.fetch(num, '(RFC822)')
        print('Message %s\n%s\n' % (num, data[0][1]))
```