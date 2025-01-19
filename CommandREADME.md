# Flask Application Deployment with Docker

---

## Steps to Set Up the Environment

### 1. SSH into the Server

Access the remote server:
```bash
gcloud compute ssh flask-web-server
```

### 2. Install Required Packages

Update the package list and install dependencies:
```bash
sudo apt update
sudo apt install python3-gunicorn libpq-dev python3-dev build-essential docker.io
```

### 3. Set Up Python Environment

Install `virtualenv` if not already installed:
```bash
pip install virtualenv
```

Create and activate a virtual environment:
```bash
virtualenv .env
source .env/bin/activate
```

### 4. Install Python Dependencies

Install Flask, SQLAlchemy, and PostgreSQL driver:
```bash
pip install Flask Flask-SQLAlchemy psycopg2 psycopg2-binary
```

Freeze the dependencies into a `requirements.txt` file:
```bash
pip freeze > requirements.txt
```

To install dependencies from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 5. Create the Flask Application

Write the Flask application code in `app.py`:
```bash
vi app.py
```

Example code snippet for `app.py`:
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### 6. Set Up Docker

#### Create a Dockerfile
Write the following content into a `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
```

#### Build and Run the Docker Container
Build the Docker image:
```bash
docker build -t flask-app .
```

Run the Docker container:
```bash
docker run -d -p 5000:5000 --name flask-app flask-app
```

Check running containers:
```bash
docker ps
```

### 7. Manage Docker Images

List all Docker images:
```bash
docker images
```

Remove unused Docker images:
```bash
docker rmi <image-id> --force
```

### 8. Test the Application

Access the application in your browser at:
```
http://<server-ip>:5000
```

