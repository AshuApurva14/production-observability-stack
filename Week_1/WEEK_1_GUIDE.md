# 📊 Production Observability Stack

## 🚀 Week 1 – Metrics Foundation (Prometheus + Grafana)

This project demonstrates the fundamentals of monitoring and observability by implementing:

- FastAPI backend with custom Prometheus metrics
- Prometheus for scraping and storing metrics
- Grafana for visualization
- Docker Compose for local orchestration

---

# 🎯 Objective

Build a backend service that:

- Exposes `/metrics` endpoint
- Is scraped by Prometheus
- Visualizes RED metrics in Grafana
- Simulates real-world latency and errors

---

# 🏗 Architecture (Week 1)




---

# 📁 Project Structure

```bash
production-observability-stack/
│
├── app/
│ └── backend/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── monitoring/
│ └── prometheus/
│ └── prometheus.yml
│
├── docker-compose.yml
└── README.md
```


---

# 🧠 Concepts Covered

## 1️⃣ Prometheus Metric Types

- Counter → Total requests
- Counter → Error count
- Histogram → Request latency

## 2️⃣ RED Method

- **Rate** → Request rate
- **Errors** → Error rate
- **Duration** → Latency (95th percentile)

## 3️⃣ Pull-Based Monitoring

Prometheus scrapes the `/metrics` endpoint every 5 seconds.

---

# ⚙️ How to Run

## 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd production-observability-stack

## 2️⃣ Start Service

```bash
docker compose up --build
```

## 3️⃣ Access Services

```bash
| Service    | URL                                                            |
| ---------- | -------------------------------------------------------------- |
| Backend    | [http://localhost:8000](http://localhost:8000)                 |
| Metrics    | [http://localhost:8000/metrics](http://localhost:8000/metrics) |
| Prometheus | [http://localhost:9090](http://localhost:9090)                 |
| Grafana    | [http://localhost:3000](http://localhost:3000)                 |

```

Grafana Default login:

```bash
admin / admin
```

## 📊 Grafana Setup

- Go to Connections → Data Sources

- Add Prometheus

- Set URL:

```bash
http://prometheus:9090

```

- Access Mode → Server

- Click Save & Test

