import pandas as pd

pesquisa_de_satisfacao = pd.DataFrame({
    'bom': [50, 21, 100],
    'ruim': [131, 2, 30],
    'pessimo': [30, 20, 1]
}, index=['XboxOne', 'Playstation4', 'Switch'])

#print(pesquisa_de_satisfacao)# imprime tudo

#print(pesquisa_de_satisfacao.head())# imprimi as 5 primeiras linhas quando nao tem nada nos parametros

#print(pesquisa_de_satisfacao.info())# exibi um resumo conciso, mas informativo, sobre o DataFrame

#print(pesquisa_de_satisfacao.columns)# exibe os nomes das colunas

#print(type(pesquisa_de_satisfacao))# exibe o tipo do objeto

#print(type(pesquisa_de_satisfacao.columns))# exibe o tipo do objeto associado aos nomes das colunas do DataFrame

#print(list(pesquisa_de_satisfacao))# converte os nomes das colunas em uma lista de strings

#print(list(pesquisa_de_satisfacao.columns))# retorna os nomes das colunas como uma lista de strings

# pesquisa_de_satisfacao_renomeado = pesquisa_de_satisfacao.rename(columns={
#     'bom': 'Muito bom',
#     'ruim': 'Muito ruim',
#     'pessimo': 'Muito pessimo'
# })# renomeia as colunas

#print(pesquisa_de_satisfacao_renomeado)

pesquisa_de_satisfacao_renomeado = pesquisa_de_satisfacao.rename(columns={
    'bom': 'Muito bom',
    'ruim': 'Muito ruim',
    'pessimo': 'Muito pessimo'
}, inplace=True)# modifica as colunas, os nomes das colunas sao alterados diretamente no DataFrame original.

print(pesquisa_de_satisfacao)

#print(pesquisa_de_satisfacao.columns)# exibe os nomes das colunas

#pesquisa_de_satisfacao.columns = ['MUITO BOM', 'MUITO RUIM', 'MUITO PESSIMO']#as colunas são renomeadas diretamente
# no próprio DataFrame

#print(pesquisa_de_satisfacao)

#print(pesquisa_de_satisfacao['Muito bom'])# imprime a String da coluna com o rótulo 'Muito bom',ela exibirá todos os
# valores presentes nessa coluna

#print(pesquisa_de_satisfacao.Muito_bom)# imprime o atributo da coluna com o rótulo 'Muito bom',ela exibirá todos os
# valores presentes nessa coluna, e o nome da coluna contiver espaços ou caracteres especiais, a notação de ponto
# não funcionará, pois não é válida em nomes de atributos

#print(pesquisa_de_satisfacao.iloc[1])# irá imprimir a linha de índice 1, iloc é usado para indexação baseada
# em posição, em vez de rótulos de índice

#print(type(pesquisa_de_satisfacao.iloc[1]))# imprimirá o tipo de objeto retornado pelo método iloc[1]

#print(pd.Series([10, 8.0, 0.4]))# cria e imprime um objeto do tipo pandas.Series

print(pd.Series([10.0, 8.0, 0.4], index=['Red dead Redemption', 'Burnout Revenge', 'Umbrella Corps'], name='Jogos'))
# estamos criando uma série a partir de uma lista de valores [10.0, 8.0, 0.4] e especificando os rótulos dos índices
# como 'Red dead Redemption', 'Burnout Revenge' e 'Umbrella Corps'. O parâmetro name='Jogos' define o
# nome da série como 'Jogos'.

avaliacao_view = pesquisa_de_satisfacao['Muito pessimo']# cria uma nova variável chamada avaliacao_view,
# que é uma série do Pandas contendo os valores da coluna 'Muito pessimo'

#print(avaliacao_view)

melhor_avaliacao_copy_bkp = pesquisa_de_satisfacao['Muito bom'].copy()# retorna uma copia da coluna 'Muito bom'

print (melhor_avaliacao_copy_bkp)