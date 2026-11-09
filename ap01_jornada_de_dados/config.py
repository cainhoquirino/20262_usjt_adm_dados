from pathlib import Path
RAIZ = Path(__file__).parent
DADOS = RAIZ / "dados"
ENTRADA = DADOS / "entrada"
RAW = DADOS / "raw"
BRONZE = DADOS / "bronze"
SILVER = DADOS / "silver"
GOLD = DADOS / "gold"
SAIDAS = DADOS / "saidas"

ARQUIVO = "dirty_cafe_sales.csv"

SLA_FRESCOR_DIAS = 1 #dias
RETENCAO_MESES = 6 #meses

def preparar_pastas():
  for pasta in [ENTRADA, RAW, BRONZE, SILVER, GOLD, SAIDAS]:
    pasta.mkdir(parents=True, exist_ok=True)
    
#12456,78
def br(numero, casas=0):
  texto = f"{numero:,.{casas}f}"
  #12.345,67
  return texto.replace(",", "_").replace(".", ",").replace("_", ".")

def moeda(valor):
  return "US$" + br(valor, 2)

if __name__ == "__main__":
  preparar_pastas()
  print("Pastas criadas em", DADOS)