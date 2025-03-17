import imaplib
import email
from email.header import decode_header

def connect_to_email(username, password, imap_server="imap.gmail.com", imap_port=993):
    try:
        imap = imaplib.IMAP4_SSL(imap_server, imap_port)
        imap.login(username, password)
        return imap
    except Exception as e:
        print(f"Error connecting to email server: {e}")
        return None

def fetch_latest_emails(imap, folder="INBOX", count=1):
    try:
        imap.select(folder)
        status, messages = imap.search(None, "ALL")
        if status != "OK":
            print("Error fetching emails")
            return []

        email_ids = messages[0].split()[-count:]
        emails = []

        for email_id in email_ids:
            res, msg = imap.fetch(email_id, "(RFC822)")
            if res != "OK":
                print(f"Error fetching email with ID {email_id}")
                continue

            for response in msg:
                if isinstance(response, tuple):
                    msg_data = email.message_from_bytes(response[1])
                    emails.append(parse_email(msg_data))

        return emails
    except Exception as e:
        print(f"Error fetching latest emails: {e}")
        return []

def parse_email(msg):
    try:
        # Decode email subject
        subject, encoding = decode_header(msg.get("Subject"))[0]
        subject = subject.decode(encoding or "utf-8") if isinstance(subject, bytes) else subject

        # Decode sender email
        sender, encoding = decode_header(msg.get("From"))[0]
        sender = sender.decode(encoding or "utf-8") if isinstance(sender, bytes) else sender

        # Parse email body
        body = ""
        for part in msg.walk() if msg.is_multipart() else [msg]:
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition", ""))

            if content_type == "text/plain" and "attachment" not in content_disposition:
                try:
                    body = part.get_payload(decode=True).decode()
                    break
                except Exception:
                    continue

        return {"subject": subject, "sender": sender, "body": body}
    except Exception as e:
        print(f"Error parsing email: {e}")
        return {"subject": None, "sender": None, "body": None}

def main():
    username = ""
    password = ""

    imap = connect_to_email(username, password)
    if not imap:
        return

    emails = fetch_latest_emails(imap, count=1)

    for email_data in emails:
        print(f"Subject: {email_data['subject']}")
        print(f"From: {email_data['sender']}")
        print(f"Body:\n{email_data['body']}")

    imap.close()
    imap.logout()

if __name__ == "__main__":
    main()

