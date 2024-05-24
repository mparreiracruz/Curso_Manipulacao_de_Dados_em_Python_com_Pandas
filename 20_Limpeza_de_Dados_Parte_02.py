import pandas as pd

# carregando o dataset corretamente ==> neste caso, use o separdor ';'
data = pd.read_csv('/Users/matheus/Downloads/GasPricesinBrazil_2004-2019.csv', sep=';')

# print(data)
# print(data.head())
# print(data.info())
# print(type(data))
# print(data.shape)
# print(f'O DataFrame possui {data.shape[0]} linhas/observações/registros e {data.shape[1]} colunas/atributos/variáveis.')


# personagens_df = pd.DataFrame({
# 'nome': ['Luke Skywalker', 'Yoda', 'Palpatine'],
# 'idade': [16, 1000, 70],
# 'peso' : [70.5, 15.2, 60.1],
# 'eh Jedi' :[True, True, False]
# })


# print(personagens_df)
# print(personagens_df.info())
# print(personagens_df.columns)
# print(type(personagens_df.columns))
# print(list(personagens_df.columns))

# print(personagens_df)
# personagens_df_renomeado = personagens_df.rename(columns={
#     'nome': 'Nome Completo',
#     'idade': 'Idade'
# })

# print(personagens_df_renomeado)
# personagens_df.rename(columns={'nome': 'Nome Completo','idade': 'Idade'}, inplace=True)
#
# print(personagens_df.columns)
#
# personagens_df.columns = ['NOME', 'IDADE', 'PESO', 'EH JEDI']
#
# print(personagens_df)

# print(data.head())
# print(data['ESTADO'])

# print(data.ESTADO)

# print(type(data['ESTADO']))

# print(data.iloc[1])

# print(type(data.iloc[1]))

# print(pd.Series([5.5, 6.0, 9.5]))

# print(pd.Series([5.5, 6.0, 9.5], index=['prova 1', 'prova 2', 'projeto'], name='Notas do Luke Skywalker'))

# print(data)

# print(data['PRODUTO']) # a series retornada a coluna, NAO É UMA CÓPIA, mas sim, uma REFERENCIA/VIEW a coluna do dataFrame

# produto_view = data['PRODUTO']
# print(produto_view)

# produto_copy_bkp = data['PRODUTO'].copy()#retorna uma copia da coluna 'PRODUTO'
# print(produto_copy_bkp)

# data['PRODUTO'] = 'Combustível' #atribuindo o valor constante 'Combustível'para linha do dataframe na coluna 'PRODUTO'
# #print(data.head())
# print(data['PRODUTO'])
# print(produto_copy_bkp)

# nrows, ncols = data.shape

# print(nrows, ncols)

# novos_produtos = [f'Produto {i}' for i in range(nrows)]
# print(novos_produtos)

# print(len(novos_produtos))
# a quantidade de elementos da lista 'novos_produtos' é igual ao número de linhas do dataframe
# data['PRODUTO'] = novos_produtos
# print(data)

# print(produto_view)
# print('\n')
# print(produto_copy_bkp)

# voltando para os produtos originais
# data['PRODUTO'] = produto_copy_bkp

# print(data)

# criando uma coluna a partir de um valor constante/default
# todas as linhas terao o mesmo valor para esta nova coluna

data['coluna sem nocao'] = 'DEFAULT'
# print(data)

data['coluna a partir de lista'] = range(data.shape[0])
# print(data)
# nao funciona porque a quantidade de elementos da lista (a serem atribuídos a nova coluna) é diferente
# da quantidade de linhas do dataframe
# data['nao funciona'] = [1, 2, 3]

# print(data.head())

data['PREÇO MÉDIO REVENDA (dólares)'] = data['PREÇO MÉDIO REVENDA'] * 6.0
# print(data)
# -----------------------------------09_Indices-----------------------------------
# print(data.index)

pesquisa_de_satisfacao = pd.DataFrame({
    'bom': [50, 21, 100],
    'ruim': [131, 2, 30],
    'pessimo': [30, 20, 1]
}, index=['XboxOne', 'Playstation4', 'Switch'])

# print(pesquisa_de_satisfacao.head())
# print(pesquisa_de_satisfacao.index)

