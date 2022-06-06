from time import sleep
from ...base import get_webdriver, locale, By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tempfile
import pathlib
import pandas as pd

_DF_STOCKS = pd.DataFrame()

# dataframe de ações
with tempfile.TemporaryDirectory() as tmpdir:
  driver = get_webdriver(prefs={'download.default_directory': tmpdir})
  driver.get('https://statusinvest.com.br/acoes/busca-avancada')

  # popup
  # WebDriverWait(driver, timeout=30).until(
  #   EC.element_to_be_clickable((By.XPATH, '/html/body/div[12]/div/div/div[1]/button'))
  # ).click()
  # buscar 
  # WebDriverWait(driver, timeout=30).until(
  #   EC.element_to_be_clickable((By.XPATH, '//*[@id="main-2"]/div[3]/div/div/div/button[2]'))
  # ).click()
  sleep(2)
  driver.find_element(By.XPATH, '//*[@id="main-2"]/div[3]/div/div/div/button[2]').click()
  # download
  driver.execute_script("arguments[0].click();", WebDriverWait(driver, timeout=5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="main-2"]/div[4]/div/div[1]/div[2]/a'))
  ))

  sleep(2)
  _DF_STOCKS = pd.read_csv(str(next(pathlib.Path(tmpdir).glob('*.csv'))), sep=';', on_bad_lines='skip')
  
  driver.close()

force_to_float = ['PRECO', 'DY', 'ROE', 'ROIC', ' LPA']
convert_func = lambda x: locale.atof(x) if not isinstance(x, float) else x
for column in force_to_float:
  _DF_STOCKS[column] = _DF_STOCKS[column].apply(convert_func)
_DF_STOCKS[force_to_float] = _DF_STOCKS[force_to_float].astype(float)

def get_stocks_df():
  return _DF_STOCKS