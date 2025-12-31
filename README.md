# Port Demo App

## Project Overview
This project demonstrates a containerized FastAPI application with a strong focus on ports, environment-based configuration, and CI/CD automation.

The application exposes two HTTP endpoints and runs entirely based on environment variables, making it suitable for cloud-native deployments.

---

## How to Run Without Docker

```bash
export APP_PORT=8000
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port $APP_PORT
