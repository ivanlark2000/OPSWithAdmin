import os
import time
import requests
from dotenv import load_dotenv
from urllib import request
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib import request
from fake_useragent import UserAgent
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv(override=True)
pas_avito = os.environ.get('pas_avito')
tel = os.environ.get('tel_avito')
url = {
    'url_login': "https://www.avito.ru/#login?authsrc=h",
    'url': "https://www.avito.ru/user/03af7c01efdf2dbc8e4721b2dae816c7/profile?id=1974589192&src=item&page_from=from_item_card&iid=1974589192"
}
options = webdriver.ChromeOptions()
ua = UserAgent()
userAgent = ua.random
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
# options.add_argument("--headless")
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument(f'user-agent={userAgent}')
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.add_cookie()
driver.refresh()
driver.get("https://m.avito.ru/#login")
driver.execute_script("window.scrollTo(0, 2080)")  # прокрутка
time.sleep(20)
driver.execute_script("window.scrollTo(0, 2080)")  # прокрутка прокручиваем вниз страницы
time.sleep(3)
html = driver.page_source  # получаем html страницы



