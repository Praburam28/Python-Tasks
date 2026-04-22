# 🏥 FastAPI Doctor-Patient Management System

## 📌 Project Overview

This project is a **FastAPI-based backend application** for managing:

* Doctors
* Patients
* Appointments
* Authentication (JWT)

It demonstrates a **real-world API structure** with proper modules, database integration, and security.

---

## 🚀 Features

### 🔹 Authentication

* User Registration
* User Login (JWT आधारित authentication)
* Protected APIs

### 🔹 Doctor Module

* Add Doctor
* Get Doctors (with specialization filter)
* Update Doctor
* Delete Doctor

### 🔹 Patient Module

* Add Patient
* Search Patient (by name)
* Update Patient
* Delete Patient

### 🔹 Appointment Module

* Create Appointment
* Get All Appointments
* Get by Doctor / Patient
* Cancel Appointment

---

## 🛠 Tech Stack

* **FastAPI**
* **SQLAlchemy (ORM)**
* **MySQL**
* **JWT Authentication**
* **Uvicorn**
* **Pydantic**

---

## 📂 Project Structure

```
new-project/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── routers.py
│
├── venv/
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone / Navigate to Project

```bash
cd new-project
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

### 3️⃣ Activate Virtual Environment

```bash
venv\Scripts\activate
```

---

### 4️⃣ Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy pymysql python-multipart passlib[bcrypt] python-jose
```

---

### 5️⃣ Setup MySQL Database

Open MySQL and run:

```sql
CREATE DATABASE doctor_db;
```

---

### 6️⃣ Configure Database

Update `database.py`:

```python
DATABASE_URL = "mysql+pymysql://root:password@localhost/doctor_db"
```

👉 Replace `root` and `password` with your credentials

---

### ▶️ 7️⃣ Run the Application

```bash
uvicorn app.main:app --reload
```

---

### 🌐 8️⃣ Open in Browser

```
http://127.0.0.1:8000/docs
```

---

## 🔐 API Usage Flow

### 1. Register User

POST `/register`

```json
{
  "username": "admin",
  "password": "admin123"
}
```

---

### 2. Login

POST `/login`

👉 Use form-data:

* username
* password

---

### 3. Get Token

```json
{
  "access_token": "xxxxx",
  "token_type": "bearer"
}
```

---

### 4. Authorize

Click **Authorize 🔓** in Swagger and enter:

```
Bearer xxxxx
```

---

### 5. Access Protected APIs

Now you can use:

* `/doctors`
* `/patients`
* `/appointments`

---

## ⚠️ Common Issues & Fixes

| Issue               | Solution                   |
| ------------------- | -------------------------- |
| 401 Unauthorized    | Add JWT token              |
| 422 Error           | Use form-data in login     |
| Server not starting | Install `python-multipart` |
| DB Error            | Check MySQL running        |

---

## 🎯 Future Enhancements

* Pagination
* Logging
* Role-based access (Admin/User)
* Deployment (Docker / Cloud)

---

## 👨‍💻 Author

Developed as part of **FastAPI Advanced Assignment**

---

## ⭐ Conclusion

This project demonstrates:

* Clean API design
* Authentication using JWT
* Database integration
* Modular FastAPI architecture

---
