

# DevOps Task Manager

A complete end-to-end DevOps project demonstrating application development, containerization, CI/CD automation, Docker image management, and Kubernetes deployment.

## Project Overview

DevOps Task Manager is a Flask-based web application that allows users to create, view, update, and delete tasks. The project was built to gain hands-on experience with modern DevOps tools and practices.

The application is containerized using Docker, integrated with Jenkins for Continuous Integration, stored in Docker Hub, and deployed on Kubernetes using Minikube.

---

## Features

* Create Tasks
* View Tasks
* Update Task Status
* Delete Tasks
* SQLite Database Integration
* Docker Containerization
* Jenkins CI Pipeline
* Docker Hub Integration
* Kubernetes Deployment
* Kubernetes Service Exposure
* ConfigMap-based Configuration

---

## Architecture

```text
Developer
    |
    v
 GitHub
    |
    v
 Jenkins Pipeline
    |
    v
 Docker Build
    |
    v
 Docker Hub
    |
    v
 Kubernetes Deployment
    |
    v
 Task Manager Application
```

---

## Tech Stack

### Programming & Scripting

* Python
* Bash

### Web Framework

* Flask

### Database

* SQLite

### Version Control

* Git
* GitHub

### Containerization

* Docker
* Docker Hub

### CI/CD

* Jenkins

### Container Orchestration

* Kubernetes
* Minikube

### Operating System

* Linux (Ubuntu/WSL)

---

## Project Structure

```text
devops-task-manager/

├── app/
│   ├── app.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── create.html
│   │   ├── tasks.html
│   │   └── update.html
│
├── database/
│   └── init_db.py
│
├── kubernetes/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── configmap.yaml
│
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Local Setup

### Clone Repository

```bash
git clone https://github.com/HARISH07-1/devops-task-manager.git

cd devops-task-manager
```

### Create Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app/app.py
```

Open:

```text
http://localhost:5000
```

---

## Docker Setup

### Build Image

```bash
docker build -t task-manager:v1 .
```

### Run Container

```bash
docker run -d -p 5000:5000 --name task-manager task-manager:v1
```

Access:

```text
http://localhost:5000
```

---

## Jenkins CI Pipeline

The Jenkins pipeline automates:

* Source Code Checkout
* Docker Image Build
* Docker Hub Authentication
* Docker Image Push

### Pipeline Flow

```text
GitHub
   ↓
Jenkins
   ↓
Docker Build
   ↓
Docker Hub Push
```

---

## Docker Hub

Docker images are pushed automatically through Jenkins.

Example:

```text
harishhh07/task-manager:<build-number>
```

---

## Kubernetes Deployment

### Apply Kubernetes Resources

```bash
kubectl apply -f kubernetes/
```

### Verify Deployment

```bash
kubectl get pods

kubectl get svc
```

### Access Application

```bash
minikube service task-manager-service
```

---

## Kubernetes Resources

### Deployment

* Replica Count: 2
* Docker Hub Image Pull
* Container Port: 5000

### Service

* NodePort Service
* External Access to Application

### ConfigMap

Used to externalize application configuration.

---

## CI/CD Workflow

```text
Developer Pushes Code
        ↓
GitHub Repository
        ↓
Jenkins Pipeline Trigger
        ↓
Docker Image Build
        ↓
Docker Hub Push
        ↓
Kubernetes Deployment Update
```

---

## Learning Outcomes

* Git & GitHub Workflow
* Docker Containerization
* Jenkins CI/CD Automation
* Docker Hub Image Management
* Kubernetes Deployments
* Kubernetes Services
* ConfigMaps
* Troubleshooting Containers and Pods
* Linux Administration Basics
* Infrastructure Automation Concepts

---

## Future Improvements

* Prometheus Monitoring
* Grafana Dashboards
* Kubernetes Health Checks
* Persistent Volumes
* PostgreSQL Integration
* Kubernetes Secrets
* Ingress Controller
* Automated Kubernetes Deployment via Jenkins

---

## Author

Harish

GitHub:
https://github.com/HARISH07-1

---

## License

This project is created for learning and portfolio purposes.

