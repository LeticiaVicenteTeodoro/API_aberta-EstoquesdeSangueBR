import uvicorn


def main():
    """Inicia a API localmente."""
    uvicorn.run("api_doacao_sangue.main:app", host="127.0.0.1", port=8000)
