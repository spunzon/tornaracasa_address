import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2AuthorizationCodeBearer
from .routers import address, forms
from .database import create_db_and_tables
from contextlib import asynccontextmanager

if os.getenv("ENV") == "development":
    from dotenv import load_dotenv
    load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    title="Tornar a casa Address Validation API",
    description="Address validation API for people affected by Dana Valencia",
    version="0.1.0",
    lifespan=lifespan
)

origins = [
    "http://localhost:3000",
    # Agrega otros orígenes permitidos si es necesario
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(address.router)
app.include_router(forms.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
