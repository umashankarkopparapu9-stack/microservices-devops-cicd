# Microservices DevOps CI/CD Automation

## Project Overview

This project demonstrates an end-to-end DevOps workflow for deploying and managing three containerized microservices using GitHub, Docker, Jenkins, Terraform, AWS, Prometheus and Grafana.

The project focuses on containerization, CI/CD automation, cloud infrastructure provisioning, deployment and monitoring.

## Application Services

The repository contains three sample microservices:

| Service | Description | Port |
|---|---|---|
| User Service | Provides user information | 5000 |
| Product Service | Provides product information | 5000 |
| Order Service | Provides order information | 5000 |

**Note:** The trainer did not provide application source code. These minimal Flask applications were created as sample services to demonstrate the DevOps assignment requirements. They are not trainer-provided applications.

## Project Architecture

- GitHub: Source code management and branch workflow.
- Docker: Containerizes the microservices.
- Docker Compose: Runs multiple containers together.
- Nginx: Acts as a reverse proxy.
- Jenkins: CI/CD automation.
- Terraform: AWS infrastructure provisioning.
- AWS: Cloud deployment and container image storage.
- Prometheus: Metrics collection.
- Grafana: Monitoring dashboards.

## Repository Structure

```text
microservices-devops-cicd/
├── docker/
│   └── nginx/
│       └── nginx.conf
├── services/
│   ├── user-service/
│   ├── product-service/
│   └── order-service/
├── jenkins/
├── terraform/
├── monitoring/
│   ├── prometheus/
│   └── grafana/
├── docs/
├── docker-compose.yml
└── README.md

```

## Local Setup

### Prerequisites
- Git
- Docker Desktop
- Docker Compose

### Start the application
```bash
docker compose up -d --build
```

### Check running containers
```bash
docker compose ps
```


### Application Endpoints

| Endpoint | Purpose |
|---|---|
| http://localhost:8081/users | User Service |
| http://localhost:8081/products | Product Service |
| http://localhost:8081/orders | Order Service |
| http://localhost:8081/health | Nginx health check |

## Git Workflow

- `main`: Stable project branch.
- `develop`: Development branch.
- Feature changes are committed to `develop`.
- Pull requests are merged into `main`.

## Project Status

- [x] GitHub repository and branch workflow
- [x] Three sample microservices
- [x] Dockerfiles for all services
- [x] Docker Compose configuration
- [x] Nginx reverse proxy
- [ ] Jenkins CI/CD pipeline
- [ ] Terraform infrastructure
- [ ] AWS ECR and EC2 deployment
- [ ] Prometheus monitoring
- [ ] Grafana dashboards
- [ ] Deployment and rollback documentation

## Security

- Do not commit AWS credentials or SSH private keys.
- Use IAM roles for AWS access.
- Apply least-privilege security group rules.
- Restrict access to Jenkins and monitoring services.