import pandas as pd
#carregando o dataset corretamente ==> neste caso, use o separdor ';'
data = pd.read_csv('/Users/matheus/Downloads/GasPricesinBrazil_2004-2019.csv', sep=';')

def print_full(df):
    # Salvando as configurações atuais
    pd.set_option('display.max_rows', None)  # Exibir todas as linhas
    pd.set_option('display.max_columns', None)  # Exibir todas as colunas
    pd.set_option('display.max_colwidth', None)  # Exibir conteúdo completo das colunas
    pd.set_option('display.width', None)  # Ajustar largura de exibição

    # Imprimindo o DataFrame
    print(df)

    # Restaurando as configurações padrão após a exibição
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')
    pd.reset_option('display.max_colwidth')
    pd.reset_option('display.width')

print_full(data.head())

#print(data)

#print(data.head())
#print(data.info())