# -----------------------------------10_selecao_por_Indices-----------------------------------

# print(data.head())
# selecionando a linha 1 ===> observaçao do índice [1] do dataframe
# print(data.iloc[1])

# Selecionando múltiplas observaçoes/linhas:

# selecionando as linhas de índice de 0 a 5 (incluso)
# print(data.iloc[:6])

# Selecinando as linhas de índice de 10 a 15 (16)
# print(data.iloc[10:16])

# selecionando as linhas/observaçoes de índice 1, 5, 10, 15
# print(data.iloc[[1, 5, 10, 15]])

# selecionando as linhas/observaçoes de índices 5, 1, 15, 10
# print(data.iloc[[5, 1, 15, 10]])
# parei em 7:30 no video

# print(data.iloc[1, 4])

# -----------------------------------11_Selecao_por_Labels-----------------------------------

# iloc: passa índices numéricos
# loc: passa labels das colunas e linhas

# print(pesquisa_de_satisfacao.iloc[0])# retorna a linha de índice 0 (implicito) ===> usando o iloc

# print(pesquisa_de_satisfacao.iloc[0, 1])

# print(pesquisa_de_satisfacao.loc['XboxOne'])# retorna a linha cujo rótulo do índice é 'XboxOne'

# print(pesquisa_de_satisfacao)
#
# print(pesquisa_de_satisfacao.loc['Playstation4', 'ruim'])
#
# print(pesquisa_de_satisfacao.loc[['XboxOne', 'Switch']])

# print(pesquisa_de_satisfacao.loc[:, ['bom', 'pessimo']])

# print(pesquisa_de_satisfacao)
#
# print(pesquisa_de_satisfacao.iloc[0, 2])
#
# print(pesquisa_de_satisfacao.loc['XboxOne', 'pessimo'])

# -----------------------------------12_Selecao_de_Colunas_Atributos-----------------------------------

# print(data.head())
#
# print(data['ESTADO'])# retorna a coluna/atributo 'ESTADO'

# print(data.ESTADO)

# print(data.loc[:, 'ESTADO'])

# a forma de acesso de colunas por .NOME_DA_COLUNA só funciona se o .NOME_DA_COLUNA
# nao possuir carecteres invalidos(espaços, acentos, cedilhas, ...)
# não funciona
# print(data.DATA INCIAL)
# para colunas cujos rótulos possuem caracteres inválidos, apenas a seleção via string é válida
# print(data['DATA INICIAL'])

# print(data[['PRODUTO', 'ESTADO', 'REGIÃO']])# selecionando múltiplas colunas

# -----------------------------------13_Salvando_um_Dataset-----------------------------------

# print(data.head())

del data['Unnamed: 0']  # deleta/remove-in-place (ou seja, no próprio dataframe) a coluna de rótulo 'Unnamed: 0'

# print(data.head())

# vamos agora remover as colunas fictícias criadas no vídeos para estudo.

del data['coluna sem nocao']
del data['coluna a partir de lista']
del data['PREÇO MÉDIO REVENDA (dólares)']

# print(data)

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

# -----------------------------------14_Filtragem_Parte_01-----------------------------------
'''
Seleção Condicional: Filtrando amostras

Durante nossas análises exploratórias, frequentemente filtraremos nossas amostras, a partir de certas condições, 
para fins de análise mais específica. Existem algumas maneiras de fazermos tal filtragem. Antes disso, vamos carregar
nosso dataset pré-processado que salvamos no item anterior.
'''

data = pd.read_csv('/Users/matheus/Downloads/GasPricesinBrazil_2004-2019_preprocessado.csv')

# print(data.head())

# print(data['ESTADO'].unique())# Mostra todos os estados cujos preços dos combustíveis foram aferidos
# Mais tecnicamente, mostra os valores únicos presentes para o atributo/coluna 'ESTADO'
'''
Selecionando apenas os preços dos Postos de São Paulo
==> Alternativa 1: Seleção Condicional(Comparações diretas)
O código abaixo retorna uma Series ('array') de booleans, com o número de linhas (amostras) do Data Frame,
que informa os registros de preços dos postos do estado de São Paulo(True).
'''

