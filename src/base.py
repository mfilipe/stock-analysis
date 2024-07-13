from selenium import webdriver
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
  options.add_experimental_option('prefs', prefs)

  return webdriver.Chrome(options=options)

UA = UserAgent()

def make_request(url):
  return requests.get(url, headers={'User-Agent': UA.chrome})
