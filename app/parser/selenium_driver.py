from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title
print("dddsd")

driver.implicitly_wait(0.5)

test_box = driver.find_element(by=By.NAME, value="text")
submit_button =driver.find_element(by=By.CSS_SELECTOR, value="button")
test_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text
driver.quit()