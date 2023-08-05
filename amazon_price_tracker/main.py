from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
URL="https://www.amazon.com/Cisco-ACI-Comprehensive-Implementation-Troubleshooting/dp/1484288378/ref=sr_1_1?crid=33OAF2ZDPS1VG"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
         "Accept-Language":"en-US,en;q=0.9"}
r=requests.get(URL, headers=headers)

soup=BeautifulSoup(r.content,"lxml")
print(soup.prettify())
price = soup.find(class_="a-text-right dp-used-col").get_text()
price_without_currency=price.split("$")[1]
price_as_float=float(price_without_currency)
print(price_without_currency)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200
my_email="P"
my_password="g"


if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP('smtp.yandex.com',465) as connection:
        connection.starttls()
        result = connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")

        )
        print("Email Sent")