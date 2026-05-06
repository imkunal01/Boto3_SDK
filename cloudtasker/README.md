# Project Idea: “CloudTasker”

A Dockerized task management API that:
- runs inside Docker
- stores tasks in DynamoDB
- uses Boto3 for AWS communication
- deploys on AWS
- can later be automated using DevOps scripts

Think:
Frontend/Postman → Flask/FastAPI App → Boto3 → DynamoDB

## Why This Project Is Good

This teaches:

| Skill | You Learn |
|---|---|
| Docker | Containerization |
| Boto3 | AWS automation |
| DynamoDB | NoSQL database |
| IAM | AWS permissions |
| EC2/ECS | Deployment |
| REST APIs | Backend |
| Environment Variables | Secure configs |
| Cloud Networking | Real deployment |
| DevOps Basics | Production thinking |

## Tech Stack
**Backend**: FastAPI

I’d recommend **FastAPI** because:
- modern
- async capable
- automatic Swagger docs
- good for microservices

## AWS Services Used

### 1. DynamoDB
Stores tasks. Example task:
`json
{
  "taskId": "1",
  "title": "Learn Boto3",
  "status": "pending"
}
`

### 2. IAM
Provides permissions. Your app should NOT use root credentials. Instead:
- create IAM user
- attach DynamoDB permissions
*Very important real-world habit.*

### 3. EC2
Host Docker container. Later you can move to ECS or EKS.

## Folder Structure
This structure teaches good engineering habits.

`	ext
cloudtasker/
│
├── app/
│   ├── main.py
│   ├── routes/
│   │   └── task_routes.py
│   ├── services/
│   │   └── dynamo_service.py
│   ├── models/
│   │   └── task_model.py
│   ├── config/
│   │   └── aws_config.py
│   └── utils/
│
├── Dockerfile
├── requirements.txt
├── .env
├── docker-compose.yml
└── README.md
`

## What Features Should It Have?
Start SIMPLE.

### Phase 1 — Basic CRUD API
**Endpoints:**
- Create Task: POST /tasks
- Get All Tasks: GET /tasks
- Update Task: PUT /tasks/{id}
- Delete Task: DELETE /tasks/{id}

### Phase 2 — Dockerize
Learn:
- Dockerfile
- image building
- containers
- ports
- volumes

### Phase 3 — AWS Deployment
Deploy Docker container to EC2. Then connect to DynamoDB. This is your first real cloud deployment.

### Phase 4 — Boto3 Automation Scripts
THIS is where DevOps starts. Example automation scripts:
1. **Create DynamoDB Table Automatically:** dynamodb.create_table(...)
2. **EC2 Control Script:** start server, stop server, reboot server
3. **Backup Script:** Backup DynamoDB data to S3.

## Architecture
Here’s the mental image:
`	ext
  ┌─────────────┐
  │  Postman    │
  └──────┬──────┘
         │ HTTP Requests
  ┌──────▼──────┐
  │ FastAPI App │
  │  Dockerized │
  └──────┬──────┘
         │ Boto3
  ┌──────▼──────┐
  │   DynamoDB  │
  └─────────────┘
`

## What You’ll Learn Deeply
1. **Docker Concepts:** images, containers, layers, networking, environment variables.
2. **AWS Authentication:** IAM users, access keys, AWS credentials, regions.
3. **NoSQL Thinking:** partition keys, scalability, denormalization, document structure.
4. **Production Thinking:** stateless apps, cloud deployment, infra separation, security practices.

## Recommended Learning Flow

- **STEP 1 — Build Local API:** FastAPI only with local memory storage. Understand APIs first.
- **STEP 2 — Connect DynamoDB:** Replace local storage with Boto3 and DynamoDB.
- **STEP 3 — Dockerize:** Create FROM python:3.11, learn docker build and docker run.
- **STEP 4 — Deploy to EC2:** Teaches SSH, security groups, server deployment, Linux basics.
- **STEP 5 — Automate AWS Using Boto3:** Create automation scripts.

## Later Upgrades (VERY COOL)
After MVP:
- **Add JWT Authentication:** auth systems, secure APIs
- **Add Redis Caching:** caching, performance
- **Add CI/CD:** GitHub Actions (push code → build docker image → deploy automatically)
- **Add ECS Deployment:** container orchestration, scaling, production infra
- **Add Terraform:** infrastructure as code

## Your First Goal
Your FIRST milestone should simply be:
1. Dockerized FastAPI app
2. Connected to DynamoDB using Boto3
3. CRUD working locally
