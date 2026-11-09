import pandas as pd
import config

def comparar_formatos():
    csv = sorted(config.RAW.glob("vendas_*.csv"))[-1]
    parquet = config.BRONZE / "vendas.parquet"
    kib_csv = csv.stat().st_size /1024
    kib_parquet = parquet.stat().st_size /1024
    print(f'CSV(raw): {config.br(kib_csv, 1)} KiB')
    print(f'Parquet(bronze): {config.br(kib_parquet, 1)} KiB')
    print(f'{config.br(100 * kib_parquet / kib_csv)}% do CSV')

def inventario():
    copias = []
    for arquivo in sorted(config.DADOS.glob("*/*")):
        if arquivo.suffix == ".csv":
            linhas = len(pd.read_csv(arquivo))
        elif arquivo.suffix == ' parquet':
            linhas = len(pd.read_parquet(arquivo))
        else:
            continue 
        copias.append({"pasta": arquivo.parent.name, "arquivo": arquivo.name, "linhas": linhas})
    return pd.DataFrame(copias)

def mostrar_inventario(copias):
    for _, copia in copias.iterrows():
        print(f'{copia["pasta"]}, {copia["arquivo"]} {config.br(copia["linhas"])} linhas')

def armazenar():
    comparar_formatos()
    copias = inventario()
    mostrar_inventario(copias)
    detalhe = copias[copias["pasta"] != "gold"]
    alerta = "fica exposto" if len(detalhe) > 1 else None
    return {"resumo":[f"{len(detalhe)} cópias do detalhe", "CSV e Parquet"], "alerta": alerta}

if __name__ == "__main__":
    armazenar()

