# Deployment Guide

## Local Development

```bash
pip install .[dev]
uvicorn enterprise_rag.api:app --reload
```

## CLI Demo

```bash
ragctl demo
ragctl ask "What security controls are required?"
```

## Docker

```bash
docker build -t enterprise-rag .
docker run -p 8000:8000 enterprise-rag
```

## Docker Compose

```bash
docker-compose up --build
```

## Health Check

```bash
curl http://localhost:8000/health
```

## Ask Endpoint

```bash
curl -X POST http://localhost:8000/answer \
  -H 'Content-Type: application/json' \
  -d @sample_query.json
```
