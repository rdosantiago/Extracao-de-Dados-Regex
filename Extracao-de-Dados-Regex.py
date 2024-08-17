import re
import pandas as pd

# Função para extrair dados
def extrair_dados(texto):
    padroes = {
        "Número do Ofício": r"Número do protocolo:\s*(\d+)",
        "Número do Processo": r"^(?:.*\n){5}([0-9\-.]{25})",
        "Juiz Demandante": r"^(?:.*\n){6}(.*?)\s+protocolado",
        "CPF/CNPJ": r"^(?:.*\n){21}(\d+)\s*:",
        "Data da Recepção": r"^(?:.*\n){3}(\d{2}/\d{2}/\d{4})",
        "Número do Protocolo": r"Número do protocolo:\s*(\d+)",
        "Transferência ID": r"Transferência de Valor ID:\s*\n(\d{18})"
    }
    
    dados = {}
    

    for chave, padrao in padroes.items():
        correspondencia = re.search(padrao, texto, re.MULTILINE)
        if correspondencia:
            dados[chave] = correspondencia.group(1)
    
    return dados

# Caminho do arquivo
caminho_arquivo = r"C:\Users\rdosa\source\repos\PythonApplication3\resultado.txt"

# Lendo o conteúdo do arquivo 
with open(caminho_arquivo, 'r', encoding='utf-8') as file:
    texto = file.read()


# Extração dos dados
dados_extraidos = extrair_dados(texto)

# Criação do DataFrame
df = pd.DataFrame([dados_extraidos])

# Salvando em um arquivo xlsx
df.to_excel("informacoes_extraidas.xlsx", index=False)

print("As informações foram salvas no arquivo informacoes_extraidas.xlsx")
