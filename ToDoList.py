import smtplib
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("spud.savage1990@gmail.com", "Spudly010")
# message to be sent
message = "Message_you_need_to_send"
# sending the mail
s.sendmail("spud.savage1990@gmail.com", "spud.savage1991@gmail.com", message)
# terminating the session
s.quit()
