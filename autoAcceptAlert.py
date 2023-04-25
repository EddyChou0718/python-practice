from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from time import sleep
import datetime
import requests

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)
driver.get("http://localhost:3000/")
button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='test']")))


def test():
  button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='test']")))
  button.click()

  try:
    alert = driver.switch_to.alert

    if not alert is None:
      # sleep(2)
      alert.accept()
      print('alert accept')
      test()

  except NoAlertPresentException:
    print('no more alert')

test()
