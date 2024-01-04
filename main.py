import getpass
import smtplib


from_mail = "davidboateng68@outlook.com"
password = getpass.getpass("Type password: ")

to_mail = "dizzymon23@proton.me"

message = "Hello this is a test email"

with smtplib.SMTP("smtp-mail.outlook.com",587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(from_mail,password)
    smtp.sendmail(from_mail,to_mail,message)



