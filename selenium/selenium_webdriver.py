from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/Cisco-Made-Simple-Step-Step/dp/B0C6P6HXJP/ref=sr_1_3?crid=5GKS5DODTB54&keywords=cisco+aci&qid=1688396645&sprefix=cisco+aci%2Caps%2C242&sr=8-3")
item=driver.find_element(By.XPATH,'//*[@id="a-autoid-2-announce"]/span[2]')
# item=driver.find_element(By.CLASS_NAME,"a-color-base")
print(item.text.split("$")[1])
driver.close()