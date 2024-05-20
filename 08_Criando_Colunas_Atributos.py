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
print(data)
