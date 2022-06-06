from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging
import sys
import locale

locale.setlocale(locale.LC_NUMERIC, '')

logging.basicConfig(stream=sys.stdout, level=logging.INFO, 
                    format='[%(asctime)s] [%(module)s] %(levelname)s: %(message)s')

def get_webdriver(prefs={}):
  options = webdriver.ChromeOptions()
  # options.add_argument("--headless")
  options.add_experimental_option('prefs', prefs)

  return webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)