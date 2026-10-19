# Assistente de IA

Projeto de estudo em Python: uma interface de chat com Streamlit integrada à API Gemini por meio do SDK Google Gen AI.

## Funcionalidades

- Envio de mensagens e exibição de respostas na interface de chat.
- Histórico de mensagens durante a sessão do Streamlit.
- Configuração da chave da API por variável de ambiente.

## Tecnologias

Python · Streamlit · Google Gen AI · python-dotenv

## Executar localmente

Com Python instalado:

```bash
git clone https://github.com/gabriza007/IA.git
cd IA
python -m venv .venv
```

Ative o ambiente virtual:

```powershell
# Windows / PowerShell
.\.venv\Scripts\Activate.ps1
```

```bash
# Linux / macOS
source .venv/bin/activate
```

Instale as dependências:

```bash
python -m pip install streamlit google-genai python-dotenv
```

Crie um arquivo `.env` na raiz com sua própria chave:

```dotenv
CHAVE_API=sua_chave_da_api_gemini
```

Inicie a aplicação:

```bash
python -m streamlit run IA1.py
```

O modelo configurado no código é `gemini-2.5-flash`. A execução depende de uma chave válida, da disponibilidade do modelo e das cotas da API. O histórico fica na sessão, sem persistência em banco de dados.

## Objetivo de aprendizado

Praticar integração com APIs, variáveis de ambiente, estado de sessão e interfaces interativas em Python.

[Gabriel Ribeiro](https://github.com/gabriza007)
