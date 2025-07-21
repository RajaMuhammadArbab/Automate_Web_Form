import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import time
import logging



logging.basicConfig(
    filename = "submission_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try :     
    data = pd.read_csv("form_data.csv")
except Exception as e:
    logging.error(f"Failed to read CSV file: {e}")
    exit()


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

form_path = os.path.abspath("form.html")
driver.get(f"file://{form_path}")


for index , row in data.iterrows():
    try:
           
        driver.find_element(By.NAME,'name').clear()
        driver.find_element(By.NAME,'name').send_keys(row["name"])

        driver.find_element(By.NAME,'email').clear()    
        driver.find_element(By.NAME,'email').send_keys(row["email"])

        driver.find_element(By.NAME, 'contactno').clear()
        driver.find_element(By.NAME, 'contactno').send_keys(row["contactno"])
        
        driver.find_element(By.NAME,'address').clear()
        driver.find_element(By.NAME,'address').send_keys(row["address"])
        
               
        gender = row["gender"].strip().lower()
        if gender == "male":
            driver.find_element(By.ID,"gender_male").click()        
        elif gender =="female":
            driver.find_element(By.ID,"gender_female").click()
            
            
        subcribe_checkbox = driver.find_element(By.ID ,"subscribe_newsletter")
        if row ["subscribe"].strip().lower() =="yes":
            if not subcribe_checkbox.is_selected:
                subcribe_checkbox.click()
        else:
            if subcribe_checkbox.is_selected():
                subcribe_checkbox.click()
        
        
        city_selected = Select(driver.find_element(By.ID , 'city'))
        city_selected.select_by_visible_text(row['city'])
        
        
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        
        
        logging.info(f"Submitted Sucessfully for : {row ['name']}")
        time.sleep(2)
        
        driver.get(f"file://{form_path}")
        time.sleep(2)
        
    except Exception as e:
        logging.error(f"error on row {index+1}({row.get('name' , 'unknown')}):as {e}")
    continue


driver.quit()
logging.info("Form Submission Script Sucessfully")



