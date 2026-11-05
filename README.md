# API Aberta de Doação de Sangue

API REST para integração, padronização e disponibilização de dados públicos sobre doação de sangue no Brasil.

## Instalação como pacote Python

Requer Python 3.10 ou superior.

```bash
python -m venv .venv
```

Ative o ambiente virtual:

- Windows: `.venv\\Scripts\\activate`
- Linux/macOS: `source .venv/bin/activate`

Instale diretamente do diretório do projeto:

```bash
python -m pip install .
```

## Execução

Depois da instalação, inicie a API com:

```bash
api-doacao-sangue
```

Alternativamente:

```bash
python -m api_doacao_sangue
```

A API ficará disponível localmente em `http://127.0.0.1:8000`.

- Documentação Swagger: `http://127.0.0.1:8000/docs`
- Documentação ReDoc: `http://127.0.0.1:8000/redoc`

Para desenvolvimento, também é possível executar:

```bash
uvicorn api_doacao_sangue.main:app --reload
```

## Banco de dados

Por padrão, o SQLite cria o arquivo `api_doacao_sangue.db` no diretório de execução. Para configurar outro banco compatível com SQLAlchemy, defina a variável de ambiente `DATABASE_URL`.

Exemplo no PowerShell:

```powershell
$env:DATABASE_URL="sqlite:///./meu_banco.db"
```

Exemplo no Linux/macOS:

```bash
export DATABASE_URL="sqlite:///./meu_banco.db"
```

## Funcionalidades

- CRUD de hemocentros, estoques, campanhas e fontes de dados
- Consulta de compatibilidade sanguínea
- Integrações com Hemominas (MG), HEMOSC (SC), HEMEPAR (PR), HEMOES (ES), HEMOCE (CE), HEMOPA (PA), HEMOBA (BA) e HEMOSUL (MS)
- Consulta nacional de estoques
- Atualização agendada para as integrações configuradas no scheduler

## Observações

- A instalação do pacote não hospeda a API na internet. Ela executa o servidor no computador ou ambiente do próprio usuário.
- A coleta da Hemominas utiliza Selenium; para essa integração, também é necessário ter um navegador compatível e seu WebDriver configurados no ambiente.
- O scheduler atual está configurado para executar atualizações de Hemominas, HEMOSC e HEMEPAR.
- O projeto utiliza SQLite por padrão. Cada instalação mantém seu próprio banco local, salvo configuração diferente por `DATABASE_URL`.

## Tecnologias

Python, FastAPI, SQLAlchemy, SQLite, APScheduler, Requests, BeautifulSoup e Selenium.
