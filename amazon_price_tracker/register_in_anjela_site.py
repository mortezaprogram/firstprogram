from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("http://secure-retreat-92358.herokuapp.com/")
# article_count=driver.find_element(By.CSS_SELECTOR,"#articlecount  a")
#
#
# all_portals=driver.find_element(By.LINK_TEXT,"Community portal")
fName=driver.find_element(By.NAME,"fName")
lName=driver.find_element(By.NAME,"lName")
email=driver.find_element(By.NAME,"email")


fName.send_keys("Morteza")
lName.send_keys("Khaleghi")
email.send_keys("khaleghi.morteza84@gmail.com")
submit=driver.find_element(By.CSS_SELECTOR,"form button")
submit.click()