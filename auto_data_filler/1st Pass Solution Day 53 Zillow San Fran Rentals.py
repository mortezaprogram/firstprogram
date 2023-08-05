from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get("https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.76188887548828%2C%22east%22%3A-122.10476912451172%2C%22south%22%3A37.60277147563533%2C%22north%22%3A37.94740978946351%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D", headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")
print(response)
all_link_elements = soup.select(".list-card-top a")
print(all_link_elements)
all_links = []
for link in all_link_elements:
    href = link["href"]
    print(href)
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)


all_links = ['https://www.zillow.com/apartments/san-francisco-ca/480-potrero-ave/5mY4JQ/' ,'https://www.zillow.com/apartments/san-francisco-ca/923-folsom/5Yy6Np/' ,'https://www.zillow.com/apartments/san-francisco-ca/parkmerced/5XjKHx/' ]
all_address_elements = soup.select(".list-card-info address")
# all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]
all_addresses =['480 Potrero Ave, San Francisco, CA 94110','923 Folsom St, San Francisco, CA 94107','3711 19th Ave, San Francisco, CA 94132']
all_price_elements = soup.select(".list-card-details li")
# all_prices = [price.get_text().split("+")[0] for price in all_price_elements if "$" in price.text]
all_prices=['2870','2990','2800']

# chrome_driver_path = YOUR_PATH_TO_THE_CHROME_DRIVER
driver = webdriver.Chrome()

for n in range(len(all_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSf7ItTLyHcqacZ_zufmeIZpQ7UHDeoFWhzvpSxRnsWx85-9kQ/viewform")

    time.sleep(2)
    address = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    print(all_addresses[n])
    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()