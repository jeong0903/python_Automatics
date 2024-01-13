from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://www.naver.com")