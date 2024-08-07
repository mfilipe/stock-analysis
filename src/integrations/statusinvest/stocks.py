from time import sleep
from ...base import get_webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tempfile
import pathlib
import pandas as pd
import locale

_DF_STOCKS = pd.DataFrame()

# dataframe de ações
with tempfile.TemporaryDirectory() as tmpdir:
  driver = get_webdriver(download_dir=tmpdir)
  driver.get('https://statusinvest.com.br/acoes/busca-avancada')

  driver.find_element(By.XPATH, '//*[@id="main-2"]/div[3]/div/div/div/button[2]').click()
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

def get_df_all():
  return _DF_STOCKS
