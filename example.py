from models.NotesMail import NotesMail

MAIL_SERVER_NAME = "DOMINOMSGN1/ABC_COMPANY"
MAIL_DB_NAME = "mail\your_username.nsf"

mail = NotesMail(MAIL_SERVER_NAME, MAIL_DB_NAME)
recivers = ["amy.cheng@xyz.com"]
subject = "Hello!"
body = "This is a test mail."
attachments = ["./test.xlsx"]

mail.send_mail(recivers=recivers, subject=subject,
               body=body, attachments=attachments)
