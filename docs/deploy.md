# Instalação e execução

## Instalação local como pacote

Na raiz do projeto:

```bash
python -m pip install .
api-doacao-sangue
```

A documentação estará disponível em `/docs` e `/redoc` no endereço local `http://127.0.0.1:8000`.

## Hospedagem em servidor

A publicação do pacote Python e a hospedagem da API são etapas diferentes. A instalação permite que outro desenvolvedor execute a API em seu próprio ambiente. Para disponibilizá-la publicamente pela internet, ainda é necessário configurar um servidor/plataforma de hospedagem, variáveis de ambiente, banco de dados e processo de execução.

O servidor ASGI pode ser iniciado com:

```bash
uvicorn api_doacao_sangue.main:app --host 0.0.0.0 --port 8000
```
