# Flask CRUD API

A basic CRUD API built with Python, Flask, Flask-RESTful, Flask-SQLAlchemy, and SQLite.

This project is created for learning how to build a simple REST API with Flask and connect it to a database.

## Technologies

* Python
* Flask
* Flask-RESTful
* Flask-SQLAlchemy
* SQLite

## Setup

Clone the repository:

```bash
git clone https://github.com/thanula2003/flask-api.git
cd YOUR-REPOSITORY
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

The API will run at:

```text
http://127.0.0.1:8080
```

## API Endpoints

| Method | Endpoint               | Description             |
| ------ | ---------------------- | ----------------------- |
| GET    | `/`                    | Home                    |
| POST   | `/users`               | Create a user           |
| GET    | `/users`               | Get all users           |
| GET    | `/users/<id>`          | Get user by ID          |
| GET    | `/users/email/<email>` | Get user by email       |
| PUT    | `/users/<id>`          | Update a user           |
| PATCH  | `/users/<id>`          | Partially update a user |
| DELETE | `/users/<id>`          | Delete a user           |

## Example

Create a user:

```http
POST /users
```

```json
{
    "name": "name",
    "email": "name@email.com"
}
```

Get all users:

```http
GET /users
```

## Purpose

The main purpose of this project is to understand the basics of:

* Flask
* REST APIs
* CRUD operations
* HTTP methods
* JSON
* SQLAlchemy
* SQLite

You can use Postman, Thunder Client, or another API testing tool to test the endpoints.

## License

MIT
