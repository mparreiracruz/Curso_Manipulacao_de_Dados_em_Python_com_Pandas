import pandas as pd
#carregando o dataset corretamente ==> neste caso, use o separdor ';'
data = pd.read_csv('/Users/matheus/Downloads/GasPricesinBrazil_2004-2019.csv', sep=';')

#print(data)
#print(data.head())
#print(data.info())
#print(type(data))
#print(data.shape)
# print(f'O DataFrame possui {data.shape[0]} linhas/observações/registros e {data.shape[1]} colunas/atributos/variáveis.')


personagens_df = pd.DataFrame({
'nome': ['Luke Skywalker', 'Yoda', 'Palpatine'],
'idade': [16, 1000, 70],
'peso' : [70.5, 15.2, 60.1],
'eh Jedi' :[True, True, False]
})

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
personagens_df.rename(columns={'nome': 'Nome Completo','idade': 'Idade'}, inplace=True)

print(personagens_df.columns)

personagens_df.columns = ['NOME', 'IDADE', 'PESO', 'EH JEDI']

print(personagens_df)
