# production-observability-stack

This is a production grade observability stack bulit using prometheus, grafana, Loki, opentelemetry and python.



🎯 WEEK 1 GOAL
---

Build:

```bash
FastAPI App → Expose Metrics → Prometheus → Grafana Dashboard
```

## Project Strtucture for Week 1 Goal

```bash
production-observability-stack/
│
├── app/
│   └── backend/
│       ├── app.py
│       ├── requirements.txt
│       └── Dockerfile
│
├── monitoring/
│   ├── prometheus/
│   │   └── prometheus.yml
│   └── grafana/
│
├── dashboards/
│
├── scripts/
│
└── docker-compose.yml
```

