import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def carregar_dados(arquivo):
    """Carrega os dados históricos de ações de um arquivo CSV."""
    dados = pd.read_csv(arquivo, index_col='Date', parse_dates=True)
    return dados

def calcular_sma(dados, janela):
    """Calcula a média móvel simples."""
    sma = dados['Close'].rolling(window=janela).mean()
    return sma

def calcular_desvio_padrao(dados, janela):
    """Calcula o desvio padrão para o preço de fechamento."""
    desvio_padrao = dados['Close'].rolling(window=janela).std()
    return desvio_padrao

def identificar_sinais(dados, janela_sma, janela_desvio):
    """Identifica sinais de compra e venda com base na SMA e no desvio padrão."""
    dados['SMA'] = calcular_sma(dados, janela_sma)
    dados['DesvioPadrao'] = calcular_desvio_padrao(dados, janela_desvio)
    
    # Sinal de compra: Quando o preço fecha acima da SMA
    dados['SinalCompra'] = dados['Close'] > dados['SMA']
    
    # Sinal de venda: Quando o preço fecha abaixo da SMA
    dados['SinalVenda'] = dados['Close'] < dados['SMA']
    
    return dados

def visualizar_dados(dados):
    """Visualiza os dados junto com os sinais de compra e venda."""
    plt.figure(figsize=(14, 7))
    plt.plot(dados.index, dados['Close'], label='Preço de Fechamento', alpha=0.5)
    plt.plot(dados.index, dados['SMA'], label='Média Móvel Simples', alpha=0.75)
    plt.scatter(dados.index[dados['SinalCompra']], dados['Close'][dados['SinalCompra']], label='Compra', marker='^', color='green')
    plt.scatter(dados.index[dados['SinalVenda']], dados['Close'][dados['SinalVenda']], label='Venda', marker='v', color='red')
    plt.title('Análise de Ações')
    plt.xlabel('Data')
    plt.ylabel('Preço de Fechamento')
    plt.legend()
    plt.show()


arquivo_dados = 'caminho_para_seu_arquivo.csv'  # Substitua pelo caminho real do arquivo CSV
dados = carregar_dados(arquivo_dados)
dados_analisados = identificar_sinais(dados, janela_sma=20, janela_desvio=20)
visualizar_dados(dados_analisados)
