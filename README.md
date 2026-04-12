# JuryScan Agent Service

Serviço de orquestração de agentes de IA do projeto JuryScan com `CrewAI` e `FastAPI`. Responsável pela análise automática de documentos CNIS utilizando múltiplos agentes especializados.

## 📚 Sumário

- [Descrição Geral](#-descrição-geral)
- [Dependências](#️-dependências)
- [Execução Local](#-execução-local)
- [Documentação da API](#-documentação-da-api)
- [Autenticação](#-autenticação)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Testes](#️-testes)

## 📄 Descrição Geral

Este serviço implementa uma arquitetura multi-agente para análise inteligente de documentos CNIS (Cadastro Nacional de Informações Sociais). Utiliza:

- **CrewAI**: Framework para orquestração de agentes de IA
- **FastAPI**: Framework web moderno para Python
- **Google Gemini**: Modelo de linguagem para os agentes
- **PDFPlumber**: Extração de texto de PDFs

O serviço expõe uma API REST com autenticação via API Key para permitir que aplicações externas solicitem análises de documentos.

## 🛠️ Dependências

### Requisitos do Sistema
- Python 3.10+
- pip (gerenciador de pacotes Python)

### Dependências Python

As principais dependências do projeto:

- **crewai**: Orquestração e gerenciamento de agentes de IA
- **fastapi**: Framework web para a API REST
- **uvicorn**: Servidor ASGI
- **pydantic**: Validação de dados e schemas
- **pdfplumber**: Extração de texto de documentos PDF

## 🚀 Execução Local

### 1. Clonar o Repositório

```bash
git clone https://github.com/JuryScan/JuryScan-agents-service.git \\
cd JuryScan-agents-service
```

### 2. Criar Ambiente Virtual

```bash
python -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
# Google Gemini API
GOOGLE_API_KEY=sua_chave_google_gemini_aqui
LLM_MODEL=gemini-2.5-flash

# Autenticação
API_KEY=sua_chave_secreta_muito_segura_aqui_minimo_32_caracteres
```

**Onde obter as chaves:**
- `GOOGLE_API_KEY`: [Google AI Studio](https://aistudio.google.com)
- `API_KEY`: Gere uma string aleatória (use ferramentas como `openssl rand -hex 32`)

### 5. Executar em Desenvolvimento

```bash
fastapi dev
```

Ou com uvicorn:

```bash
uvicorn src.app:app --reload
```

## 📖 Documentação da API

Após iniciar o serviço, acesse a documentação interativa no **Swagger UI**, no endpoint `http://localhost:8000/docs`

A documentação permite testar todos os endpoints diretamente no navegador.

## 🔐 Autenticação

O serviço utiliza **API Key via Header HTTP** para autenticação.

### Uso no Swagger UI

1. Acesse `http://localhost:8000/docs`
2. Clique no botão **"Authorize"** no topo direito
3. Coloque sua chave: `sua_chave_secreta_muito_segura_aqui_minimo_32_caracteres`
4. Clique em "Authorize"
5. Agora todas as requisições incluirão o header automaticamente

## 📁 Estrutura do Projeto

```
JuryScan-agents-service/
├── main.py              # Ponto de entrada da aplicação
├── requirements.txt     # Dependências Python
├── README.md            # Este arquivo
├── src/                 # Código-fonte principal
├── config/              # Configurações dos agentes (YAML)
├── knowledge/           # Base de conhecimento dos agentes
└── tests/               # Testes unitários
```

### Production Local

Para rodar em produção localmente:

```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker src.app:app --bind 0.0.0.0:8000
```

## 🧪 Testes

```bash
# Executar testes
pytest tests/

# Com cobertura
pytest --cov=src tests/
```