# print(data['ESTADO'] == 'SAO PAULO')# Faz uma comparação elemento a elemento da series, retornando uma Series
# de booleans

# Salvando essa Series de booleans em uma variável
selecao = data['ESTADO'] == 'SAO PAULO'

# print(selecao)
#
# print(type(selecao))

# print(selecao.shape)
#
# print(data.shape)

# Fazendo a filtragem dos registros do estado de São Paulo
# print(data[selecao])# O resultado é um Data Frame com apenas os registros desejados após a filtragem
#
# print(data.loc[selecao])# Podemos ainda utilizar o método "loc" para o mesmo fim

# -----------------------------------15_Filtragem_Parte_02-----------------------------------

# Alternativa 2: Utilizando o método "query"
# query filtra as linhas de um Data Frame baseado em um query (pergunta)

# print(data.head())

# print(data.query('ESTADO == "SAO PAULO"'))

postos_sp = data.query('ESTADO == "SAO PAULO"')  # Uma boa prática é salvar o Data Frame filtrado em uma nova variável.
# Isso simplifica a complexidade do código apar futurras análises  feitas para os postos de São Paulo (neste caso).

# print(postos_sp)

# print(type(postos_sp))
#
# print(postos_sp.shape)
#
# print(postos_sp.head())

'''
Resetando os índices

Note que os índices das linhas/registros após a filtragem continuam sendo os mesmos do Data Frame original.
Em muitas situações, manter esta informação será importante.

Mas, se voce quiser resetar os índices do Data Frame filtrado, fazendo com que os registros começem com índice 0 até 
num_linhas-1, use o método .reset_index. 
'''

# print(postos_sp)
#
# print(postos_sp.reset_index(drop=True))

# print(postos_sp)# Ainda não foi alterado, precisamos usar o atributo/parametro "inplace=True"

# print(postos_sp.reset_index(drop=True, inplace=True))

postos_sp = data.query('ESTADO == "SAO PAULO"').reset_index(drop=True)  # ALTERNATIVA MUITO COMUM

# print(postos_sp)

# -----------------------------------15_Filtragem_Parte_03-----------------------------------

# Selecionando registros de postos do Rio de Janeiro com Preços acima de 2 reais

# print(data.head())
#
# print(data['ESTADO'] == 'RIO DE JANEIRO')
#
# print(data['PREÇO MÉDIO REVENDA'] > 2.0)

# print((data['ESTADO'] == 'RIO DE JANEIRO') & (data['PREÇO MÉDIO REVENDA'] > 2.0))

selecao_Rio_Revenda = (data['ESTADO'] == 'RIO DE JANEIRO') & (data['PREÇO MÉDIO REVENDA'] > 2.0)

# print(selecao_Rio_Revenda)

'''
Note que o resultado da seleção continua sendo uma Series de booleans com o mesmo número de linhas/observações do
DataFrame, de modo que cada linha possuirá um valor booleano indicando se o posto é do Rio de Janeiro E o preço aferido 
do combustível é maior que 2 reais (True) ou não.

O símbolo & significa AND na comparação. Essa nomeclatura do python/pandas é diferente das 
nomeclaturas tradicionais (&&).
- | representa o OR (não é ||)
- ˜ representa o NOT (não é !)
'''

# print(data[selecao_Rio_Revenda])

'''
Alternativamente, poderíamos usar o método query para fazermos tal seleção. Porém, isso não é possível especificamente
para esse caso, pois o rótulo da coluna 'PREÇO MÉDIO REVENDA' possui caracteres inválidos para
o método (cedilha, acentos)
'''

# print(data.query('ESTADO == "Rio de Janeiro" and PREÇO MÉDIO REVENDA > 2'))# Não funciona

# print(data.query('ESTADO == "RIO DE JANEIRO" or ESTADO == "SAO PAULO"'))# Funciona

