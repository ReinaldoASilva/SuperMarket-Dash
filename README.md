# SuperMarket-Dash

## Bibliotecas

- dash==2.7.0
- dash-bootstrap-components==1.5.0
- dash-bootstrap-templates==1.1.1
- dash-core-components==2.0.0
- dash-html-components==2.0.0
- dash-table==5.0.0
- gunicorn==20.1.0
- numpy==1.20.0
- pandas==1.3.0
- plotly==5.5.0

## Código

### Inicialização do projeto

Descrição Simples:

Este é o coração do nosso projeto! Aqui, criamos o nosso aplicativo mágico usando a biblioteca Dash. Além disso, preparamos nossos dados de vendas de supermercado para uma análise incrível. 🛒✨

- O que Este Código Faz:

- Inicializa o aplicativo Dash com um estilo visual encantador.
- Prepara nosso servidor para a mágica acontecer.
- Em seguida, importamos os dados de vendas de um arquivo CSV chamado "supermarket_sales.csv" e realizamos algumas ações mágicas:
- Verificamos informações sobre os dados.
- Descobrimos quais cidades estão em nossos dados.
- Transformamos a coluna de data em um formato de data.
- A partir daqui, nossa jornada mágica de análise de vendas começa! ✨📊

  - app = dash.Dash(external_stylesheets=[dbc.themes.MINTY])
  - server = app.server
  - data = pd.read_csv("supermarket_sales.csv")
  - data.info()
  - data["City"].value_counts().index
  - data["Date"] = pd.to_datetime(data["Date"])
