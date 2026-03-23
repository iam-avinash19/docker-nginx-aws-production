#  Production-Ready Flask App with Docker, Nginx & AWS

##  Project Overview

This project demonstrates a production-grade deployment of a Flask application using Docker and Nginx as a reverse proxy on AWS EC2.

---

##  Architecture

User → Nginx (Port 80) → Docker Container (Flask App)

---

##  Tech Stack

* Python (Flask)
* Docker
* Nginx
* AWS EC2

---

##  Project Structure

```
.
├── app.py
├── requirements.txt
├── Dockerfile
└── nginx.conf
```

---

##  Docker Setup

### Build Image

```
docker build -t myapp .
```

### Run Container

```
docker run -d -p 5000:5000 myapp
```

---

##  Nginx Configuration

```
server {
    listen 80;

    location / {
        proxy_pass http://127.0.0.1:5000;
    }
}
```

---

##  AWS Deployment Steps

1. Launch EC2 instance
2. Install Docker & Nginx
3. Configure Nginx reverse proxy
4. Run Docker container
5. Restart Nginx

---

##  Access Application

```
http://<EC2-PUBLIC-IP>
```

---

##  Key Features

* Reverse proxy with Nginx
* Production-ready setup
* Clean architecture
* Secure exposure (port 80)

---

##  Learnings

* Reverse proxy concept
* Production deployment
* Nginx configuration
* Docker networking

---

##  Author

Avinash Bagul