'''
Aprofundando mais ainda

A primeira comparação (data['ESTADO'] == 'RIO DE JANEIRO') checa, linha a linha (amostra a amostra) do DataFrame, quais 
são aquelas cujo o estado é RIO DE JANEIRO. Nenhuma averiguação de preços é feita nesse momento. Como resultado, temos 
uma Series de booleans que responde apenas a essa "pergunta" feita.

A segunda comparação (data['PREÇO MÉDIO REVENDA'] > 2) checa, linha a linha (amostra a amostra) do DataFrame, quais 
são os registro cujo preço do combustível é maior que 2 reais. Note que essa comparação checará os postos de TODOS os 
estados. Como resultado, temos uma Series de booleans que responde apenas a essa "pergunta" feita.

Por fim, as duas "perguntas" são unidas pelo AND (&) que retorna a "pergunta completa" que fizemos.

Alguns podem argumentar que tal abordagem é ineficiente, uma vez que, para cada condição ("pergunta"), estamos 
varrendo todas as linhas do DataFrame.
O Pandas tenta otimizar isso ao máximo por de trás dos panos. Mas, de fato, de tivermos um dataset muito grande 
(centenas de milhares de linhas), tal abordagem se tornará lenta.

Assim, poderíamos fazer filtragem com múltiplos condicionais em partes:
'''

selecao_1 = data['ESTADO'] == 'RIO DE JANEIRO'
postos_rj = data[selecao_1]
# print(postos_rj)

selecao_2 = postos_rj['PREÇO MÉDIO REVENDA'] > 2
# print(selecao_2)

postos_rj_preco_maior_que_2 = postos_rj[selecao_2]
# print(postos_rj_preco_maior_que_2)
# carregando o dataset corretamente ==> neste caso, use o separdor ';'
data = pd.read_csv('/Users/matheus/Downloads/GasPricesinBrazil_2004-2019.csv', sep=';')

# print(data)
# print(data.head())
# print(data.info())
# print(type(data))
# print(data.shape)
# print(f'O DataFrame possui {data.shape[0]} linhas/observações/registros e {data.shape[1]} colunas/atributos/variáveis.')


# personagens_df = pd.DataFrame({
# 'nome': ['Luke Skywalker', 'Yoda', 'Palpatine'],
# 'idade': [16, 1000, 70],
# 'peso' : [70.5, 15.2, 60.1],
# 'eh Jedi' :[True, True, False]
# })


# print(personagens_df)
# print(personagens_df.info())
# print(personagens_df.columns)
# print(type(personagens_df.columns))
# print(list(personagens_df.columns))

# print(personagens_df)
# personagens_df_renomeado = personagens_df.rename(columns={
#     'nome': 'Nome Completo',
#     'idade': 'Idade'
# })

# print(personagens_df_renomeado)
# personagens_df.rename(columns={'nome': 'Nome Completo','idade': 'Idade'}, inplace=True)
#
# print(personagens_df.columns)
#
# personagens_df.columns = ['NOME', 'IDADE', 'PESO', 'EH JEDI']
#
# print(personagens_df)

# print(data.head())
# print(data['ESTADO'])

# print(data.ESTADO)

# print(type(data['ESTADO']))

# print(data.iloc[1])

# print(type(data.iloc[1]))

# print(pd.Series([5.5, 6.0, 9.5]))

# print(pd.Series([5.5, 6.0, 9.5], index=['prova 1', 'prova 2', 'projeto'], name='Notas do Luke Skywalker'))

# print(data)

# print(data['PRODUTO']) # a series retornada a coluna, NAO É UMA CÓPIA, mas sim, uma REFERENCIA/VIEW a coluna do dataFrame

# produto_view = data['PRODUTO']
# print(produto_view)

# produto_copy_bkp = data['PRODUTO'].copy()#retorna uma copia da coluna 'PRODUTO'
# print(produto_copy_bkp)

# data['PRODUTO'] = 'Combustível' #atribuindo o valor constante 'Combustível'para linha do dataframe na coluna 'PRODUTO'
# #print(data.head())
# print(data['PRODUTO'])
# print(produto_copy_bkp)

# nrows, ncols = data.shape

# print(nrows, ncols)

# novos_produtos = [f'Produto {i}' for i in range(nrows)]
# print(novos_produtos)

# print(len(novos_produtos))
# a quantidade de elementos da lista 'novos_produtos' é igual ao número de linhas do dataframe
# data['PRODUTO'] = novos_produtos
# print(data)

# print(produto_view)
# print('\n')
# print(produto_copy_bkp)

