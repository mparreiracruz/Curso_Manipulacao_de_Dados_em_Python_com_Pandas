import pandas as pd
#
# '''
# 1.1. Importando o Dataset
# '''
#
data = pd.read_csv('/Users/matheus/Downloads/GasPricesinBrazil_2004-2019.csv', sep=';')
# # carregando o dataset corretamente ==> neste caso, usa o separador ';'
#
# '''
# 1.2. Exibindo as primeiras linhas do Dataset
# '''
#
# print(data.head())  # 5 primeiras linhas
# print(data.head(10))  # 10 primeiras linhas
#
# '''
# 1.3 Informações do Dataset e Elementos Chave
# '''
#
# print(data.info())  # Informações gerais sobre o Dataset
#
# print(type(data))  # tipo de DataFrame
#
# print(data.shape)  # acessar as dimensões do Data Frame (número de linhas x número de colunas)
#
# print(f'O DataFrame possui {data.shape[0]} linhas/observações/registros e {data.shape[1]} colunas/atributos/variáveis.')
#
# '''
# 1.3.3 Series
# '''
#
# print(data['ESTADO'])  # selecionando uma coluna inteira
#
# print(data.ESTADO)  # só funciona para colunas com nomes sem espaços, acentos, etc
#
# print(type(data['ESTADO']))  # tipo de data em 'ESTADO'
#
# print(data.iloc[1])  # selecionando a observação indexada no índice [1] do dataframe
#
# print(type(data.iloc[1]))  # selecionando o tipo de data no índice [1] do dataframe
#
# '''
# 1.3.4 Atribuindo Dados e constantes
# '''
#
produto_view = data['PRODUTO']  # a series retornada refente à coluna, NÃO É UMA CÓPIA,
# # mas sim, uma REFERÊNCIA/VIEW à coluna do dataframe
#
# print(produto_view)
#
produto_copy_bkp = data['PRODUTO'].copy()  # retorna uma cópia da coluna 'PRODUTO'
# print(produto_copy_bkp)
#
data['PRODUTO'] = 'Combustível'  # atribuindo o valor constante 'Combustível' para
# # linha do dataframe na coluna 'PRODUTO'
#
# '''
# 1.3.4.2 Atribuindo listas ou series
# '''
#
nrows, ncols = data.shape
# print(nrows, ncols)
#
novos_produtos = [f'Produto {i}' for i in range(nrows)]
# print(len(novos_produtos))  # retorna o número de elementos na lista "novos_produtos".
# # A quantidade de elementos da lista `novos_produtos` é igual ao número de linhas do dataframe
#
data['PRODUTO'] = novos_produtos  # substitui os valores existentes na coluna 'PRODUTO' do DataFrame
# # com os valores da lista novos_produtos.
#
# print(data)
#
# print(produto_view)
# print('\n')
# print(produto_copy_bkp)
#
data['PRODUTO'] = produto_copy_bkp  # Voltando para os produtos originais, produto_copy_bkp é uma Series
#
# '''
# 1.3.4.3 Criando novas colunas
# '''
#
data['coluna sem nocao'] = 'DEFAULT'  # criando uma coluna a partir de um valor constante/default,
# # todas as linhas terão o mesmo valor para esta nova coluna
#
# print(data)
#
data['coluna a partir de lista'] = range(data.shape[0])  # cria uma coluna nova chamada 'coluna a partir de lista' e
# # cria um objeto range que gera uma sequência de números
# # de 0 até data.shape[0] - 1. Se data.shape[0] for 1000, isso gera uma sequência de 0 a 999.
#
# print(data)
#
# #data['nao funciona'] = [1, 2, 3]  # não funciona pq a quantidade de elementos da lista
# # (a serem atribuídos a nova coluna) é diferente da quantidade de linhas do dataframe
#
data['PREÇO MÉDIO REVENDA (dólares)'] = data['PREÇO MÉDIO REVENDA'] * 6.0 #  cria uma nova coluna chamada
# # 'PREÇO MÉDIO REVENDA (dólares)' e multiplica por 6.0 os valores da coluna 'PREÇO MÉDIO REVENDA'.
#
# print(data)
#
# '''
# 1.3.4 Índices
# '''
#
#print(data.index)  # exibe os índices do DataFrame data.
#
#print(list(data.index))  # converte um RangeIndex para uma python list.
#print(data.index.to_list())  # converte um RangeIndex para uma python list.

