import os
import sys
from fastapi import FastAPI

PORT = os.getenv("APP_PORT")

if not PORT:
    print("ERROR: APP_PORT environment variable is not set", file=sys.stderr)
    sys.exit(1)

app = FastAPI(title="Port Demo App")

@app.get("/")
def root():
    return {
        "app": "Port Demo App",
        "listening_port": PORT
    }

@app.get("/health")
def health():
    return {"status": "ok"}
