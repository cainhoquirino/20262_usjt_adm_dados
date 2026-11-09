import pandas as pd
pedidos = pd.DataFrame({
  "id_cliente": [1, 2, 1, 3],
  "valor": [100, 200, 50, 80]
})

clientes = pd.DataFrame({
  "id_cliente": [1, 2, 3],
  "nome": ["Ana", "Bruno", "Carla"],
  "cidade": ["SP", "Rio", "BH"]
})

completo = pedidos.merge(clientes, on="id_cliente")
print(completo)

# df = pd.read_csv(
#   "clientes.csv",
#   sep=",",
#   decimal=".",
#   encoding="utf-8"
# )
# df["com_frete"] = df["valor"] + 15
# df["faixa"] = df["valor"].apply(
#   lambda v: "alto" if v > 100 else "baixo"
# )
# print(
#   df.sort_values("valor", ascending=False).head(3)
# )

# print(
#   df.groupby("cidade").agg(
#     total=("valor", "sum"),
#     media=("valor", "mean"),
#     pedidos=("valor", "count")
#   )
# )
# print(df.groupby("cidade")["valor"].mean())
# print(df[["cliente", "valor", "faixa"]])

# print(df.isnull().sum())
# df["valor"].fillna(0)
# print(df.head())

#series
# serie = pd.Series(["1.234,56", "89,90", "abc"])
# numeros = serie.str.replace(".", "", regex=False)
# numeros = numeros.str.replace(",", ".", regex=False)
# numeros = pd.to_numeric(numeros, errors="coerce")
# print(numeros)
# print(df.head())
# print(df[(df["valor"] > 100) & (df["cidade"] == "Curitiba")])
# print(df[df["cliente"].str.contains("a")])
#print(df[df["valor"].between(80,200)])
#print(df[df["cidade"].isin(["Recife", "Curitiba"])])
# print(df[df["valor"] > 100])
# print(df.loc[df["valor"] > 100, "cliente"])
# print(df.iloc[0, 0])
# print(df.loc[0,"cidade"])
# print(df["cidade"])
# print(df["cidade"].value_counts())
# print(df.describe())
# print(df.info())
# print(df.head(2))
# print(df.shape)
# print(df.dtypes)


# dados = {
#   "cliente": ["Maria", "João", "Ana", "Bruno"],
#   "cidade": ["São Paulo", "Recife", "Curitiba", "Recife"],
#   "valor": [150.0, 89.90, 230.5, 60.0]
# }
# df = pd.DataFrame(dados)
# print(df)
# nome = "Ana"
# #O nome é: Ana
# print("O nome é: " + nome)
# #f-string
# print(f"O nome é: {nome}")
# # 2 + 2 = 4
# numero = 2
# print(f'{numero} + {numero} = {numero + numero}')
#try/except
# valores = ["100", "abc", "250", ""]
# for v in valores:
#   try:
#     numero = int(v)
#     print(f"2 * {numero} = {2 * numero}")
#   except ValueError:
#     print(f"{v} não é númerico")
# try:
#   for v in valores:
#     numero = int(v)
#     print(numero * 2)
# except ValueError:
#   print(f"{v} não é um número válido")


# situacao = lambda nota: "aprovado" if nota >= 70 else  "reprovado"
# print(situacao(85))
# print(situacao(40))

# dobro = lambda x: x * 2
# print(dobro(5))

# def dobro(x):
#   return 2 * x

# def resumo_vendas(valores, imposto=0.1):
#   total = sum(valores)
#   media = total / len(valores)
#   total_com_imposto = total * (1 + imposto)
#   return total, media, total_com_imposto
# t, m, ti = resumo_vendas([100, 200, 300], 0clear
# .15)
# print(f"Total: {t}, Média: {m:.2f}, Com imposto: {ti:.2f}")
# def teste(p=2):
#   print(p)

# teste()
# teste(3)

# nomes = ["Maria", "João", "Ana"]
# for i, nome in enumerate(nomes):
#   print(i, nome)


# emails = ["ana@x.com", "joao.com", "maria@y.com", "pedro"]
# #variável contadora
# invalidos = 0
# for email in emails:
#   if "@" not in email:
#       invalidos = invalidos + 1
#       print(f"Inválido: {email}")
# print(f"Total de inválidos: {invalidos}")

# precos = [19.9, 45, 12.5]
# total = 0 #acumulador
# for p in precos:
#   total = total + p
# print(f"Total: R$ {total:.2f}")


#operador in
# uf = "MA"
# validos = ["SP", "RJ", "MG", "PR", "RS"]
# if uf in validos:
#   print("UF reconhecida")
# else:
#   print("UF inválida")

# # if elif else
# valor = 250
# #se for pelo menos 500, é alto
# #se for pelo menos 100 é médio
# #caso contrário, é baixo
# if valor >= 500:
#   faixa = "alto"
# elif valor >= 100:
#   faixa = "médio"
# else:
#   faixa = "baixo"

# print(f"Cliente de ticket {faixa}")

# valores únicos usando conjuntos (sets)
# estados = ["SP", "RJ", "MG", "RJ", "SP"]
# print(set(estados))
# print(len(set(estados)))

# tabela = [
#   {"nome": "Maria", "saldo": 150},
#   {"nome": "João", "saldo": 200},
#   {"nome": "Ana", "saldo": 250}
# ]
# print(tabela[3]["nome"])

#dicionário: coleção de pares chave/valor
# cliente = {
#   "nome": "Maria",
#   "idade": 34,
#   "cidade": "São Paulo"
# }
# print(cliente["cidade"])
# cliente["email"] = "maria@email.com"
# for chave, valor in cliente.items():
#   print(chave, "->", valor)

#list comprehensions (compreensão de lista)
# precos = [19.90, 45.00, 12.50, 89.90]
# #aplicar 10% a todos
# com_imposto = [p * 1.1 for p in precos]
# print(com_imposto)
# caros = [p for p in precos if p > 40]
# print(caros)


# #listas
# precos = [19.90, 45.00, 12.50, 89.90]
# #quantos
# print(len(precos)) #length
# #soma
# print(sum(precos))
# #maior valor
# print(max(precos))
# #adicionar um valor
# precos.append(30.00) #concatenar
# #apenas os dois primeiros
# print(precos[:2])


# valor_txt = " R$ 1.234,56 "
# limpo = valor_txt.replace("R$", "").replace(".", "").replace(",", " ").strip()
# valor = float(limpo)
# print(valor + 10)

# nome = "  maria     SILVA   "
# limpo = nome.strip().title() #Maria Silva
# print(limpo)
# print(limpo.split())
# print(" ".join(limpo.split()))
#índice e fatiamento
# cpf = "12345678900"
# print(cpf[-1:1])
# print(cpf[-1])
# print(cpf[0:3])
# print(cpf[0])
# print(cpf[10])

# f-string
# nome = "Maria"
# valor = 1234.50
# #Maria gastou R$1234.50
# print(f'{nome} gastou R${valor:.2f}')

# preco_textual = "19.90"
# preco = float(preco_textual)
# idade_textual = "18"
# idade = int(idade_textual)


# print(type("Maria"))
# nome = "Maria"
# sobrenome = 'Silva'
# idade = 34
# ativo = True
# altura = '180'
# print(nome, sobrenome, idade, ativo, altura)
# print(10 / 0)
# print('Olá, mundo dos dados!')