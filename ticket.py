from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from time import sleep
import datetime
import requests

try:
  from PIL import Image
except ImportError:
  import Image

import pytesseract

# 設定瀏覽器驅動
driver = webdriver.Chrome()

# 設定瀏覽器選項
options = webdriver.ChromeOptions()

options.add_experimental_option("excludeSwitches", ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("prefs", {"profile.password_manager_enabled": False, "credentials_enable_service": False,'profile.default_content_setting_values':{'notifications':2}})

wait = WebDriverWait(driver, 5)
# 票券目標
ticket = "https://tixcraft.com/activity/detail/21_wakinKH"
# ticket = "https://ticket.ibon.com.tw/ActivityInfo/Details/36449"
# 票卷張數
ticket_number = 2

# 欲購買區塊
target_area = "紅218"

# 啟用時間 (年,月,日,時,分,秒)
target_time = datetime.datetime(2021,3,31,12,17,0)

# 登入
# 先用瀏覽器登入後，找到並替換以下cookie
def login():
  driver.get(ticket)

  if ticket.find('tixcraft') > 0:
    driver.add_cookie({"name": "SID", "value": "0bmde1dltf6er9reb1g8h5hu5t"})
    driver.add_cookie({"name": "CSRFTOKEN", "value": "eb0c4073676c3e8a1e632fd2eb87c22be4dc15acs%3A88%3A%22ZGkwczFETEd0eUVwMDN4Rk5rTTByYm9vdlp0RmFOWGJXA5OV0tmDmR6CgS6ze2O0YzePxzyqU5eJtF7bByHtlA%3D%3D%22%3B"})

  if ticket.find('ibon') > 0:
    driver.add_cookie({"name": "ibonqware", "value": "mem_id=73278853278318918763&mem_email=x34521@gmail.com&huiwanTK=cKtuN1Z+mprNph5N5cdgUvivr+12FiUpSWMhC4JkI7jfZYWQBwbLjjQllDryBNcfnvmOKNvAMCyi7dQ/afUX81iTyiLAh7oBKgFwZksvKeM=&ibonqwareverify=0b37fc6a97c09e17d190"})

  driver.refresh()

# 進入選位網頁
def enter_choose_area():
  if ticket.find('tixcraft') > 0:
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "立即購票"))).click()
    detail = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-href]"))).get_attribute("data-href")
    driver.get("https://tixcraft.com" + detail)

  if ticket.find('ibon') > 0:
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-buy"))).click()

  choose_area()

# 選擇位置
def choose_area():
  if ticket.find('tixcraft') > 0:

    if target_area is None:
      area = driver.find_element_by_xpath("//ul[@class='area-list']//li//a")

    if target_area is not None:
      areas = driver.find_elements_by_xpath("//ul[@class='area-list']//li//a")

      for row in areas:
        if target_area in row.text:
          area = areas[0]


  if ticket.find('ibon') > 0:
    list = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//td[@id='tdAreaList']//tr//span[text()!='已售完']")))
    area = list[0]

  print(area.text)
  # area.click()

  # try:
  #   alert = driver.switch_to_alert

  #   if not alert is None:
  #     alert.accept()
  #     choose_area();

  # except:
  #   captcha_verify()

# 輸入驗證資料
def captcha_verify():
  select = driver.find_element_by_tag_name("select")
  Select(select).select_by_visible_text(str(ticket_number))

  if ticket.find('tixcraft') > 0:
    agree_label = wait.until(EC.element_to_be_clickable((By.ID, "TicketForm_agree")))
    verify_input = driver.find_element(By.ID, 'TicketForm_verifyCode')

  if ticket.find('ibon') > 0:
    agree_label = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_ATYPE")))
    verify_input = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_CHK')

  agree_label.click()
  verify_input.click()

def main():
  login()

  # 計時
  while datetime.datetime.now() < target_time:
    sleep(0.5)

  choose_area()

main()