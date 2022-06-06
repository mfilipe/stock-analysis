# stock-analysis

Cria um relatório CSV com indicadores para a minha análise fundamentalista das ações. Alguns dos indicadores disponíveis:

- Earnings yield
- Magic Formula
- Preço-teto (Método Barsi)

Somente ações da B3 estão disponíveis. Os dados são da [StatusInvest](https://statusinvest.com.br), entretanto a ideia é que seja simples implementar a integração com qualquer outra fonte de dados.

## Requerimentos

- Google Chrome
- Python 3.9+
- `$ pip install -r requirements.txt`

## Executar

`$ python main.py TICKER[ TICKER]... # output.csv`