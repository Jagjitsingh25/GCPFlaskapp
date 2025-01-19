# GCPFlaskapp
GCP project using python flask app 

# Flask App Setup with Gunicorn

This guide provides step-by-step instructions to set up a Flask application with Gunicorn on a Linux-based system.

## Prerequisites
Ensure your system is up-to-date and has Python 3 installed.

---

## Steps

### 1. Update and Upgrade Packages
```bash
sudo apt update && sudo apt upgrade -y
```

### 2. Install Python and Virtual Environment Tools
```bash
sudo apt install python3-pip python3-venv -y
```

### 3. Create a Flask Application Directory
```bash
mkdir flask_app && cd flask_app
```

### 4. Set Up a Virtual Environment
Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 5. Install Flask and Gunicorn
Inside the virtual environment, install Flask and Gunicorn:
```bash
pip install flask gunicorn
```

### 6. Create the Flask Application
Create a Python file named `app.py`:
```bash
vi app.py
```
Add the following content:
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### 7. Test the Flask Application
Run the application:
```bash
python app.py
```
Visit `http://<your_server_ip>:5000` in a browser to see "Hello, World!".

### 8. Run the Application with Gunicorn
Stop the Flask application (`Ctrl+C`) and start the application using Gunicorn:
```bash
gunicorn --bind 0.0.0.0:5000 app:app
```
