#!/usr/bin/env python
# -*- coding: utf-8 -*-   
'''
import os
import smtplib
import mimetypes
import string
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEAudio import MIMEAudio
from email.MIMEImage import MIMEImage
from email.Encoders import encode_base64
import email
"""This function performs send mail.
    The arguments are:
            - subject                       : The email subject description.
            - text                          : the email content description.
            - *attachmentFilePaths          : The attachment will apend to the email,it is opptional.


    Example:

         >>> sendMail('This is a test email', 'Send a test email.',r'C:\build.zip')
"""
def sendMail(subject, text, *attachmentFilePaths):
    emailUser = 'yong.xu@xor-media.tv'
    emailPassword = 'qwerty'
    recipient = ["jing.cao@xor-media.tv","hongzhou.li@xor-media.tv","maggie.gao@xor-media.tv"]
    #recipient = ["hongzhou.li@xor-media.tv","yong.xu@xor-media.tv" ]
    msg = MIMEMultipart()
    msg['From'] = emailUser
    msg['To'] = string.join(recipient, ";")
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
    for attachmentFilePath in attachmentFilePaths:
        msg.attach(getAttachment(attachmentFilePath))
    try:
        mailServer = smtplib.SMTP('mail.xor-media.tv', 25)
        #u'使用"helo"指令向服务器确认身份。相当于告诉smtp服务器"我是谁"'。
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(emailUser, emailPassword)
#         print "-----------------------------------------------"
#         print msg.as_string()
#         print "-----------------------------------------------"
#
        mailServer.sendmail(emailUser, recipient, msg.as_string())
        mailServer.quit()
        print('Success to sent email.')
    except Exception, e:
        print str(e)

def getAttachment(attachmentFilePath):
    contentType, encoding = mimetypes.guess_type(attachmentFilePath)
    print contentType
    print encoding
    if contentType is None or encoding is not None:
        contentType = 'application/octet-stream'
    mainType, subType = contentType.split('/', 1)
    print mainType
    print subType
    file = open(attachmentFilePath, 'rb')
    if mainType == 'text':
        attachment = MIMEText(file.read())
        print attachment
    elif mainType == 'message':
        attachment = email.message_from_file(file)
    elif mainType == 'image':
        attachment = MIMEImage(file.read(),_subType=subType)
    elif mainType == 'audio':
        attachment = MIMEAudio(file.read(),_subType=subType)
    else:
        attachment = MIMEBase(mainType, subType)
    attachment.set_payload(file.read())
    encode_base64(attachment)
    file.close()
    attachment.add_header('Content-Disposition', 'attachment',   filename=os.path.basename(attachmentFilePath))
    return attachment
'''
