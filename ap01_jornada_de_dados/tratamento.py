import pandas as pd
import config as c

NOMES = {
    "Transaction ID": "id_transacao",
    "Item": "item",
    "Quantity": "quantidade",
    "Price Per Unit": "preco_unitario",
    "Total Spent": "total_gasto",
    "Payment Method": "forma_pagamento",
    "Location": "local",
    "Transaction Date": "data"
}

CAMPOS = list(NOMES.values())

PROBLEMAS = ["","ERROR", "UNKNOWN"]
AUSENTES = PROBLEMAS + ["Não informado", "Não identificado"]

ITENS = {
    "Coffee": "Café", "Tea": "Chá", "Sandwich": "Sanduíche", "Salad": "Salada", "Cake": "Bolo", "Cookie":"Cookie",
    "Smoothie": "Smoothie", "Juice": "Suco"
}

PAGAMENTOS = {
    "Cash": "Dinheiro", "Credit Card": "Cartão de Crédito",
    "Digital Wallet": "Carteira Digital"
}

LOCAIS = {
    "In-Store": "No local", "Takeaway": "Para viagem"
}

CARDAPIO = {
    "Café": 2.0, "Chá": 1.5, "Sanduíche": 4.0, "Salada": 5.0,
     "Bolo": 3.0, "Cookie": 1.0, "Smootie": 4.0, "Suco": 3.0
}

PRECO_EXCLUSIVO = {
    1.0: "Cookie", 1.5: "Chá", 2.0: "Café", 5.0: "Salada"
}

def diagnosticar(df): 
    ruim = df[CAMPOS].isna() | df[CAMPOS].isin(AUSENTES)
    print(ruim)
    completude = (1- ruim.mean()) * 100
    print(completude)
    perfeitas = (~ruim.any(axis=1)).mean() * 100
    print(perfeitas)
    return completude, perfeitas

def mostrar_diagnostico(completude, perfeitas):
    for coluna, valor in completude.items():
        print(f"{coluna} {c.br(valor, 1)}%")
    print(f"Linhas Perfeitas: {c.br(perfeitas, 1)}%")

def padronizar(bronze):
    df = bronze.rename(columns=NOMES)
    df[CAMPOS] = df[CAMPOS].replace(PROBLEMAS, pd.NA)
    for coluna in ["quantidade", "preco_unitario", "total"]:
        df[coluna] = pd.to_numeric(df[coluna], errors="coerce")
    df["data"] = pd.to_datetime(
        df["data"],
        format="%Y-%m-%d",
        errors="coerce"
    )
    df["item"] = df["item"].map(ITENS)
    df["forma_pagamento"] = df["forma_pagamento"].map(PAGAMENTOS)
    df["local"] = df["local"]
    return df

def tratar():
    bronze = pd.read_parquet(c.BRONZE / "vendas.parquet")
    antes, perfeitas_antes= diagnosticar(bronze.rename(columns=NOMES))
    print("Diagnóstico da camada bronze (valores utilizáveis):")
    mostrar_diagnostico(antes, perfeitas_antes)

if __name__ == "__main__": 
    tratar()