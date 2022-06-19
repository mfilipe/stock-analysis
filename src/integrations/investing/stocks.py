import investpy
import pandas as pd
import pkg_resources

_DF_STOCKS = pd.DataFrame()

_resource_package = 'investpy'
_resource_path = '/'.join((('resources', 'stocks.csv')))
if pkg_resources.resource_exists(_resource_package, _resource_path):
  _DF_STOCKS = pd.read_csv(
    pkg_resources.resource_filename(_resource_package, _resource_path),
    keep_default_na=False,
  )
else:
  raise FileNotFoundError("investpy stocks não encontrado")

def get_all():
  return _DF_STOCKS