# import smtplib
# from email.message import EmailMessage

# email = EmailMessage()
# print(email)
# email['from'] = 'Python <dizzymonde23@proton.me>'
# email['to'] = 'davebostons2017@gmail.com'
# email['subject'] = 'Automated Message Test'

# email.set_content("Ok so if youre seeing this, a message was sent from another email using a python script")

# with smtplib.SMTP(host='localhost',port=1234) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()

#     smtp.login('dizzymonde23@proton.me','Isaac@2001')
#     smtp.send_message(email)
#     print("Mail sent......")
###################################
import getpass
import smtplib


from_mail = "davidboateng68@outlook.com"
password = getpass.getpass("Type password: ")

to_mail = "dizzymode23@proton.me"

message = "Hello this is a test email"

with smtplib.SMTP("smtp-mail.outlook.com",587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(from_mail,password)
    smtp.sendmail(from_mail,to_mail,message)



