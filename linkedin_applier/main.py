from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import   time

driver=webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3580748757&f_AL=true&f_WT=2&geoId=101174742&keywords=network%20engineer&location=Canada&refresh=true&sortBy=R")
# driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3567017339&f_AL=true&f_WT=2&geoId=101174742&keywords=python%20developer&location=Canada&refresh=true&sortBy=R")
time.sleep(2)
sign_in_button = driver.find_element(By.LINK_TEXT,"Sign in")
sign_in_button.click()

username=driver.find_element(By.NAME,"session_key")
password=driver.find_element(By.NAME,"session_password")
username.click()
time.sleep(5)
username.send_keys("mobileteast1984@gmail.com")
password.send_keys("Salam@123")
submit=driver.find_element(By.CLASS_NAME,"login__form_action_container ")
submit.click()
# jobs-save-button artdeco-button artdeco-button--3 artdeco-button--secondary
all_job_list=driver.find_elements(By.CSS_SELECTOR,".job-card-container--clickable")
print(all_job_list.text)
for job in all_job_list:
    print(job.text)
    job.click()
    time.sleep(5)
    try:
        save_button=driver.find_element(By.CLASS_NAME,"jobs-save-button")
        save_button.click()
        print("One job saved")
    except:
        print("ii is done.")
        continue


