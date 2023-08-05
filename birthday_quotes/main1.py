import smtplib ,ssl


my_email=" "
my_password=" "
with smtplib.SMTP_SSL("smtp.yandex.com:465") as connection:
     connection.ehlo()
     connection.starttls()
     connection.login(user=my_email,password=my_password)
     connection.sendmail(from_addr="PtestPtest2000@yandex.com",to_addrs="mobileteast1984@gmail.com"
 ,msg="Subject:HELLO\n\nThis is for test.")