# voltando para os produtos originais
# data['PRODUTO'] = produto_copy_bkp

# print(data)

# criando uma coluna a partir de um valor constante/default
# todas as linhas terao o mesmo valor para esta nova coluna

data['coluna sem nocao'] = 'DEFAULT'
# print(data)

data['coluna a partir de lista'] = range(data.shape[0])
# print(data)
# nao funciona porque a quantidade de elementos da lista (a serem atribuídos a nova coluna) é diferente
# da quantidade de linhas do dataframe
# data['nao funciona'] = [1, 2, 3]

# print(data.head())

data['PREÇO MÉDIO REVENDA (dólares)'] = data['PREÇO MÉDIO REVENDA'] * 6.0
# print(data)
# -----------------------------------09_Indices-----------------------------------
# print(data.index)

pesquisa_de_satisfacao = pd.DataFrame({
    'bom': [50, 21, 100],
    'ruim': [131, 2, 30],
    'pessimo': [30, 20, 1]
}, index=['XboxOne', 'Playstation4', 'Switch'])

# print(pesquisa_de_satisfacao.head())
# print(pesquisa_de_satisfacao.index)

# -----------------------------------10_selecao_por_Indices-----------------------------------

# print(data.head())
# selecionando a linha 1 ===> observaçao do índice [1] do dataframe
# print(data.iloc[1])

# Selecionando múltiplas observaçoes/linhas:

# selecionando as linhas de índice de 0 a 5 (incluso)
# print(data.iloc[:6])

# Selecinando as linhas de índice de 10 a 15 (16)
# print(data.iloc[10:16])

# selecionando as linhas/observaçoes de índice 1, 5, 10, 15
# print(data.iloc[[1, 5, 10, 15]])

# selecionando as linhas/observaçoes de índices 5, 1, 15, 10
# print(data.iloc[[5, 1, 15, 10]])
# parei em 7:30 no video

# print(data.iloc[1, 4])

# -----------------------------------11_Selecao_por_Labels-----------------------------------

# iloc: passa índices numéricos
# loc: passa labels das colunas e linhas

# print(pesquisa_de_satisfacao.iloc[0])# retorna a linha de índice 0 (implicito) ===> usando o iloc

# print(pesquisa_de_satisfacao.iloc[0, 1])

# print(pesquisa_de_satisfacao.loc['XboxOne'])# retorna a linha cujo rótulo do índice é 'XboxOne'

# print(pesquisa_de_satisfacao)
#
# print(pesquisa_de_satisfacao.loc['Playstation4', 'ruim'])
#
# print(pesquisa_de_satisfacao.loc[['XboxOne', 'Switch']])

# print(pesquisa_de_satisfacao.loc[:, ['bom', 'pessimo']])

# print(pesquisa_de_satisfacao)
#
# print(pesquisa_de_satisfacao.iloc[0, 2])
#
# print(pesquisa_de_satisfacao.loc['XboxOne', 'pessimo'])

# -----------------------------------12_Selecao_de_Colunas_Atributos-----------------------------------

# print(data.head())
#
# print(data['ESTADO'])# retorna a coluna/atributo 'ESTADO'

# print(data.ESTADO)

# print(data.loc[:, 'ESTADO'])

# a forma de acesso de colunas por .NOME_DA_COLUNA só funciona se o .NOME_DA_COLUNA
# nao possuir carecteres invalidos(espaços, acentos, cedilhas, ...)
# não funciona
# print(data.DATA INCIAL)
# para colunas cujos rótulos possuem caracteres inválidos, apenas a seleção via string é válida
# print(data['DATA INICIAL'])

# print(data[['PRODUTO', 'ESTADO', 'REGIÃO']])# selecionando múltiplas colunas

# -----------------------------------13_Salvando_um_Dataset-----------------------------------

# print(data.head())

del data['Unnamed: 0']  # deleta/remove-in-place (ou seja, no próprio dataframe) a coluna de rótulo 'Unnamed: 0'

# print(data.head())

# vamos agora remover as colunas fictícias criadas no vídeos para estudo.

del data['coluna sem nocao']
del data['coluna a partir de lista']
del data['PREÇO MÉDIO REVENDA (dólares)']

