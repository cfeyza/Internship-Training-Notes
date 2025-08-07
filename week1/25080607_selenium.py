#Selenium bir web otomayson kütüphanesidir, selenium ile bir web sitesini ziyaret edip etkileşimde bulunabiliriz
#Driver hangi tarayıcı ile çalıştığımızı belirten exe dosyası, selenium siteyi bir tarayıcı üzerinden açmak zorunda
"""
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/FEYZA/Downloads/chrome-win64/chrome.exe")

url = "https://www.imdb.com/"
driver.get(url)

"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # <-- eksik olan bu satırdı
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.imdb.com/")

time.sleep(2)
driver.maximize_window()
driver.save_screenshot("ss.png")

url = "http://github.com/sadikturan"
driver.get(url)
time.sleep(2)
driver.back()
print(driver.title)
if "sadikturan" in driver.title:
    driver.save_screenshot("github-sadikturan.png")
time.sleep(2)
driver.forward()
time.sleep(2)
driver.close()