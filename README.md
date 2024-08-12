# stock-analysis

Cria um relatório CSV com indicadores para apoio da minha análise fundamentalista das ações. Alguns dos indicadores presentes:

- Earnings Yield
- Magic Formula
- Preço Teto
- Dividend on Cost

Somente ações da B3 estão disponíveis. Os dados são da [Investing](https://investing.com/) e [StatusInvest](https://statusinvest.com.br), entretanto a ideia é que seja simples implementar a integração com qualquer outra fonte de dados.

## Requerimentos

- Google Chrome
- Python 3.10+ (recomendo [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv))
- `$ pip install -r requirements.txt`

## Executar

`$ python main.py TICKER[ TICKER]... # output.csv`
