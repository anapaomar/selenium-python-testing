import pytest
from util.db_config import create_db

# Fixture que se ejecuta antes de todas las pruebas, creando la base de datos si es necesario
@pytest.fixture(scope="session", autouse=True)
def setup_db():
    create_db()