# print(data)

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

# -----------------------------------14_Filtragem_Parte_01-----------------------------------
'''
Seleção Condicional: Filtrando amostras

Durante nossas análises exploratórias, frequentemente filtraremos nossas amostras, a partir de certas condições, 
para fins de análise mais específica. Existem algumas maneiras de fazermos tal filtragem. Antes disso, vamos carregar
nosso dataset pré-processado que salvamos no item anterior.
'''

data = pd.read_csv('/Users/matheus/Downloads/GasPricesinBrazil_2004-2019_preprocessado.csv')

# print(data.head())

# print(data['ESTADO'].unique())# Mostra todos os estados cujos preços dos combustíveis foram aferidos
# Mais tecnicamente, mostra os valores únicos presentes para o atributo/coluna 'ESTADO'
'''
Selecionando apenas os preços dos Postos de São Paulo
==> Alternativa 1: Seleção Condicional(Comparações diretas)
O código abaixo retorna uma Series ('array') de booleans, com o número de linhas (amostras) do Data Frame,
que informa os registros de preços dos postos do estado de São Paulo(True).
'''

# print(data['ESTADO'] == 'SAO PAULO')# Faz uma comparação elemento a elemento da series, retornando uma Series
# de booleans

# Salvando essa Series de booleans em uma variável
selecao = data['ESTADO'] == 'SAO PAULO'

# print(selecao)
#
# print(type(selecao))

# print(selecao.shape)
#
# print(data.shape)

# Fazendo a filtragem dos registros do estado de São Paulo
# print(data[selecao])# O resultado é um Data Frame com apenas os registros desejados após a filtragem
#
# print(data.loc[selecao])# Podemos ainda utilizar o método "loc" para o mesmo fim

# -----------------------------------15_Filtragem_Parte_02-----------------------------------

# Alternativa 2: Utilizando o método "query"
# query filtra as linhas de um Data Frame baseado em um query (pergunta)

# print(data.head())

# print(data.query('ESTADO == "SAO PAULO"'))

postos_sp = data.query('ESTADO == "SAO PAULO"')  # Uma boa prática é salvar o Data Frame filtrado em uma nova variável.
# Isso simplifica a complexidade do código apar futurras análises  feitas para os postos de São Paulo (neste caso).

# print(postos_sp)

# print(type(postos_sp))
#
# print(postos_sp.shape)
#
# print(postos_sp.head())

'''
Resetando os índices

Note que os índices das linhas/registros após a filtragem continuam sendo os mesmos do Data Frame original.
Em muitas situações, manter esta informação será importante.

Mas, se voce quiser resetar os índices do Data Frame filtrado, fazendo com que os registros começem com índice 0 até 
num_linhas-1, use o método .reset_index. 
'''

# print(postos_sp)
#
# print(postos_sp.reset_index(drop=True))

# print(postos_sp)# Ainda não foi alterado, precisamos usar o atributo/parametro "inplace=True"

# print(postos_sp.reset_index(drop=True, inplace=True))

postos_sp = data.query('ESTADO == "SAO PAULO"').reset_index(drop=True)  # ALTERNATIVA MUITO COMUM

# print(postos_sp)

# -----------------------------------16_Filtragem_Parte_03-----------------------------------

# Selecionando registros de postos do Rio de Janeiro com Preços acima de 2 reais

# print(data.head())
#
# print(data['ESTADO'] == 'RIO DE JANEIRO')
#
# print(data['PREÇO MÉDIO REVENDA'] > 2.0)

# print((data['ESTADO'] == 'RIO DE JANEIRO') & (data['PREÇO MÉDIO REVENDA'] > 2.0))

selecao_Rio_Revenda = (data['ESTADO'] == 'RIO DE JANEIRO') & (data['PREÇO MÉDIO REVENDA'] > 2.0)

# print(selecao_Rio_Revenda)

'''
Note que o resultado da seleção continua sendo uma Series de booleans com o mesmo número de linhas/observações do
DataFrame, de modo que cada linha possuirá um valor booleano indicando se o posto é do Rio de Janeiro E o preço aferido 
do combustível é maior que 2 reais (True) ou não.

O símbolo & significa AND na comparação. Essa nomeclatura do python/pandas é diferente das 
nomeclaturas tradicionais (&&).
- | representa o OR (não é ||)
- ˜ representa o NOT (não é !)
'''

