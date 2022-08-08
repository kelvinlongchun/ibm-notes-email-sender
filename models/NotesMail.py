import os
from win32com.client import Dispatch


class NotesMail:
    def __init__(self, server_name, db_name):
        self.session = Dispatch("Notes.NotesSession")
        self.db = self.session.GetDatabase(server_name, db_name)
        if not self.db.IsOpen:
            self.db.OPENMAIL

    def send_mail(self, recivers: list, **kwargs):
        default_kwargs = {
            "subject": None,
            "body": None,
            "cc": [],
            "bcc": [],
            "attachments": []
        }
        kwargs = {**default_kwargs, **kwargs}

        mail_doc = self.db.CREATEDOCUMENT

        mail_doc.Form = "Memo"
        mail_doc.SendTo = ", ".join(recivers)

        mail_doc.Subject = kwargs["subject"]
        mail_doc.Body = kwargs["body"]

        mail_doc.CopyTo = ", ".join(kwargs["cc"])
        mail_doc.BlindCopyTo = ", ".join(kwargs["bcc"])

        mail_doc_attachment = mail_doc.CreateRichTextItem("Attachment")
        for attach in kwargs["attachments"]:
            attach_absolute_path = os.path.abspath(attach)
            mail_doc_attachment.EmbedObject(1454, "", attach_absolute_path)

        mail_doc.SaveMessageOnSend = True

        mail_doc.Send(0, recivers)

        print("Email is sent.")
