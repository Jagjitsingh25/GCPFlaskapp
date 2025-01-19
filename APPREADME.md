---

## Prerequisites

Ensure you have the following installed before proceeding:

- Python 3.7+
- PostgreSQL database
- Required Python libraries (`flask`, `flask_sqlalchemy`)

---

## Setup Instructions

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd <repository-name>
```

### Step 2: Install Dependencies

Create a virtual environment and install required Python libraries:

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install flask flask_sqlalchemy
```

### Step 3: Update Database Configuration

Modify the database connection URL in the application:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user1:Localhost_1234567@34.27.54.14:5432/mono2micro'
```
- Replace `user1`, `Localhost_1234567`, `34.27.54.14`, and `mono2micro` with your actual PostgreSQL credentials and database details.

### Step 4: Run the Application

Start the Flask application:

```bash
python app.py
```

The application will run at `http://0.0.0.0:5000`.

---

## API Endpoints

### 1. Add a User

**Endpoint:** `/add_user`  
**Method:** `POST`

Add a new user to the `users` table.

**Request Body (JSON):**
```json
{
    "username": "example_user",
    "email": "example_user@example.com"
}
```

**Response:**
- Success: HTTP 201 with message
- Failure: HTTP 500 with error message

**Example cURL Command:**
```bash
curl -X POST http://localhost:5000/add_user \
-H "Content-Type: application/json" \
-d '{"username": "example_user", "email": "example_user@example.com"}'
```

### 2. Get All Users

**Endpoint:** `/get_users`  
**Method:** `GET`

Retrieve all users from the `users` table.

**Response:**
- Success: HTTP 200 with list of users (JSON array)

**Example Response:**
```json
[
    {
        "id": 1,
        "username": "example_user",
        "email": "example_user@example.com"
    }
]
```

**Example cURL Command:**
```bash
curl -X GET http://localhost:5000/get_users
```

---

