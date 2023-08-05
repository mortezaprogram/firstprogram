from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count=driver.find_element(By.CSS_SELECTOR,"#articlecount  a")


all_portals=driver.find_element(By.LINK_TEXT,"Community portal")
search=driver.find_element(By.NAME,"search")
search.send_keys("python")
search.send_keys(Keys.ENTER)