    
# Análise de Documentos Anti-Fraude com Azure AI

## 📝 Descrição

Este projeto é uma aplicação web desenvolvida como parte de um laboratório do bootcamp da DIO (Digital Innovation One). A solução utiliza a Azure AI para analisar documentos de identidade (como CNHs) enviados pelo usuário, extrair as informações e verificar a autenticidade, atuando como um sistema anti-fraude.

A aplicação permite o upload de um documento, que é armazenado no Azure Blob Storage e, em seguida, processado pelo serviço Azure AI Document Intelligence para extrair dados e assinaturas, exibindo o resultado da análise em uma página web.

## ✨ Funcionalidades

*   **Upload de Documentos**: Interface web para o usuário enviar um arquivo de imagem (ex: CNH).
*   **Armazenamento em Nuvem**: O documento enviado é salvo de forma segura em um container no Azure Blob Storage.
*   **Análise com IA**: Utiliza o Azure AI Document Intelligence para extrair e analisar os campos do documento.
*   **Exibição de Resultados**: Apresenta os dados extraídos e o resultado da análise em uma página de fácil visualização.

## 🤖 Tecnologias Utilizadas

*   **Backend**: Python, Flask
*   **Frontend**: HTML, CSS (Bootstrap)
*   **Cloud**:
    *   Azure AI Document Intelligence
    *   Azure Blob Storage
*   **Bibliotecas Python**:
    *   `flask`
    *   `azure-storage-blob`
    *   `azure-ai-formrecognizer`
    *   `python-dotenv`

## 🚀 Como Executar o Projeto

### Pré-requisitos

*   Python 3.10+
*   Uma conta no Azure com acesso aos serviços:
    *   Azure AI Document Intelligence
    *   Azure Storage Account

### 1. Clone o Repositório

```bash
git clone https://github.com/GilliardF/DIO_Document_Anti_Fraude.git
cd DIO_Document_Anti_Fraude
```
  

2. Crie e Ative um Ambiente Virtual
code Bash

    
# Para Windows
python -m venv venv
venv\Scripts\activate

# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate

  

3. Instale as Dependências
code Bash

    
pip install -r requirements.txt

  

4. Configure as Variáveis de Ambiente

Crie um arquivo chamado .env na raiz do projeto e preencha com as suas credenciais do Azure:
code Env

    
ENDPOINT="SEU_ENDPOINT_DO_DOCUMENT_INTELLIGENCE"
SUBSCRIPTION_KEY="SUA_CHAVE_DO_DOCUMENT_INTELLIGENCE"
AZURE_STORAGE_CONNECTION_STRING="SUA_CONNECTION_STRING_DO_BLOB_STORAGE"
CONTAINER_NAME="NOME_DO_SEU_CONTAINER_DE_BLOB"

  

5. Execute a Aplicação
code Bash

    
flask run

  

Acesse a aplicação em http://127.0.0.1:5000 no seu navegador.
📁 Estrutura do Projeto
code Code

    
.
├── src/
│   ├── services/             # Módulos para interagir com serviços externos (Azure)
│   │   ├── blob_service.py
│   │   └── document_intelligence_service.py
│   ├── templates/            # Arquivos HTML
│   │   ├── index.html
│   │   └── result.html
│   ├── utils/                # Utilitários e configurações
│   │   └── Config.py
│   └── app.py                # Arquivo principal da aplicação Flask
├── .gitignore
├── requirements.txt          # Dependências do projeto
└── README.md                 # Este arquivo

  
