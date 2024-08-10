from flask import render_template
import plotly
import plotly.express as px
import plotly.graph_objects as go
import json
import pandas as pd


def graficoReceita():
  tabela = pd.read_csv('FluxoCaixa.csv')
  fig = px.bar(tabela, x='Tipo', y='Valor', title='Receitas')
  fig.write_image('images/grafico.png')
  graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

  return render_template('grafico.html',
                         nome_grafico='Total das Receitas e Despesas das empresas', 
                         graph_json=graph_json)


def graficoReceitaEmp():
  tabela = pd.read_csv('FluxoCaixa.csv', parse_dates=['Data'])
  fig = px.bar(tabela,
               x='Tipo',
               y='Valor',
               color='Empresa',
               barmode='group',
               title='Gráfico de Barras por Empresa e Tipo')
  fig.write_image('images/grafico.png')
  
  graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

  return render_template('grafico.html',
                         nome_grafico='Total das Receitas por Empresa',
                         graph_json=graph_json)


def graficoLinha(IDEmpresa):
  tabela = pd.read_csv('FluxoCaixa.csv', parse_dates=['Data'])
  #tabela['Data'] = pd.to_datetime(tabela['Data'])
  df = tabela.sort_values(by='Data')
  # Agrupar por data e somar os valores
  #df = tabela.groupby('Data').sum().reset_index()

  df_Emp = df[df['Empresa'] == 'Empresa ' + IDEmpresa]

  fig = px.line(df_Emp,
                x='Data',
                y='Valor',
                color='Tipo',
                title='Fluxo de Caixa')
  fig.write_image('images/grafico.png')
  
  graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

  return render_template('grafico.html',
                         nome_grafico='Fluxo de Caixa da Empresa ' + IDEmpresa,
                         graph_json=graph_json)


def graficoValores(ID_Empresa, tipo):
  tabela = pd.read_csv('FluxoCaixa.csv', parse_dates=['Data'])

  sTitulo = ''
  if tipo == 'E':
    df = tabela[tabela['Tipo'] == 'Entrada']
    sTitulo = 'Receitas'
  else:
    df = tabela[tabela['Tipo'] == 'Saida']
    sTitulo = 'Despesas'

  if ID_Empresa == '1':
    df1 = df[tabela['Empresa'] == 'Empresa 1']
    sTitulo = sTitulo + ' da Empresa 1'
  elif ID_Empresa == '2':
    df1 = df[tabela['Empresa'] == 'Empresa 2']
    sTitulo = sTitulo + ' da Empresa 2'
  else:
    df1 = df
    sTitulo = sTitulo + ' de todas as Empresas'
    
  fig = px.bar(
      df1,
      x='Valor',
      y='Conta',
      #color='Empresa',
      orientation='h',
      barmode='group',
      title='Gráfico de Barras por Empresa e Tipo')
  
  fig.write_image('images/grafico.png')
  graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

  return render_template('grafico.html',
                         nome_grafico='Total das ' + sTitulo,
                         graph_json=graph_json)
