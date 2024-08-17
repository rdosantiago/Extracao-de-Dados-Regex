# Extracao-de-Dados-Regex
Este repositório contém um script Python para a extração automatizada de informações específicas a partir de um texto, utilizando expressões regulares. As informações extraídas são armazenadas em um DataFrame do pandas e posteriormente exportadas para um arquivo Excel.

# Funcionalidades
- Leitura de Arquivo: O script lê o conteúdo de um arquivo de texto.
- Extração de Dados: Utiliza expressões regulares para extrair informações específicas, como número do ofício, número do processo, juiz demandante, CPF/CNPJ, data de recepção, número do protocolo e ID de transferência.
- Armazenamento de Dados: Os dados extraídos são armazenados em um DataFrame do pandas.
- Exportação para Excel: O DataFrame é exportado para um arquivo Excel.

# Estrutura do Código
- Função extrair_dados: Responsável por aplicar expressões regulares no texto e retornar um dicionário com os dados extraídos.
- Leitura do Arquivo: O conteúdo do arquivo de texto é lido e armazenado em uma variável.
- Extração dos Dados: A função extrair_dados é chamada para processar o texto e extrair as informações.
- Criação do DataFrame: Um DataFrame do pandas é criado a partir dos dados extraídos.
- Exportação para Excel: O DataFrame é salvo em um arquivo Excel.

# Como Utilizar
#### 1) Clone este repositório.
#### 2) Coloque o arquivo de texto a ser processado no caminho especificado no script.
#### 3) Execute o script Python.
#### 4) O arquivo informacoes_extraidas.xlsx será gerado no diretório atual contendo as informações extraídas.

# Pré-requisitos
- Python 3.x
- Pandas

# Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

# Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.

