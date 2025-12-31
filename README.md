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
**How to Run Without Docker**
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   
2. **Set up the environment**
   # For Python
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

   # For Node.js
   npm install
   
3. **Run the application**
   # Python example
   python app.py
   
   # Node.js example
   npm start

4. **Access the app**
   Open http://localhost:5000 (or your configured port) in your browser.

------------------------------------------------------------------
## How to Run with Docker Compose
1. Ensure Docker and Docker Compose are installed
2. Build and run containers
   docker-compose up --build
3. Access the app
   Open http://localhost:8080 (or mapped host port).
4. Stop containers
   docker-compose down

------------------------------------------------------------------
## Ports & Networking Explanation
App listens on: 5000 (internal container port)

## Why container port and host port differ:
Docker isolates container networks. Mapping the container port (5000) to host port (8080) allows multiple services to run on the same machine without conflicts.

## Docker Compose mapping:
ports:
  - "8080:5000"
This maps the host port 8080 to container port 5000. Requests to localhost:8080 are forwarded to the app inside the container.

------------------------------------------------------------------
## CI Pipeline Explanation
The CI pipeline automates building, testing, and deploying the application.

**Checkout Code** – Pulls the latest code from the repository.
**Install Dependencies** – Ensures the application has all necessary packages.
**Run Tests** – Validates functionality and prevents breaking changes.
**Build Docker Image** – Creates a container image for deployment.
**Tag Docker Image** – Tagged using:

username/project-name:latest
username/project-name:<commit-hash>

**Push Docker Image** – Uploaded to Docker Hub or a container registry.
**Deploy (Optional)** – Can deploy automatically to staging or production environments.

------------------------------------------------------------------
## Decisions & Tradeoffs

## Decision: Use Docker Compose for multi-container orchestration
   **Reason**  : Simplifies local development and mirrors production architecture.
   **Tradeoff**: Slightly higher complexity for initial setup.
## Decision: Map container port 5000 to host port 8080
   **Reason**  : Avoids conflicts with other local services.
   **Tradeoff**: Users need to remember host port mapping.
## Decision: Tag Docker images with commit hash
   **Reason**  : Ensures reproducibility and traceability in CI/CD pipeline.
   **Tradeoff**: Requires automated tagging in CI pipeline.
