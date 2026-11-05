
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api_doacao_sangue.database import engine
from api_doacao_sangue.models import Base
from api_doacao_sangue.scheduler import iniciar_scheduler

from api_doacao_sangue.routes import (
    hemocentros,
    estoques,
    campanhas,
    compatibilidade,
    cidades,
    fontes,
    integracoes
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Aberta de Doação de Sangue",
    description="API para integração, padronização e disponibilização de dados sobre doação de sangue.",
    version="1.0.0"
)

# Configuração CORS para permitir a comunicação com o Vida+
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    iniciar_scheduler()

app.include_router(fontes.router)
app.include_router(integracoes.router)
app.include_router(hemocentros.router)
app.include_router(estoques.router)
app.include_router(campanhas.router)
app.include_router(compatibilidade.router)
app.include_router(cidades.router)


@app.get("/")
def home():
    return {
        "mensagem": "API Doação de Sangue funcionando!",
        "documentacao": "/docs"
    }
