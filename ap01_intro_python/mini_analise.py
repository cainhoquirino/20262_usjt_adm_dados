import matplotlib.pyplot as plt
import pandas as pd

dados = {
  "pedido": [1, 2, 2, 3, 4],
  "valor": ["100,00", "250,50", "250,50", "abc", "80,00"]
}

df = pd.DataFrame(dados)
print(df["valor"].dtype)

df = df.drop_duplicates(subset="pedido")
df["valor"] = df["valor"].str.replace(",", ".", regex=False)
df["valor"] = pd.to_numeric(df["valor"], errors="coerce")
df = df.dropna(subset=["valor"])
print(f"Pedidos válidos: {len(df)}")
print(f"Ticket Médio: R${df['valor'].mean():.2f}")

df = pd.read_csv(
  "clientes.csv",
  sep=",",
  decimal=".",
  encoding="utf-8"
)

total_cidade = df.groupby("cidade")["valor"].sum()
print(total_cidade)
total_cidade.sort_values().plot(kind="")
plt.title("Total vendido por cidade")
plt.xlabel("Valor(R$)")
plt.show()
