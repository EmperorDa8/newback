#!/usr/bin/env pyhton3
import email
import mimetypes
import os
import smtplib


def generate_email(From,To,subject_line,body,Attachment):
    msg=email.message.EmailMessage()
    msg["From"]=From
    msg["To"]=To
    msg["Subject"]=subject_line
    msg.set_content(body)

    if not attachment_path==" ":
        attachment_name=os.path.basename(attachment_path)
        mimetype,_=mimetypes.guess_type(attachment_path)
        mime_type,mime_subtype=mimetype.split("/",1)
        
       with open(attachment_path, "rb")as fg:
            msg.add_attachment(fg.read(), maintype=mime_type, subtype=mime_subt$

    return msg


def send_email(msg):
   mail_server=smtplib.SMTP("localhost")
   mail_server.send_message(msg)
   mail_server.quit()


