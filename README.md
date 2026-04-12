# Dockerized Python Code Execution Web Application with CI/CD and Kubernetes Deployment

## Project Overview
This project is a Flask-based web application that allows users to write and execute Python code through a browser interface. The application is containerized using Docker, pushed to Docker Hub, managed in GitHub, automated with GitHub Actions CI/CD, and deployed using Kubernetes.

It demonstrates the integration of development and DevOps tools in a single project.

---

## Objectives
- Build a web-based Python code execution platform
- Containerize the application using Docker
- Push and pull the Docker image using Docker Hub
- Store and manage source code with GitHub
- Automate Docker image build and push using GitHub Actions
- Deploy the application using Kubernetes with replicas and service exposure

---

## Tech Stack
- Python
- Flask
- Docker
- Docker Hub
- GitHub
- GitHub Actions
- Kubernetes

---

## Project Files
- `app.py` – Flask backend for code execution
- `requirements.txt` – Python dependencies
- `Dockerfile` – Docker image build instructions
- `deployment.yaml` – Kubernetes deployment file
- `service.yaml` – Kubernetes service file
- `.github/workflows/docker-image.yml` – GitHub Actions CI/CD workflow

---

## Working of the Project
1. The user opens the web application in the browser.
2. The user writes Python code in the text area.
3. The Flask backend receives the code through a POST request.
4. The application executes the code and captures the output.
5. The output is displayed back in the browser.

---

## Docker Implementation
The application was containerized using Docker.

### Build Docker Image
```bash
docker build -t python-code-exec .
