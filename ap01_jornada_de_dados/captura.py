import shutil
from datetime import date
import pandas as pd
import config

def capturar():
  config.preparar_pastas()
  origem = config.ENTRADA / config.ARQUIVO
  if not origem.exists():
    raise SystemExit(f'Baixe o arquivo do Kaggle e salve em: {origem}')
  destino = config.RAW / f'vendas_{date.today()}.csv'
  if destino.exists():
    print('O arquivo de hoje já foi capturado:', destino.name)
  else:
    shutil.copy(origem, destino)
    print('Arquivo capturado: ', destino.name)
  
  linhas = len(pd.read_csv(destino))
  tamanho = destino.stat().st_size / 1024
  print(f'{config.br(linhas)} linhas, {config.br(tamanho, 1)} KiB')
  return {'resumo': [f'{config.br(linhas)} linhas', 'somente leitura']}

if __name__ == '__main__':
  capturar()
  