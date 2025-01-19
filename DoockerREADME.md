# Step 1: Use the official Python image as the base image
FROM python:3.11-slim

# Step 2: Set environment variables to ensure output is sent straight to the terminal
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Step 3: Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Step 4: Set the working directory inside the container
WORKDIR /app

# Step 5: Copy the application code and requirements.txt into the container
COPY . /app

# Step 6: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 7: Expose the port the Flask app will run on
EXPOSE 5000

# Step 8: Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Step 9: Start the Flask app
CMD ["flask", "run"]