# print(data[selecao_Rio_Revenda])

'''
Alternativamente, poderíamos usar o método query para fazermos tal seleção. Porém, isso não é possível especificamente
para esse caso, pois o rótulo da coluna 'PREÇO MÉDIO REVENDA' possui caracteres inválidos para
o método (cedilha, acentos)
'''

# print(data.query('ESTADO == "Rio de Janeiro" and PREÇO MÉDIO REVENDA > 2'))# Não funciona

# print(data.query('ESTADO == "RIO DE JANEIRO" or ESTADO == "SAO PAULO"'))# Funciona

'''
Aprofundando mais ainda

A primeira comparação (data['ESTADO'] == 'RIO DE JANEIRO') checa, linha a linha (amostra a amostra) do DataFrame, quais 
são aquelas cujo o estado é RIO DE JANEIRO. Nenhuma averiguação de preços é feita nesse momento. Como resultado, temos 
uma Series de booleans que responde apenas a essa "pergunta" feita.

A segunda comparação (data['PREÇO MÉDIO REVENDA'] > 2) checa, linha a linha (amostra a amostra) do DataFrame, quais 
são os registro cujo preço do combustível é maior que 2 reais. Note que essa comparação checará os postos de TODOS os 
estados. Como resultado, temos uma Series de booleans que responde apenas a essa "pergunta" feita.

Por fim, as duas "perguntas" são unidas pelo AND (&) que retorna a "pergunta completa" que fizemos.

Alguns podem argumentar que tal abordagem é ineficiente, uma vez que, para cada condição ("pergunta"), estamos 
varrendo todas as linhas do DataFrame.
O Pandas tenta otimizar isso ao máximo por de trás dos panos. Mas, de fato, de tivermos um dataset muito grande 
(centenas de milhares de linhas), tal abordagem se tornará lenta.

Assim, poderíamos fazer filtragem com múltiplos condicionais em partes:
'''

# selecao_1 = data['ESTADO'] == 'RIO DE JANEIRO'
# postos_rj = data[selecao_1]
# print(postos_rj)
#
# selecao_2 = postos_rj['PREÇO MÉDIO REVENDA'] > 2
# print(selecao_2)
#
# postos_rj_preco_maior_que_2 = postos_rj[selecao_2]
# print(postos_rj_preco_maior_que_2)

# -----------------------------------17_Filtragem_Parte_04-----------------------------------

'''
Selecionando registros de postos de São Paulo ou do Rio de Janeiro com Gasolina Comum acima de 2 reais
Podemos fazer a solução do "jeito mais lento", percorrendo o DataFrame inteiro múltiplas vezes:
'''
# print(data.head())

selecao_1 = (data['ESTADO'] == 'SAO PAULO') | (data['ESTADO'] == 'RIO DE JANEIRO')
# print(selecao_1)
selecao_2 = (data['PRODUTO'] == 'GASOLINA COMUM')
selecao_3 = (data['PREÇO MÉDIO REVENDA'] > 2)

selecao_final = selecao_1 & selecao_2 & selecao_3

# print(selecao_final)

# print(data[selecao_final])

data_filtrado = data[selecao_final]

# print(data_filtrado)

# print(data_filtrado['ESTADO'].unique())
#
# print(data_filtrado['PRODUTO'].unique())

'''
Alternativamente:
'''

selecao_1 = (data['ESTADO'] == 'SAO PAULO') | (data['ESTADO'] == 'RIO DE JANEIRO')
postos_sp_rj = data[selecao_1]  # apenas registros de postos dos estados de SP e RJ

# print(postos_sp_rj)

selecao_2 = (postos_sp_rj['PRODUTO'] == 'GASOLINA COMUM')
# print(selecao_2)

postos_sp_rj_gasolina = postos_sp_rj[selecao_2]  # apenas registros de postos dos estados de SP e RJ
# cujo produto é GASOLINA COMUM

# print(postos_sp_rj_gasolina)

selecao_3 = (postos_sp_rj_gasolina['PREÇO MÉDIO REVENDA'] > 2)

