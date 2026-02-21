# production-observability-stack

This is a production grade observability stack bulit using prometheus, grafana, Loki, opentelemetry and python.



🎯 WEEK 1 GOAL
---

You will learn:

- What metrics look like?

- How Prometheus scrapes?

- Counters vs Gauges vs Histograms

- RED method (Rate, Errors, Duration)

We will Build:

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

## Challenges and Issues faced

### Error:

1.**Connection refused**

2.**Error scraping target:**  received unsupported Content-Type "application/json" and no fallback_scrape_protocol specified for target

```bash
 time=2026-02-21T14:59:55.989Z level=ERROR source=scrape.go:1631 msg="Failed to determine correct type of scrape target." component="scrape manager" scrape_pool=backend-app target=http://backend:8000/metrics content_type=application/json fallback_media_type="" err="received unsupported Content-Type \"application/json\" and no fallback_scrape_protocol specified for target"
grafana-1     | logger=dashboard-service t=2026-02-21T14:59:57.791322866Z level=info msg="No last resource version found, starting from scratch" orgID=1
backend-1     | INFO:     172.18.0.4:39530 - "GET /metrics HTTP/1.1" 200 OK
prometheus-1  | time=2026-02-21T15:00:00.989Z level=ERROR source=scrape.go:1631 msg="Failed to determine correct type of scrape target." component="scrape manager" scrape_pool=backend-app target=http://backend:8000/metrics content_type=application/json fallback_media_type="" err="received unsupported Content-Type \"application/json\" and no fallback_scrape_protocol specified for target"
backend-1     | INFO:     172.18.0.4:39530 - "GET /metrics HTTP/1.1" 200 OK
prometheus-1  | time=2026-02-21T15:00:05.990Z level=ERROR source=scrape.go:1631 msg="Failed to determine correct type of scrape target." component="scrape manager" scrape_pool=backend-app target=http://backend:8000/metrics content_type=application/json fallback_media_type="" err="received unsupported Content-Type \"application/json\" and no fallback_scrape_protocol specified for target"
backend-1     | INFO:     172.18.0.4:39530 - "GET /metrics HTTP/1.1" 200 OK
prometheus-1  | time=2026-02-21T15:00:10.990Z level=ERROR source=scrape.go:1631 msg="Failed to determine correct type of scrape target." component="scrape manager" scrape_pool=backend-app target=http://backend:8000/metrics content_type=application/json fallback_media_type="" err="received unsupported Content-Type \"application/json\" and no fallback_scrape_protocol specified for target"
backend-1     | INFO:     172.18.0.4:39530 - "GET /metrics HTTP/1.1" 200 OK
prometheus-1  | time=2026-02-21T15:00:15.989Z level=ERROR source=scrape.go:1631 msg="Failed to determine correct type of scrape target." component="scrape manager" scrape_pool=backend-app target=http://backend:8000/metrics content_type=application/json fallback_media_type="" err="received unsupported Content-Type \"application/json\" and no fallback_scrape_protocol specified for target"
backend-1     | INFO:     172.18.0.4:39530 - "GET /metrics HTTP/1.1" 200 OK
prometheus-1  | time=2026-02-21T15:00:20.991Z level=ERROR source=scrape.go:1631 msg="Failed to determine correct type of scrape target." component="scrape manager" scrape_pool=backend-app target=http://backend:8000/metrics content_type=application/json fallback_media_type="" err="received unsupported Content-Type \"application/json\" and no fallback_scrape_protocol specified for target"
```

### Common Issue

- Your /metrics endpoint might not return proper content-type.

- Your FastAPI metrics route should be:


### When target is DOWN, always check in order:

- Container running?
```bash
docker ps
```

- Service reachable?

```bash
docker exec -it prometheus sh
wget http://backend:8000/metrics

```

- Correct target?

- Correct content type?

- YAML indentation?
