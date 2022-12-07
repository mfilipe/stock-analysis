from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
import logging
import sys
import locale
import requests

locale.setlocale(locale.LC_NUMERIC, '')

logging.basicConfig(stream=sys.stdout, level=logging.INFO, 
                    format='[%(asctime)s] [%(module)s] %(levelname)s: %(message)s')

def get_webdriver(prefs={}):
  options = webdriver.ChromeOptions()
  # options.add_argument("--headless")
  options.add_experimental_option('prefs', prefs)

  return webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)

UA = UserAgent(use_external_data=True)

def make_request(url):
  return requests.get(url, headers={'User-Agent': UA.chrome})