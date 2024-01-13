from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pyperclip
import pyautogui

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")
driver.maximize_window()    # 화면 최대화

# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, '#id')
id.click()
pyperclip.copy("wjdgus_0903")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

# 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR, '#pw')
pw.click()
pyperclip.copy("9193jane")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

# 로그인 버튼
driver.find_element(By.CSS_SELECTOR, '#log\.login').click()
