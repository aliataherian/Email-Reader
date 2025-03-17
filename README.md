# Email Reader

## Overview
This Python script connects to an IMAP email server (e.g., Gmail, Outlook, Yahoo) to fetch the latest emails and parse their content (subject, sender, and body). It supports SSL-encrypted connections and can be customized to work with different email providers.

## Features
- **IMAP Support:** Works with any IMAP-enabled email server.
- **Fetch Multiple Emails:** Retrieve and process a specified number of emails.
- **Email Parsing:** Extracts and decodes the subject, sender, and body.
- **Error Handling:** Includes robust error handling for connection and parsing issues.
- **Customizable:** Easily configure email folder, number of emails to fetch, and more.

## How It Works
1. **Connect to Email Server:** Establishes a secure connection using your email credentials.
2. **Fetch Emails:** Retrieves the latest emails from the specified folder (e.g., INBOX).
3. **Parse Emails:** Decodes and extracts relevant email data.
4. **Output:** Displays the parsed email information in a structured format.

## Requirements
- Python 3.x
- Built-in libraries: `imaplib`, `email`


## Usage
Modify the script with your email credentials:
```python
username = "your_email@gmail.com"
password = "your_password"
email_count = 5  # Change this number to fetch more or fewer emails
```
Then, run the script:
```sh
python email_reader.py
```
Example output:
```
Subject: Meeting Reminder
From: example@example.com
Body:
Don't forget our meeting tomorrow at 10 AM.
```

## Notes
- If using Gmail, enable "Less Secure Apps" or use an App Password.
- Store credentials securely (avoid hardcoding in the script).
- You can adjust the number of emails fetched by modifying the `email_count` variable.
- This script is intended for educational and automation purposes.

## License
This project is licensed under the MIT License. See `LICENSE` for details.




