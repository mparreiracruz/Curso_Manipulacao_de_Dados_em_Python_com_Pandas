import pandas as pd
#carregando o dataset corretamente ==> neste caso, use o separdor ';'
data = pd.read_csv('/Users/matheus/Downloads/GasPricesinBrazil_2004-2019.csv', sep=';')

#print(data)
#print(data.head())
#print(data.info())
#print(type(data))
#print(data.shape)
# print(f'O DataFrame possui {data.shape[0]} linhas/observações/registros e {data.shape[1]} colunas/atributos/variáveis.')


# personagens_df = pd.DataFrame({
# 'nome': ['Luke Skywalker', 'Yoda', 'Palpatine'],
# 'idade': [16, 1000, 70],
# 'peso' : [70.5, 15.2, 60.1],
# 'eh Jedi' :[True, True, False]
# })


#print(personagens_df)
#print(personagens_df.info())
#print(personagens_df.columns)
#print(type(personagens_df.columns))
#print(list(personagens_df.columns))

#print(personagens_df)
# personagens_df_renomeado = personagens_df.rename(columns={
#     'nome': 'Nome Completo',
#     'idade': 'Idade'
# })

#print(personagens_df_renomeado)
# personagens_df.rename(columns={'nome': 'Nome Completo','idade': 'Idade'}, inplace=True)
#
# print(personagens_df.columns)
#
# personagens_df.columns = ['NOME', 'IDADE', 'PESO', 'EH JEDI']
#
# print(personagens_df)

# print(data.head())
#print(data['ESTADO'])

#print(data.ESTADO)

#print(type(data['ESTADO']))

#print(data.iloc[1])

#print(type(data.iloc[1]))

#print(pd.Series([5.5, 6.0, 9.5]))

#print(pd.Series([5.5, 6.0, 9.5], index=['prova 1', 'prova 2', 'projeto'], name='Notas do Luke Skywalker'))

#print(data)

# print(data['PRODUTO']) # a series retornada a coluna, NAO É UMA CÓPIA, mas sim, uma REFERENCIA/VIEW a coluna do dataFrame

#produto_view = data['PRODUTO']
# print(produto_view)

#produto_copy_bkp = data['PRODUTO'].copy()#retorna uma copia da coluna 'PRODUTO'
# print(produto_copy_bkp)

# data['PRODUTO'] = 'Combustível' #atribuindo o valor constante 'Combustível'para linha do dataframe na coluna 'PRODUTO'
# #print(data.head())
# print(data['PRODUTO'])
# print(produto_copy_bkp)

#nrows, ncols = data.shape

#print(nrows, ncols)

#novos_produtos = [f'Produto {i}' for i in range(nrows)]
#print(novos_produtos)

#print(len(novos_produtos))
# a quantidade de elementos da lista 'novos_produtos' é igual ao número de linhas do dataframe
#data['PRODUTO'] = novos_produtos
#print(data)

# print(produto_view)
# print('\n')
# print(produto_copy_bkp)

# voltando para os produtos originais
#data['PRODUTO'] = produto_copy_bkp

#print(data)

# criando uma coluna a partir de um valor constante/default
# todas as linhas terao o mesmo valor para esta nova coluna

data['coluna sem nocao'] = 'DEFAULT'
#print(data)

data['coluna a partir de lista'] = range(data.shape[0])
#print(data)
# nao funciona porque a quantidade de elementos da lista (a serem atribuídos a nova coluna) é diferente
# da quantidade de linhas do dataframe
#data['nao funciona'] = [1, 2, 3]

#print(data.head())

data['PREÇO MÉDIO REVENDA (dólares)'] = data['PREÇO MÉDIO REVENDA'] * 6.0
#print(data)
#-----------------------------------09_Indices-----------------------------------
#print(data.index)

pesquisa_de_satisfacao = pd.DataFrame({
    'bom': [50, 21, 100],
    'ruim': [131, 2, 30],
    'pessimo': [30, 20, 1]
}, index=['XboxOne', 'Playstation4', 'Switch'])

#print(pesquisa_de_satisfacao.head())
#print(pesquisa_de_satisfacao.index)

#-----------------------------------10_selecao_por_Indices-----------------------------------

#print(data.head())
# selecionando a linha 1 ===> observaçao do índice [1] do dataframe
#print(data.iloc[1])

#Selecionando múltiplas observaçoes/linhas:

# selecionando as linhas de índice de 0 a 5 (incluso)
#print(data.iloc[:6])

# Selecinando as linhas de índice de 10 a 15 (16)
#print(data.iloc[10:16])

# selecionando as linhas/observaçoes de índice 1, 5, 10, 15
#print(data.iloc[[1, 5, 10, 15]])

# selecionando as linhas/observaçoes de índices 5, 1, 15, 10
#print(data.iloc[[5, 1, 15, 10]])
#parei em 7:30 no video

