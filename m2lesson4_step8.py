from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

text_tag = WebDriverWait(browser, 5).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100")
)
button = browser.find_element_by_id("book")
button.click()

x_tag = browser.find_element_by_id("input_value")
x = int(x_tag.text)
e = math.exp(1)
y = str(math.log(abs((12*math.sin(x))), e))
ans = browser.find_element_by_id("answer")
ans.send_keys(y)
submit = browser.find_element_by_id("solve")
submit.click()
