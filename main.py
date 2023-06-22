import pandas as pd
from flask import Flask, jsonify


App = Flask(__name__)


tabela = pd.read_csv('tabela.csv')


@App.route('/')
def index():
  dados = {
        'linhas': tabela.to_dict('records'),
        'colunas': list(tabela.columns)
    }
  return jsonify(dados)

  
@App.route('/vendas')
def vendas():
  totalvendas = tabela['Vendas'].sum()
  total = {'totalvendas': totalvendas}
  mediavendas = tabela['Vendas'].mean()
  media = {'mediavendas' : mediavendas}
  maxvendas = tabela['Vendas'].max()
  maximo = {'maxvendas' : maxvendas}
  minvendas = tabela['Vendas'].min()
  minimo = {'minvendas' : minvendas}
  
  return jsonify(total, media, maximo, minimo)


@App.route('/TV')
def tv():
  qtdTV = tabela['TV'].sum()
  qtd = {'qtdTV': qtdTV}
  descricao = tabela['TV'].var()
  desc = {'descricao' : descricao}
  return jsonify(qtd, desc)


#@App.route('/radio')

#@App.route('/jornal')



App.run(host='0.0.0.0')