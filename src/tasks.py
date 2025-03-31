import os
from crypto.crypto_repository import CryptoRepository
from db.database import Database
from celery import Celery
from dotenv import load_dotenv
from crypto.coingecko.coingecko_client import CoinGeckoClient

load_dotenv()

redis_host = os.getenv("REDIS_HOST")
redis_port = os.getenv("REDIS_PORT")

broker_url = f"redis://{redis_host}:{redis_port}/0"
backend_url= f"redis://{redis_host}:{redis_port}/0"

app = Celery(broker=broker_url, backend=backend_url)
app.conf.broker_connection_retry_on_startup = True

coingecko_client = CoinGeckoClient(api_key=os.getenv("COINGECKO_API_KEY"), base_url=os.getenv("COINGECKO_BASE_URL"))


@app.on_after_configure.connect
def setup_periodic_tasks(
    sender: Celery,     
    **kwargs
):
    sender.add_periodic_task(1.0, updateCurrencies.s(), name="Update crypto currencies")

@app.task()
def updateCurrencies():  
    database = Database(url=os.getenv("DATABASE_URL"))
    repository = CryptoRepository(session=database.get_session())
    
    crypto_currencies = repository.get_many()

    print(crypto_currencies[0])
    

