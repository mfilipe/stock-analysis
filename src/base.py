import undetected_chromedriver as uc
from fake_useragent import UserAgent
import logging
import sys
import locale
import requests

locale.setlocale(locale.LC_NUMERIC, '')

logging.basicConfig(stream=sys.stdout, level=logging.INFO, 
                    format='[%(asctime)s] [%(module)s] %(levelname)s: %(message)s')

def get_webdriver(download_dir=None):
  options = uc.ChromeOptions()
  if download_dir:
    options.add_experimental_option('prefs', {'download.default_directory': download_dir})

  return uc.Chrome(options=options)

UA = UserAgent()

def make_request(url):
  return requests.get(url, headers={'User-Agent': UA.chrome})
