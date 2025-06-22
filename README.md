#  Late Show API

A RESTful Flask API for managing a Late Night TV Show system, including Guests, Episodes, Appearances, and Users with JWT-based authentication.

---

##  Project Structure

```
.
├── server/
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── guest.py
│   │   ├── episode.py
│   │   ├── appearance.py
│   │   └── user.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── guest_controller.py
│   │   ├── episode_controller.py
│   │   ├── appearance_controller.py
│   │   └── auth_controller.py
├── migrations/
├── challenge-4-lateshow.postman_collection.json
└── README.md
```

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ErnestKamau/Late-Show-API__Code-challenge.git
cd late-show-api-challenge
```

### 2. Install Dependencies

```bash
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell
```

### 3. PostgreSQL Setup

Open PostgreSQL and run:

```sql
CREATE DATABASE late_show_db;
```

### 4. Configure Environment

Create a `.env` file or update `server/config.py`:

```python
SQLALCHEMY_DATABASE_URI = "postgresql://<username>:<password>@localhost:5432/late_show_db"
```

---

##  How to Run

### 1. Set FLASK\_APP and Run Migrations

```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 2. Seed the Database

```bash
python server/seed.py
```

### 3. Start the Server

```bash
flask run
```

---

##  Authentication Flow

### Register a New User

```http
POST /register
Content-Type: application/json

{
  "username": "user123",
  "password": "securepassword"
}
```

### Login to Get Token

```http
POST /login
Content-Type: application/json

{
  "username": "user123",
  "password": "securepassword"
}
```

**Response:**

```json
{
  "access_token": "<JWT-TOKEN>"
}
```

### Use the Token

Send this in the header of protected routes:

```
Authorization: Bearer <JWT-TOKEN>
```

---

##  API Routes

| Route                | Method | Auth Required | Description                          |
| -------------------- | ------ | ------------- | ------------------------------------ |
| `/register`          | POST   | ❌             | Register a new user                  |
| `/login`             | POST   | ❌             | Login and receive JWT token          |
| `/episodes`          | GET    | ❌             | Get list of all episodes             |
| `/episodes/<int:id>` | GET    | ❌             | Get single episode + appearances     |
| `/episodes/<int:id>` | DELETE | ✅             | Delete an episode (with appearances) |
| `/guests`            | GET    | ❌             | Get list of all guests               |
| `/appearances`       | POST   | ✅             | Create a new guest appearance        |

---

##  Sample Request & Response

### GET `/episodes`

```http
GET /episodes
```

**Response:**

```json
[
  {
    "id": 1,
    "date": "2024-06-15",
    "number": 102,
    "appearances": [
      {
        "guest_name": "Emma Stone",
        "rating": 5
      }
    ]
  }
]
```

---

##  Postman Usage Guide

1. Open Postman.
2. Import `challenge-4-lateshow.postman_collection.json`.
3. Use `Register` and `Login` endpoints first to get the JWT token.
4. Add token to headers for protected routes:

```
Key: Authorization
Value: Bearer <your-token>
```

5. Test `POST /appearances` and `DELETE /episodes/:id` with authentication.

---

##  GitHub Repository

- [https://github.com/ErnestKamau/Late-Show-API__Code-challenge.git](https://github.com/ErnestKamau/Late-Show-API__Code-challenge.git)

---


