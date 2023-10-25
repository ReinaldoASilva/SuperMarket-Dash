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

## Deploy 

https://render.com/

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





### Configuração do Layout do App

Aqui, nós moldamos a aparência do nosso aplicativo mágico! Utilizando o Dash e Dash Bootstrap Components, criamos um layout incrível para a nossa análise de vendas. 📈✨

- O que Este Código Faz:

- Configura um painel com várias seções, organizadas de forma encantadora.
- Apresenta informações-chave sobre nossos dados de vendas de supermercado.
- Oferece opções interativas para explorar as cidades e variáveis de análise.
- Exibe gráficos mágicos que revelam insights sobre nossos dados.
- Nosso aplicativo é agora uma janela para o mundo das análises de vendas! 🪄😊
      
        app.layout =  html.Div(children=[
                 dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            html.H2("RBlack", style={"font-family": "Voltaire", "font-size": "60px"}),
                            html.Hr(),

                            html.H5("Cities:"),
                            dcc.Checklist(data["City"].value_counts().index,
                            data["City"].value_counts().index, id="check_city",
                            inputStyle={"margin-right": "5px", "margin-left": "20px"}),
                            html.Hr(),
                            html.H5("Analysis Variable"),
                            dcc.RadioItems(["gross income", "Rating"], "gross income", id="main_variable",
                            inputStyle={"margin-right": "5px", "margin-left": "20px"}),

                        ], style={"height":"90vh", "margin":"20px", "padding":"20px"})

                    ], sm=2),

                    dbc.Col([
                        dbc.Row([
                            dbc.Col([dcc.Graph(id="city_fig"),],sm=4),
                            dbc.Col([dcc.Graph(id="gender_fig"),],sm=4),
                            dbc.Col([dcc.Graph(id="pay_fig"),],sm=4)
                        ]),
                        dbc.Row([dcc.Graph(id="income_per_date_fig")]),
                        dbc.Row([dcc.Graph(id="income_per_product_fig")])

                    ], sm=10)

                ])
            
            ]

        )


### Callbacks Mágicos

Aqui estão os feitiços que tornam nosso aplicativo verdadeiramente mágico! Esses callbacks, criados com o Dash, reagem às escolhas do usuário e geram gráficos incríveis. 🪄📊

O que Este Código Faz:

- Recebe escolhas do usuário, como cidades e variáveis principais.
- Filtra os dados com base nas escolhas.
- Calcula estatísticas mágicas, como soma ou média, dependendo da variável principal.
- Cria gráficos mágicos que revelam insights com base nas escolhas do usuário.
- Os gráficos gerados são uma janela para a compreensão de nossos dados e revelam segredos sobre nossas vendas de supermercado. 🌟😊

            @app.callback([
                    Output("city_fig", "figure"),
                    Output("gender_fig", "figure"),
                    Output("pay_fig", "figure"),
                    Output("income_per_date_fig", "figure"),
                    Output("income_per_product_fig", "figure")
    
                ],
    
                    [
                        Input("check_city", "value"),
                        Input("main_variable", "value")
    
                    ])
        def render_graph(cities, main_variable):
        operation = np.sum if main_variable == "gross income" else np.mean
        data_filtered = data[data["City"].isin(cities)]
        data_city = data_filtered.groupby("City")[main_variable].apply(operation).to_frame().reset_index()
        data_gender = data_filtered.groupby(["Gender", "City"])[main_variable].apply(operation).to_frame().reset_index()
        data_payment = data_filtered.groupby("Payment")[main_variable].apply(operation).to_frame().reset_index()
        data_product_time = data_filtered.groupby("Date")[main_variable].apply(operation).to_frame().reset_index()
        data_product_income = data_filtered.groupby(["Product line", "City"])[main_variable].apply(operation).to_frame().reset_index()
    
        fig_city = px.bar(data_city, x="City", y=main_variable)
        fig_payment = px.bar(data_payment, y="Payment", x=main_variable, orientation="h")
        fig_gender = px.bar(data_gender, y=main_variable,x="Gender", color="City",barmode="group")
        fig_product_income = px.bar(data_product_income, x= main_variable, y="Product line", color="City", orientation="h", barmode="group")
        fig_product_date = px.bar(data_product_time, y= main_variable, x="Date")
    
        for fig in [fig_city,fig_payment,fig_gender,fig_product_date]:
            fig.update_layout(margin=dict(l=0,r=0,t=20,b=20),height=200, template="minty")
        
        fig_product_income.update_layout(margin=dict(l=0,r=0,t=20,b=20),height=500)
        
        return fig_city, fig_gender, fig_payment,  fig_product_date, fig_product_income 


### Executando o Feitiço Final

Aqui está o toque final de magia! Ao executar esta parte do código, nosso aplicativo ganha vida e fica pronto para encantar. 🚀✨

O que Este Código Faz:

- Verifica se estamos executando o aplicativo como o principal ponto de entrada.
- Inicializa o servidor para o nosso aplicativo mágico.
- Prepara o aplicativo para ser acessado, sem mostrar detalhes mágicos durante o processo.
- Com esse feitiço, nosso aplicativo estará pronto para ser lançado no mundo e compartilhado com todos. A magia está prestes a acontecer! 🪄😊

          if __name__ == "__main__":
              app.run_server(debug=False)


    
