from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
driver = webdriver.Chrome()
driver.get("https://www.vogue.in/")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,'//a[text()="Shopping"]').click()
sleep(2)
Olive = driver.find_element(By.XPATH,'(//span[@class="SpanWrapper-kFnjvc fvrhBe responsive-asset"]/child::picture/img)[2]')
action = ActionChains(driver)
action.scroll_to_element(Olive)
sleep(2)
Olive.click()
sleep(2)

all_windows = driver.window_handles
driver.switch_to.window(all_windows[-1])
sleep(2)
name = driver.find_element(By.XPATH,'//h1[@class="product-title title mb-0 h2"]')
price = driver.find_element(By.XPATH,'//span[@class="product-price-final product-price-final-sale"]/child::span[2]')
print(f'name = {name.text}, price = {price.text}')
sleep(2)
driver.quit()

