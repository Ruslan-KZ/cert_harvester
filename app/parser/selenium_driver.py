from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException, ElementClickInterceptedException, StaleElementReferenceException,
    NoSuchElementException
)
import time

URL = "https://www.coursera.org/learn/fundamentals-of-robotics--industrial-automation#modules"

def open_driver():
    options = Options()
    options.add_experimental_option("detach", True)  

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver

def click_enroll_button(driver, timeout=20, retries=3):
    wait = WebDriverWait(driver, timeout)

    css = 'button[data-e2e="enroll-button"]'  
    for attempt in range(1, retries + 1):
        try:
            btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))
            
            def enabled_and_displayed(driver):
                try:
                    el = driver.find_element(By.CSS_SELECTOR, css)
                   
                    aria = el.get_attribute("aria-disabled")
                    disabled_attr = el.get_attribute("disabled")
                    is_enabled = (aria != "true") and (disabled_attr is None)
                  
                    return is_enabled and el.is_displayed()
                except Exception:
                    return False

            
            try:
                wait.until(enabled_and_displayed)
            except TimeoutException:
                
                pass

            
            btn = driver.find_element(By.CSS_SELECTOR, css)

            
            driver.execute_script("arguments[0].scrollIntoView({block:'center', inline:'nearest'});", btn)
            time.sleep(0.2)  

            
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css)))

            try:
                btn.click()
                print("Clicked by WebElement.click()")
                return True
            except ElementClickInterceptedException:
                
                print("ElementClickInterceptedException — попробую JS click")
                driver.execute_script("arguments[0].click();", btn)
                return True

        except StaleElementReferenceException:
            print(f"Attempt {attempt}: StaleElementReferenceException — пробую снова")
            time.sleep(0.5)
            continue
        except TimeoutException:
            print(f"Attempt {attempt}: Timeout — элемент не найден/не кликабелен в течение {timeout}s")
            time.sleep(1)
            continue
        except NoSuchElementException:
            print(f"Attempt {attempt}: NoSuchElementException — элемент не найден")
            time.sleep(1)
            continue
        except Exception as e:
            print(f"Attempt {attempt}: Неизвестная ошибка: {e}")
            time.sleep(1)
            continue

    print("Не удалось нажать кнопку после всех попыток.")
    return False


if __name__ == "__main__":
    driver = open_driver()
    driver.get(URL)

   
    time.sleep(2)

    
    try:
        
        banner = driver.find_elements(By.CSS_SELECTOR, 'button[data-e2e="accept-cookies"], button[aria-label="Accept"]')
        if banner:
            banner[0].click()
            print("Закрыл cookie-banner")
            time.sleep(0.5)
    except Exception:
        pass

    success = click_enroll_button(driver, timeout=15, retries=4)
    if success:
        print("Кнопка нажата успешно.")
    else:
        print("Кнопку не удалось нажать. Проверь: iframe, overlay, или защита от автоматизации.")
