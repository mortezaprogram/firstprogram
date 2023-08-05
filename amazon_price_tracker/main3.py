from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/")
event_times=driver.find_elements(By.CSS_SELECTOR,".event-widget time")
event_names=driver.find_elements(By.CSS_SELECTOR,".event-widget li a")
events={}

for n in range(len(event_times)):
    events[n]={
        "time":event_times[n],
        "name":event_names[n],
    }

print(events)