'''
1.4 Selecionando uma ou mais observações (Indexação)
'''

'''
==> Index-based selection (seleção baseada em Índices)
'''

# print(data.iloc[1])  # selecionando a linha 1 ===> observação de índice [1] do dataframe --> row-first, column-second
#
# print(data.iloc[:6])  # selecionando as linhas de índice de 0 a 5 (incluso)
#
# print(data.iloc[10:16])  # selecionando as linhas de índice de 10 a 15 (incluso)
#
# print(data.iloc[[1, 5, 10, 15]])  # selecionando as linhas/observações de índice 1, 5, 10, 15
#
# print(data.iloc[[5, 1, 15, 10]])  # selecionando as linhas/observações de índices 5, 1, 15, 10
#
#
# print(data.iloc[1, 4])  # retornar o valor da linha de índice 1, coluna 4 ('ESTADO')

'''
==> Label-based selection (seleção baseadas em Rótulos)
'''

# print(data.loc[:, 'ESTADO'])
#
# # a forma de acesso de colunas por .NOME_DA_COLUNA só funciona se
# # NOME_DA_COLUNA não possuir caracteres inválidos (espaços, acentos, cedilha, ...)
# ### não funciona
# # data.DATA INICIAL
#
# print(data['DATA INICIAL'])  # para colunas cujos rótulos possuem caracteres inválidos,
# # apenas a seleção via string é válida
#
# print(data[['PRODUTO', 'ESTADO', 'REGIÃO']])  # selecionando múltiplas colunas: 'PRODUTO', 'ESTADO', 'REGIÃO'

'''
1.6 Removendo um Atributo (Coluna) do Data Frame
'''

# Removendo as colunas fictícias criadas nos vídeos para estudo.
del data['Unnamed: 0']  # deleta/remove in-place (ou seja, no próprio dataframe) a coluna de rótulo 'Unnamed: 0'
del data['coluna sem nocao']
del data['coluna a partir de lista']
del data['PREÇO MÉDIO REVENDA (dólares)']

'''
1.7 Salvando um Data Frame
'''

# data.to_csv('/Users/matheus/Downloads/GasPricesinBrazil_2004-2019_preprocessado.csv', index=False)
#
# data = pd.read_csv('/Users/matheus/Downloads/GasPricesinBrazil_2004-2019_preprocessado.csv')
#
# print(data.head())
#
# print(data['ESTADO'].unique())  # Mostra todos os estados cujos os preços dos combustíveis foram aferidos
# Mais tecnicamente, mostra os valores únicos presentes para o atributo/coluna 'ESTADO'.

'''
Selecionando apenas os preços dos Postos de São Paulo
==> Alternativa 1: Seleção Condicional (Comparações diretas)
'''


# print(data['ESTADO'] == 'SAO PAULO')  # faz uma comparação elemento a elemento da series, retornando uma Series de booleans
# #
# # # salvando essa Series de booleans em uma variável
# selecao = data['ESTADO'] == 'SAO PAULO'
# #
# # print(selecao)
# #
# # print(data[selecao])  # Para filtrarmos os registros de postos do estado de São Paulo
# #
# # print(data.loc[selecao])  # Podemos ainda utilizar o método loc para o mesmo fim:
#
# '''
# ==> Alternativa 2: Utilizando o método query
# query filtra linhas de um DataFrame baseado em uma query (pergunta).
# '''
#
# print(data.query('ESTADO == "SAO PAULO"'))

'''
Uma boa prática é salvar o Data Frame filtrado em uma nova variável. Isso simplifica 
a complexidade do código para futuras análises feitas para os postos de São Paulo (neste caso).
'''

