import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from celery import Celery
from dotenv import load_dotenv
from crypto.coingecko.coingecko_client import CoinGeckoClient
from crypto.crypto_repository import CryptoRepository
from worker.worker_container import WorkerContainer
from dependency_injector.wiring import Provide, inject

load_dotenv()

redis_host = os.getenv("REDIS_HOST")
redis_port = os.getenv("REDIS_PORT")

broker_url = f"rediss://{redis_host}:{redis_port}/0?ssl_cert_reqs=CERT_NONE"
backend_url= f"rediss://{redis_host}:{redis_port}/1?ssl_cert_reqs=CERT_NONE"

app = Celery(broker=broker_url, backend=backend_url)
worker_container = WorkerContainer()
worker_container.wire(modules=[__name__])

@app.on_after_configure.connect
def setup_periodic_tasks(sender: Celery, **kwargs):
    sender.add_periodic_task(60.0, updateCurrencies.s(None), name="Update crypto currencies")

@app.task()
@inject
def updateCurrencies(
    _, 
    coingecko_client: CoinGeckoClient = Provide[WorkerContainer.coingecko_client],
    crypto_repository: CryptoRepository = Provide[WorkerContainer.crypto_repository]
):
    print("HERE !", coingecko_client, crypto_repository)


