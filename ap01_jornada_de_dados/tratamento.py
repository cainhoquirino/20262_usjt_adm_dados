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

def tratar():
    bronze = pd.read_parquet(c.BRONZE / "vendas.parquet")
    antes, perfeitas_antes= diagnosticar(bronze.rename(columns=NOMES))
    print("Diagnóstico da camada bronze (valores utilizáveis):")
    mostrar_diagnostico(antes, perfeitas_antes)

if __name__ == "__main__": 
    tratar()