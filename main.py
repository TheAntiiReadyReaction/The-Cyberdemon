from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from string import ascii_letters, punctuation, digits
from random import choice, randint

import time

def shoot () :
  driver = webdriver.Firefox()
  target = "https://i-ready.fandom.com/wiki/I-Ready_Wiki"

  driver.get(target)

  min = 12
  max = 15

  timeout = 10

  string_format = ascii_letters
  generated_string = "".join(choice(string_format) for x in range(randint(min, max)))

  add_page = driver.find_element_by_xpath("//a[@title='Add new page']")
  add_page.click()

  element_present = EC.presence_of_element_located((By.ID, 'create-page-dialog__title'))
  WebDriverWait(driver, timeout).until(element_present)

  new_page = driver.find_element_by_class_name("wds-input__field")
  new_page.send_keys(generated_string)

  new_page.send_keys(Keys.RETURN)

  time.sleep(1)
  shoot()

shoot()