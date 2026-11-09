from datetime import datetime
import pandas as pd
import config

def arquivo_mais_recente():
  arquivos = sorted(config.RAW.glob("vendas_*.csv"))
  return arquivos[-1]

def ingerir():
  arquivo = arquivo_mais_recente()
  bronze = pd.read_csv(arquivo, dtype=str)
  bronze['_arquivo'] = arquivo.name
  bronze['_ingerido_em'] = datetime.now().strftime('%Y-%m-%d %H:%M')
  bronze.to_parquet(config.BRONZE/'vendas.parquet', index=False)
  print(f'Camada bronze: {config.br(len(bronze))} linhas gravadas')
  return{'resumo': [f'{config.br(len(bronze))} linhas', 'sem correções']}

if __name__ == '__main__':
  ingerir()
  print(
    pd.read_parquet(config.BRONZE / 'vendas.parquet').iloc[0]
  )