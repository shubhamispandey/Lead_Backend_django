# 🚀 Lead Management Backend (Django + JWT)

A simple Lead Management backend built with **Django**, **Django REST Framework**, and **JWT Authentication**, using **PostgreSQL** as the database.

---

## 📌 Features

* 🔐 JWT Authentication (Login / Refresh Token)
* 👤 User-based lead management
* ➕ Create Lead
* 📄 List Leads
* ✏️ Update Lead
* ❌ Delete Lead
* 🗄️ PostgreSQL Database
* 🌐 REST APIs

---

## 🛠️ Tech Stack

* Python (Django)
* Django REST Framework
* PostgreSQL
* JWT (SimpleJWT)

---

## 📂 Project Setup (Local)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/shubhamispandey/Lead_Backend_django.git
cd Lead_Backend_django/lead_manager
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Environment Configuration

Create a `.env` file in the root (`lead_manager/`):

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```

---

## 🗄️ Database Setup (PostgreSQL)

### Option 1: Local PostgreSQL

1. Install PostgreSQL
2. Create database:

```sql
CREATE DATABASE postgres;
```

3. Update `.env` credentials

---

### Option 2: Cloud (Supabase / Neon)

Use connection details:

```env
DB_HOST=db.xxxxx.supabase.co
DB_PORT=5432
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=yourpassword
```

---

## 🧱 Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 👤 Create Superuser

```bash
python manage.py createsuperuser
```

---

## ▶️ Run Server

```bash
python manage.py runserver
```

---

## 🌐 API Endpoints

### 🔐 Authentication

* Login:

```
POST /api/token/
```

* Refresh Token:

```
POST /api/token/refresh/
```

---

### 📌 Leads

| Action      | Method | Endpoint         |
| ----------- | ------ | ---------------- |
| Create Lead | POST   | /api/leads/      |
| List Leads  | GET    | /api/leads/      |
| Update Lead | PATCH  | /api/leads/{id}/ |
| Delete Lead | DELETE | /api/leads/{id}/ |

---

## 🧪 Sample Request (Create Lead)

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "9999999999",
  "source": "Website",
  "status": "New"
}
```

---

## 🔒 Authentication Usage

Include token in headers:

```http
Authorization: Bearer <access_token>
```

---

## 📁 Project Structure

```
lead_manager/
│
├── lead_manager/        # main project
├── leads/               # app
├── manage.py
├── requirements.txt
├── .env
```

---

## ⚠️ Notes

* `created_by` is automatically set from logged-in user
* JWT access token expiry is configurable
* Do NOT commit `.env` file

---

## ✅ Assignment Scope Covered

* Django REST APIs ✔
* PostgreSQL integration ✔
* JWT Authentication ✔
* CRUD operations ✔
* Clean project structure ✔

---

## 👨‍💻 Author

Shubham Pandey

---

## 🚀 Future Improvements

* Pagination
* Search & Filters
* Role-based access
* Deployment (AWS / Railway)

---
