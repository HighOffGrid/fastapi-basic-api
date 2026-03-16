# FastAPI Basic API

API simples desenvolvida com FastAPI para estudo de desenvolvimento backend com Python.

---

Tecnologias:
	•	Python
	•	FastAPI
	•	Pydantic
	•	Uvicorn

---

Funcionalidades:
	•	API REST básica
	•	Estrutura inicial para aplicações FastAPI
	•	Documentação automática com Swagger

---

## Arquitetura


Client
   │
   ▼
FastAPI Routes
   │
   ▼
Pydantic Schemas
   │
   ▼
Response

---

## Objetivo


Este projeto foi criado para estudo da framework FastAPI e desenvolvimento de APIs REST em Python.

---

## Rodando o projeto

```bash
Instale as dependências:

pip install -r requirements.txt

---

## Executando a API

uvicorn app.main:app --reload

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc
