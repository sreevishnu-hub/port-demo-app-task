# Port Demo App

## Project Overview
**Port Demo App**
It is a simple FastAPI-based application designed to demonstrate:
- Environment-based configuration (no hardcoded ports)  
- Containerization using Docker  
- Networking and port mapping with Docker Compose  
- CI/CD automation with GitHub Actions  
- Proper logging and health checks  
The application exposes two endpoints: `/` and `/health`, and clearly indicates which port it is listening on.

------------------------------------------------------------------
## Features
- Start an HTTP server with FastAPI  
- `/` endpoint: returns app name and listening port  
- `/health` endpoint: returns health status  
- Reads listening port from environment variable `APP_PORT`  
- Fails clearly if `APP_PORT` is not set  
- Logs to stdout/stderr  
- Containerized and deployable via Docker Compose  
- CI pipeline to build, tag, push, and verify the Docker image

------------------------------------------------------------------
## Technology Choice

**FastAPI + Python 3.11**
**Reasons:**

- Lightweight and fast  
- Easy to configure environment variables  
- Built-in validation and health endpoints  
- Simple to log to stdout

------------------------------------------------------------------
**How to Run With Docker**

docker-compose up

------------------------------------------------------------------
**How to Run Without Docker**

pip install -r requirements.txt
