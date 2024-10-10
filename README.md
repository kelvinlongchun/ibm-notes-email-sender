# IBM Notes Email Sender

## Overview

Email sender python script for IBM Notes 📧

## Get Started

### Import Model

```py
from models.NotesMail import NotesMail
```

### Create NotesMail Object

Create `NotesMail` object. You need your server name and IBM Notes nsf file path.

```py
MAIL_SERVER_NAME = "DOMINOMSGN1/ABC_COMPANY"
MAIL_DB_NAME = "mail\your_username.nsf"
mail = NotesMail(MAIL_SERVER_NAME, MAIL_DB_NAME)
```

### Send The Email

Use function `.send_email` to send the email via IBM Notes.

```py
recivers = ["amy.cheng@xyz.com"]
subject = "Hello!"
body = "This is a test mail."
attachments = ["./test.xlsx"]

mail.send_mail(recivers=recivers, subject=subject,
body=body, attachments=attachments)
```