postos_sp = data.query('ESTADO == "SAO PAULO"')
# print(postos_sp)
#
# '''
# Resetando os índices
# '''
#
#print(postos_sp.reset_index()  # faz com que os registros começem com índice 0 até num_linhas-1
#
# print(postos_sp.reset_index(drop=True))  # cria um novo índice baseado em uma sequência numérica crescente (0, 1, 2, ...)
# # e faz com que o antigo índice não seja adicionado como uma nova coluna no DataFrame, ainda não foi alterado,
# # precisamos usar o atributo/parâmetro inplace=True.
#
# print(postos_sp)

postos_sp.reset_index(drop=True, inplace=True)

# print(postos_sp)
#
postos_sp = data.query('ESTADO == "SAO PAULO"').reset_index(drop=True)  # ALTERNATIVA MUITO COMUM
#
# print(postos_sp)

'''
Selecionando registros de postos do Rio de Janeiro com Preços acima de 2 reais
'''

# print(data['ESTADO'] == 'RIO DE JANEIRO')
#
# print(data['PREÇO MÉDIO REVENDA'] > 2.0)

selecao = (data['ESTADO'] == 'RIO DE JANEIRO') & (data['PREÇO MÉDIO REVENDA'] > 2.0)

print(selecao)

print(data[selecao])

# Não funciona pois o rótulo da coluna 'PREÇO MÉDIO REVENDA' possui caracteres
# inválidos para o método (cedilha, acentos)
# data.query('ESTADO=="RIO DE JANEIRO" and PREÇO MÉDIO REVENDA > 2')

print(data.query('ESTADO == "RIO DE JANEIRO" or ESTADO == "SAO PAULO"'))  # já esse funciona

'''
Aprofundando mais ainda

A primeira comparação (data['ESTADO'] == 'RIO DE JANEIRO') checa, linha a linha (observação a observação) do DataFrame,
 quais são aquelas cujo o estado é RIO DE JANEIRO. Nenhuma averiguação de preços é feita nesse momento. Como resultado,
  temos uma Series de booleans que responde apenas a essa "pergunta" feita.

A segunda comparação (data['PREÇO MÉDIO REVENDA'] > 2) checa, linha a linha (observação a observação) do DataFrame,
 quais são os registros cujo preço do combustível é maior que 2 reais. Note que essa comparação checará os postos de
  TODOS os estados. Como resultado, temos uma Series de booleans que responde apenas a essa "pergunta" feita.

Por fim, as duas "perguntas" são unidas pelo AND (&) que retorna a "pergunta completa" que fizemos.

Alguns podem argumentar que tal abordagem é ineficiente, uma vez que, para cada condição ("pergunta"), 
estamos varrendo todas as linhas do DataFrame.
O Pandas tenta otimizar isso ao máximo por de trás dos panos. Mas, de fato, se tivermos um dataset muito grande 
(centenas de milhares de linhas), tal abordagem se tornará lenta.
'''

'''
Filtragem com múltiplos condicionais em partes
'''

selecao_1 = data['ESTADO'] == 'RIO DE JANEIRO'
postos_rj = data[selecao_1]
print(postos_rj)

selecao_2 = postos_rj['PREÇO MÉDIO REVENDA'] > 2
print(selecao_2)

postos_rj_preco_maior_que_2 = postos_rj[selecao_2]
print(postos_rj_preco_maior_que_2)

'''
Selecionando registros de postos de São Paulo ou do Rio de Janeiro com Gasolina Comum acima de 2 reais
'''

selecao_1 = (data['ESTADO'] == 'SAO PAULO') | (data['ESTADO'] == 'RIO DE JANEIRO')
selecao_2 = (data['PRODUTO'] == 'GASOLINA COMUM')
selecao_3 = (data['PREÇO MÉDIO REVENDA'] > 2)

selecao_final = selecao_1 & selecao_2 & selecao_3
print(selecao_final)

data_filtrado = data[selecao_final]
print(data_filtrado)

