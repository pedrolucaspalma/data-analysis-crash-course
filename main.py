import pandas as pd

tabela_vendas = pd.read_excel('Vendas.xlsx')

pd.set_option('display.max_columns', None)

print(tabela_vendas)

faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)