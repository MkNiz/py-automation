import smtplib
import config

smtp_obj = smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT)
ehlo = smtp_obj.ehlo()
if ehlo[0] == 250:
    print("Code 250 : ehlo succeeded")
else:
    print("Code", ehlo[0], ": ehlo did not succeed")
    
s_tls = smtp_obj.starttls()
if s_tls[0] == 220:
    print("Code 220 : TLS encryption set and server is ready")
else:
    print("Code", s_tls[0], ": Server is not ready")
    
log_in = smtp_obj.login(config.EMAIL, config.PWD)
if log_in[0] == 235:
    print("Code 235 : Successful Login")
else:
    print("Code", log_in[0], ": Login did not succeed")
    
failures = smtp_obj.sendmail(config.EMAIL, config.TARGET_EMAIL, 
    'Subject: Test Email\nThis was a test email sent with a Python script')

for k, v in failures.items():
    print("Failed to send " + k + " to " + v + ".")
    
if not failures:
    print("Email successfully sent!")
    
smtp_obj.quit()