# print(selecao_3)

postos_sp_rj_preco_maior_que_2 = postos_sp_rj_gasolina[selecao_3]

# print(postos_sp_rj_preco_maior_que_2)

# -----------------------------------18_Filtragem_Parte_05-----------------------------------

'''
Selecionando registros dos anos de 2008, 2010 e 2012
'''

'''
ALTERNATIVA 1
'''

selecao = (data['ANO'] == 2008) | (data['ANO'] == 2010) | (data['ANO'] == 2012)
# print(selecao)

# print(data[selecao]['ANO'].unique())

'''
ALTERNATIVA 2
'''

lista_de_anos = [2008, 2010, 2012]

selecao = (data['ANO'].isin(lista_de_anos))  # retorna uma Series de booleanos
# print(selecao)

'''
ALTERNATIVA 3
'''

# print(lista_de_anos)
#
# print(data.query('ANO in @lista_de_anos'))

'''
Iterando com DataFrames
For-each DataFrame.iterrows() (LENTO ==> apenas indicado para iterar pequenos conjunto de dados)
'''

# for index, row in data.head(10).iterrows():
#     print(f'indice{index} ==> {row['ESTADO']}')

#-----------------------------------19_Limpeza_de_Dados_Parte_01-----------------------------------

'''
2. Preparação dos dados, Tratando observações com valores vazios (null / nan) no dataset
'''

print(data.info())
'''
De um total de 106823 observações, não há valores null / nan para nenhum atributo.
Mas, veremos que não é bem assim neste caso específico.
'''

'''
2.2 Conversão de tipos de atributos
O pandas automaticamente reconhece os tipos de dados de cada coluna.
Porém, existem alguns atributos que estão com seus tipos errados: P. ex., "PREÇO MÉDIO DISTRIBUIÇÃO" 
deveria ser float64 e não object.
Nestes casos, muito provavelmente alguns registros têm uma string ao invés de um número para tais atributos.

Os atributos "DATA INICIAL" e "DATA FINAL" deveriam ser do tipo datetime.

Em outros casos, alguns atributos categóricos são objects, mas poderiam ser o tipo category, 
que é um tipo especial do pandas.
Este tipo é necessário para se utilizar algumas funções específicas do pandas.
Não converteremos para este tipo por ora.
'''

data_pre = data.copy()

'''
Datas
Como os atributos de data do dataset já estão 
em um formato de data aceitável (YYYY-MM-DD), não precisamos forçar nenhuma conversão nesse sentido.
'''

data_pre['DATA INICIAL'] = pd.to_datetime(data_pre['DATA INICIAL'])

data_pre['DATA FINAL'] = pd.to_datetime(data_pre['DATA FINAL'])

print(data_pre.info())

'''
# convertendo atributos/colunas para 'numeric'
'''

# convertendo atributos/colunas para 'numeric'
for atributo in ['MARGEM MÉDIA REVENDA', 'PREÇO MÉDIO DISTRIBUIÇÃO', 'DESVIO PADRÃO DISTRIBUIÇÃO', 'PREÇO MÍNIMO DISTRIBUIÇÃO', 'PREÇO MÁXIMO DISTRIBUIÇÃO', 'COEF DE VARIAÇÃO DISTRIBUIÇÃO']:
    # converte a coluna (de valores string) para um tipo numérico
    # Em caso de erro na conversão (p. ex., uma string que não representa um número), um valor vazio (null / nan) será
    # atribuído no lugar
    data_pre[atributo] = pd.to_numeric(data_pre[atributo], errors='coerce')

print(data_pre.info())

# Note que temos vários valores null agora **após a *conversão de tipos***.
# Vamos checá-los com mais cuidado nos dados originais e preprocessados

#-----------------------------------20_Limpeza_de_Dados_Parte_02-----------------------------------

'''
2.3 Limpeza de dados
'''

mask = data_pre['PREÇO MÉDIO DISTRIBUIÇÃO'].isnull()
print(data_pre[mask])
# Nos dados originais, quais eram os valores do PREÇO MÉDIO DISTRIBUIÇÃO dos registros
# que agora possuem valores NaN
print(data[mask])
