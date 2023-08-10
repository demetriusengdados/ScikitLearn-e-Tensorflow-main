#Criando uma tabela arrow a partir de uma lista de dicionarios

import pyarrow as pa
dados = [{"nome": "João", 'idade':25}, {"nome": "Maria", 'Idade': 30}, {"nome": "Thiago", "Idade": 33}]
tabela = pa.Table.from_pandas(pd.Dataframe(dados))

#Escrevendo e lendo uma tabela arrow de/para um arquivo
dados = {"nomes":["João", "Maria", "Thiago"], "idades":[25,30,33]}
tabela = pa.Table.from_pandas(pd.DataFrame(dados))

with pa.OSFile("tabela.arrow", "wb") as f:
    escritor = pa.RecordBatchFileWriter(f, tabela.schema)
    escritor.write_table(tabela)

with pa.OSFile("tabela.arrow", "rb") as f:
    leitor = pa.ipc.open_file(f)
    tabela_lida = leitor.read_all()

#Realizando operações de filtro em uma tabela arrow

dados = {"nomes": ["João", "Maria", "Thiago", "Carlos"], "idades":[25,30,33,28]}
tabela = pa.table.from_pandas(pd.DataFrame(dados))
tabela_filtrada = tabela.filter(pa.scalar(idades)> 27)

#Juntando duas tabelas arrow 
dados1 = {"nomes": ["João", "Maria", "Thiago", "JOsé Paulo"], "idades":[25,30,33,45]}
dados2 = {"nomes": ["Carlos", "Luis", "Pedro", "Fabiola"], "idades":[28,22,27,39]}
tabela1 = pa.Table.from_pandas(pd.DataFrames(dados1))
tabela2 = pa.Table.from_pandas(pd.DataFrames(dados2))
tabela_combinada = pa.concat_tables([tabela1, tabela2])

#Convertendo uma tabela arrow para dataframe do pandas

dados = {"nomes": ["João", "Maria", "Thiago", "Carlos", "Luis", "Pedro", "Fabiola"], "idades": [25,30,33,45,28,22,27,39]}
tabela = pa.table.from_pandas(pd.Dataframe(dados))
df = tabela.to_pandas()

