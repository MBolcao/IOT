from flask import Flask
from flask.templating import render_template

import grafico as gr
import graficoEmail as em


app = Flask(__name__ )

@app.route('/')
def homepage():
  return render_template("index.html")

@app.route('/graficoReceita')
def graficoReceita():  
  return gr.graficoReceita()
  
@app.route('/graficoReceitaEmp')
def graficoReceitaEmp():  
  return gr.graficoReceitaEmp()

@app.route('/Linha/<ID_Empresa>')
def Linha(ID_Empresa):  
  return gr.graficoLinha(ID_Empresa)

@app.route('/Valores/<ID_Empresa>/<tipo>')
def Valores(ID_Empresa,tipo):  
  return gr.graficoValores(ID_Empresa,tipo)

@app.route('/enviarEmail/<endereco>')
def enviarEmail(endereco):  
  return em.enviarEmail(endereco)

#Rodando a API
app.run(host='0.0.0.0')

