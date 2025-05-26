# 👋 FastAPI Hello API

A simple FastAPI application demonstrating basic endpoints.

## 🚀 Endpoints

| Method | Endpoint        | Description                        |
|--------|------------------|------------------------------------|
| GET    | `/`              | Returns "Hello, World!"            |
| GET    | `/about`         | Returns an about page message      |
| GET    | `/greet/{name}`  | Returns a personalized greeting    |

---

## 🛠️ Requirements

- Python 3.7 or newer
- FastAPI
- Uvicorn (for running the server)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fastapi-hello-api.git
cd fastapi-hello-api
```

### 2. Create and activate a virtual environment
``` bash

python -m venv myenv
myenv\Scripts\activate  # On Windows use `env\Scripts\activate`
```
### Install the dependencies
``` bash

pip install fastapi uvicorn
```

### ▶️ Running the Application
Run the FastAPI app using Uvicorn:

```bash

uvicorn main:app --reload
```
