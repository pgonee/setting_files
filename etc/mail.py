#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib, os#, glob, mimetypes

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.MIMEText import MIMEText
from email import Encoders

"""
    * Exceptions
"""
class Mail_Sender_CommonError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return repr(self.message)

class Mail_Sender_CanNotConnectToSMTPServer(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return repr(self.message)

class Mail_Sender_CanNotCloseConnection(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return repr(self.message)

class Mail_Sender_NotSignIn(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return repr(self.message)

class Mail_Sender_UnknownError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return repr(self.message)

"""
    * Classes
"""

class Sender(object):
    def __init__(self, mail_type="localhost", user="", pwd=""):
        self.mail_type = mail_type
        self.user = user
        self.pwd = pwd
        self.mail_server = None
        self.connect(self.mail_type, self.user, self.pwd)

        self.test_mode = False

    def connect(self, mail_type="localhost", user="", pwd=""):
        if not mail_type:
            print "set mail_type"
            return

        if mail_type == "gmail" and not( user and pwd ):
            print "set user and password"
            return

        self.mail_server = self._connect_to_smtp(mail_type, user, pwd)
        self.mail_type = mail_type
        self.user = user
        self.pwd = pwd

    def close(self):
        try:
            self.mail_server.close()
            self.mail_server = None
        except:
            raise Mail_Sender_CanNotCloseConnection, "can't close your smtp connection."

    def send_mail(self, target=[], title="", text="", filepath="", filename=""):
        while 1:
            result = self.send(target, title, text, filepath, filename)
            if result:
                return result
            else:
                self.connect(self.mail_type, self.user, self.pwd)

    def send(self, target=[], title="", text="", filepath="", filename=""):
        if self.test_mode:
            return True
        if type(target) != list:
            print "\"target\" is list type."
            return False
        if not target:
            print "set target's mail address"
            return False
        if self.mail_server == None:
            print "set mail_server with connect()"
            return False

        msg = MIMEMultipart()
        msg["Subject"] = title
        msg["From"] = self.user
        msg["To"] = ""
        for addr in target:
            msg["To"] += addr+", "
        msg.attach(MIMEText(text, "plain", "utf-8"))

        if filepath:
            part = MIMEBase("application", "octet_stream")
            part.set_payload(open(filepath, "rb").read())
            Encoders.encode_base64(part)
            if not filename:
                filename = os.path.basename(filepath)
            part.add_header("Content-Disposition", "attachment; filename=\"%s\"" % filename)
            msg.attach(part)

        result = False
        try:
            result = self.mail_server.sendmail(self.user, target, msg.as_string())
            result = not(len(result))
        except:
            result = False
        return result

    def _connect_to_smtp(self, mail_type, user, pwd):
        mail_server = None
        if mail_type == "gmail":
            mail_server = smtplib.SMTP("smtp.gmail.com", 587)
        elif mail_type == "localhost":
            mail_server = smtplib.SMTP("localhost")
        mail_server.ehlo()
        mail_server.starttls()
        mail_server.ehlo()

        if mail_type == "gmail":
            mail_server.login(user, pwd)
        return mail_server
