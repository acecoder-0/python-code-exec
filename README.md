# Dockerized Python Code Execution Web Application with Kubernetes Deployment

A Flask-based web application that allows users to write and execute Python code in the browser. The application is containerized using Docker, shared through Docker Hub, version-controlled with GitHub, and deployed using Kubernetes.

## Features
- Web-based Python code editor
- Real-time Python code execution
- Output display in browser
- Dockerized deployment
- Docker Hub image sharing
- GitHub source code management
- Kubernetes deployment with replicas and service exposure

## Tech Stack
- Python
- Flask
- Docker
- Docker Hub
- GitHub
- Kubernetes

## Project Structure
- `app.py` - Flask backend
- `requirements.txt` - Python dependencies
- `Dockerfile` - Docker image instructions
- `deployment.yaml` - Kubernetes deployment file
- `service.yaml` - Kubernetes service file

## Run with Docker

### Build Docker image
```bash
docker build -t python-code-exec .
