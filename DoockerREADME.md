
---

## Dockerfile Breakdown

### Step 1: Base Image
We use the official lightweight Python 3.11 image:
```dockerfile
FROM python:3.11-slim
```

### Step 2: Environment Variables
Set environment variables to ensure proper behavior during execution:
```dockerfile
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
```
- `PYTHONDONTWRITEBYTECODE`: Prevents Python from writing `.pyc` files.
- `PYTHONUNBUFFERED`: Ensures logs are output immediately.

### Step 3: Install System Dependencies
Install required system libraries:
```dockerfile
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*
```
- `libpq-dev`: Required for PostgreSQL.
- `gcc`: Needed for compiling certain Python packages.

### Step 4: Working Directory
Set the working directory inside the container:
```dockerfile
WORKDIR /app
```

### Step 5: Copy Files
Copy the application source code and dependency file:
```dockerfile
COPY . /app
```

### Step 6: Install Python Dependencies
Install dependencies from `requirements.txt`:
```dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```

### Step 7: Expose Port
Expose the port used by the Flask application (default: 5000):
```dockerfile
EXPOSE 5000
```

### Step 8: Flask Environment Variables
Set Flask-specific environment variables:
```dockerfile
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
```

### Step 9: Run the Application
Start the Flask application:
```dockerfile
CMD ["flask", "run"]
```

---

## How to Build and Run the Container

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Build the Docker Image**:
   ```bash
   docker build -t flask-app .
   ```

3. **Run the Container**:
   ```bash
   docker run -p 5000:5000 flask-app
   ```

4. **Access the Application**:
   - Open a browser and navigate to `http://localhost:5000`.

---


