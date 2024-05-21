import pandas as pd

pesquisa_de_satisfacao = pd.DataFrame({
    'bom': [2, 10, 50, 21, 100],
    'ruim': [5, 30, 131, 2, 30],
    'pessimo': [4, 40, 30, 20, 1]
}, index=['Playstation2', 'Nintendo64', 'XboxOne', 'Playstation4', 'Switch'])

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

#print(pesquisa_de_satisfacao)

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

#print(pd.Series([10.0, 8.0, 0.4], index=['Red dead Redemption', 'Burnout Revenge', 'Umbrella Corps'], name='Jogos'))
# estamos criando uma série a partir de uma lista de valores [10.0, 8.0, 0.4] e especificando os rótulos dos índices
# como 'Red dead Redemption', 'Burnout Revenge' e 'Umbrella Corps'. O parâmetro name='Jogos' define o
# nome da série como 'Jogos'.

avaliacao_view = pesquisa_de_satisfacao['Muito pessimo']# cria uma nova variável chamada avaliacao_view,
# que é uma série do Pandas contendo os valores da coluna 'Muito pessimo'

#print(avaliacao_view)

melhor_avaliacao_copy_bkp = pesquisa_de_satisfacao['Muito bom'].copy()# retorna uma copia da coluna 'Muito bom'

pesquisa_de_satisfacao['Muito bom'] = 'Melhores'# substitui os valores na coluna 'Muito bom' por 'Melhores'

#print(pesquisa_de_satisfacao['Muito bom'])# imprimi os valores 'Melhores' relacionados a cada produto

nrows, ncols = pesquisa_de_satisfacao.shape# Obtendo o número de linhas e colunas, usa-se shape para obter o número
# de linhas (nrows) e colunas (ncols)

#print(nrows, ncols)

novos_resultados = [f'Muito bom{i}' for i in range(nrows)]# Cria-se uma lista novos_resultados, onde cada elemento é
# uma string 'Muito bom' seguida por um índice (i), variando de 0 até o número de linhas menos 1.

#print(novos_resultados)

#print(len(novos_resultados))# retorna o número de elementos na lista

pesquisa_de_satisfacao['Muito bom'] = novos_resultados# a coluna 'Muito bom' foi atualizada com os novos
# valores da lista novos_resultados.
#print(pesquisa_de_satisfacao)

# print(avaliacao_view)
# print('\n')
# print(melhor_avaliacao_copy_bkp)
# print('\n')
# print(pesquisa_de_satisfacao)

pesquisa_de_satisfacao['Muito bom'] = melhor_avaliacao_copy_bkp# voltando para os produtos originais

#print(pesquisa_de_satisfacao)

# criando uma coluna a partir de um valor constante/default

pesquisa_de_satisfacao['Jogos'] = 'DEFAULT'# criando uma coluna a partir de um valor constante/default
# todas as linhas terao o mesmo valor para esta nova coluna

# print(pesquisa_de_satisfacao)
#
# print(pesquisa_de_satisfacao)

pesquisa_de_satisfacao['Colunas'] = range(pesquisa_de_satisfacao.shape[0])

precos_consoles = [100, 2000, 4000, 4500, 1300]# criando valores para a coluna precos

pesquisa_de_satisfacao['precos'] = precos_consoles# criando a coluna precos com os valores acima

#print(pesquisa_de_satisfacao)

pesquisa_de_satisfacao['PREÇO MÉDIO REVENDA'] = [20, 400, 500, 600, 700]

pesquisa_de_satisfacao['PREÇO MÉDIO REVENDA (dólares)'] = pesquisa_de_satisfacao['PREÇO MÉDIO REVENDA'] * 6.0

#print(pesquisa_de_satisfacao)

#print(pesquisa_de_satisfacao.index)

# print(pesquisa_de_satisfacao)
#
# print(pesquisa_de_satisfacao.iloc[1])# selecionando a linha 1 ===> observaçao do índice [1] do dataframe

#Selecionando múltiplas observaçoes/linhas:

# print(pesquisa_de_satisfacao.iloc[:3])# selecionando as linhas de índice de 0 a 3 (incluso)
#
# print(pesquisa_de_satisfacao.iloc[0:2])# Selecinando as linhas de índice de 0 a 2 (incluso)

print(pesquisa_de_satisfacao.iloc[[1, 4]])# selecionando as linhas/observaçoes de índice 1 e 4

print(pesquisa_de_satisfacao.iloc[[0, 2, 4]])# selecionando as linhas/observaçoes de índices 0, 2 e 4
#parei em 7:30 no video
