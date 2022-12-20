from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('../chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.get('https://adminqa.neapro.site/login')
driver.set_window_size(1024, 600)
driver.minimize_window()

driver.find_element(By.XPATH, '//*[@id="admin_email"]').send_keys('moderat@neapro.ru')
driver.find_element(By.XPATH, '//*[@id="admin_password"]').send_keys('Aa123456')
driver.find_element(By.XPATH, '//*[@id="admin_submit_action"]/input').click()

print("Test Passed Successfully")
driver.close()
