from fastapi import FastAPI, Request, Response
from prometheus_client import Counter, Histogram, generate_latest
from prometheus_client import CONTENT_TYPE_LATEST
import time
import random

app = FastAPI()

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of requests",
    ["method", "endpoint"]
)

REQUEST_LATENCY = Histogram(
    "app_request_latency_seconds",
    "Request latency",
    ["endpoint"]
)

ERROR_COUNT = Counter(
    "app_errors_total",
    "Total errors",
    ["endpoint"]
)

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    latency = time.time() - start_time

    REQUEST_COUNT.labels(request.method, request.url.path).inc()
    REQUEST_LATENCY.labels(request.url.path).observe(latency)

    if response.status_code >= 400:
        ERROR_COUNT.labels(request.url.path).inc()

    return response

@app.get("/")
def home():
    if random.random() < 0.2:
        return {"message": "Random slow response"}
    time.sleep(random.random())
    return {"message": "Hello Observability"}

@app.get("/metrics")
def metrics():
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)