# print(data.iloc[1, 4])

#-----------------------------------11_Selecao_por_Labels-----------------------------------

#iloc: passa índices numéricos
#loc: passa labels das colunas e linhas

#print(pesquisa_de_satisfacao.iloc[0])# retorna a linha de índice 0 (implicito) ===> usando o iloc

#print(pesquisa_de_satisfacao.iloc[0, 1])

#print(pesquisa_de_satisfacao.loc['XboxOne'])# retorna a linha cujo rótulo do índice é 'XboxOne'

# print(pesquisa_de_satisfacao)
#
# print(pesquisa_de_satisfacao.loc['Playstation4', 'ruim'])
#
# print(pesquisa_de_satisfacao.loc[['XboxOne', 'Switch']])

#print(pesquisa_de_satisfacao.loc[:, ['bom', 'pessimo']])

# print(pesquisa_de_satisfacao)
#
# print(pesquisa_de_satisfacao.iloc[0, 2])
#
# print(pesquisa_de_satisfacao.loc['XboxOne', 'pessimo'])

#-----------------------------------12_Selecao_de_Colunas_Atributos-----------------------------------

# print(data.head())
#
# print(data['ESTADO'])# retorna a coluna/atributo 'ESTADO'

#print(data.ESTADO)

#print(data.loc[:, 'ESTADO'])

# a forma de acesso de colunas por .NOME_DA_COLUNA só funciona se o .NOME_DA_COLUNA
#nao possuir carecteres invalidos(espaços, acentos, cedilhas, ...)
# não funciona
#print(data.DATA INCIAL)
# para colunas cujos rótulos possuem caracteres inválidos, apenas a seleção via string é válida
#print(data['DATA INICIAL'])

#print(data[['PRODUTO', 'ESTADO', 'REGIÃO']])# selecionando múltiplas colunas

#-----------------------------------13_Salvando_um_Dataset-----------------------------------

#print(data.head())

del data['Unnamed: 0']# deleta/remove-in-place (ou seja, no próprio dataframe) a coluna de rótulo 'Unnamed: 0'

#print(data.head())

# vamos agora remover as colunas fictícias criadas no vídeos para estudo.

del data['coluna sem nocao']
del data['coluna a partir de lista']
del data['PREÇO MÉDIO REVENDA (dólares)']

#print(data)

'''
Salvando um Data Frame

Para salvarmos um Data Frame para um arquivo CSV, basta usarmos o método .to_csv.
Por padrão, esse método salva os íncices da tabela como uma coluna no CSV.
Como no geral tais índices são números de 0 a n-1, não há necessidade para isso (veja que removemos a coluna 'Unnamed: 0' que foi
justamente esse caso).
Desta forma, utlilize o parâmetro: index=False.

Por padrão, o método utilizará a ',' como separador das colunas. Caso queira alterá-lo utilize o parâmetro sep.
'''

data.to_csv('/Users/matheus/Downloads/GasPricesinBrazil_2004-2019_preprocessado.csv', index=False)

data.to_csv('/Users/matheus/Downloads/GasPricesinBrazil_2004-2019_preprocessado.csv', index=False)

#-----------------------------------14_Filtragem_Parte_01-----------------------------------
'''
Seleção Condicional: Filtrando amostras

Durante nossas análises exploratórias, frequentemente filtraremos nossas amostras, a partir de certas condições, 
para fins de análise mais específica. Existem algumas maneiras de fazermos tal filtragem. Antes disso, vamos carregar
nosso dataset pré-processado que salvamos no item anterior.
'''


data = pd.read_csv('/Users/matheus/Downloads/GasPricesinBrazil_2004-2019_preprocessado.csv')

#print(data.head())

#print(data['ESTADO'].unique())# Mostra todos os estados cujos preços dos combustíveis foram aferidos
# Mais tecnicamente, mostra os valores únicos presentes para o atributo/coluna 'ESTADO'
'''
Selecionando apenas os preços dos Postos de São Paulo
==> Alternativa 1: Seleção Condicional(Comparações diretas)
O código abaixo retorna uma Series ('array') de booleans, com o número de linhas (amostras) do Data Frame,
que informa os registros de preços dos postos do estado de São Paulo(True).
'''

#print(data['ESTADO'] == 'SAO PAULO')# Faz uma comparação elemento a elemento da series, retornando uma Series
#de booleans

# Salvando essa Series de booleans em uma variável
selecao = data['ESTADO'] == 'SAO PAULO'

# print(selecao)
#
# print(type(selecao))

print(selecao.shape)

print(data.shape)

# Fazendo a filtragem dos registros do estado de São Paulo
print(data[selecao])# O resultado é um Data Frame com apenas os registros desejados após a filtragem

print(data.loc[selecao])# Podemos ainda utilizar o método "loc" para o mesmo fim
