import smtplib

my_email=" "
my_password=" "
def send_emails(title,msg):
    server = smtplib.SMTP('smtp.yandex.com',465)
    server.ehlo()
    #server.starttls()
    server.login(my_email,my_password)
    #message = 'Subject: {}\n\n{}'.format(title,msg)
    server.sendmail(from_addr="PtestPtest2000@yandex.com",to_addrs="PtestPtest2000@yandex.com",msg="Subject:HELLO\n\nThis is for test.")
    server.quit()
    print('E-mails successfully sent!')

send_emails('Test Mail', 'Yes its a test mail!')