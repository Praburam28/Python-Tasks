🏥 Doctor–Patient Management API (FastAPI)

📌 Overview

This project is a simple REST API built using FastAPI to manage Doctors and Patients.
It demonstrates clean API design, validation using Pydantic, and basic in-memory data storage.

---

🚀 Tech Stack

- Python 3.9+
- FastAPI
- Pydantic
- Uvicorn

---

📁 Project Structure

Doctor_Patient_API/
│── main.py        # FastAPI app and routes
│── models.py      # Pydantic models (validation)
│── database.py    # In-memory storage

---

⚙️ Setup Instructions

🔹 1. Clone or Download Project

git clone <your-repo-url>
cd Doctor_Patient_API

---

🔹 2. Create Virtual Environment

python -m venv .venv

---

🔹 3. Activate Virtual Environment

Windows (PowerShell):

.venv\Scripts\Activate

If execution is blocked:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

---

🔹 4. Install Dependencies

pip install fastapi uvicorn email-validator

---

🔹 5. Run the Application

uvicorn main:app --reload

---

🔹 6. Open API Documentation

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

---

📚 API Endpoints

👨‍⚕️ Doctor APIs

- "POST /doctors" → Create doctor
- "GET /doctors" → List all doctors
- "GET /doctors/{doctor_id}" → Get doctor by ID

Sample Request

{
  "name": "Dr. John",
  "specialization": "Cardiology",
  "email": "john@example.com",
  "is_active": true
}

---

🧑‍🤝‍🧑 Patient APIs

- "POST /patients" → Create patient
- "GET /patients" → List all patients

Sample Request

{
  "name": "Ram",
  "age": 25,
  "phone": "9876543210"
}

---

✅ Validation Rules

- Email must be valid ("EmailStr")
- Age must be greater than 0
- Default value for "is_active = true"
- Errors handled using "HTTPException"

---

❗ Common Issues & Fixes

🔸 Missing email validator

ModuleNotFoundError: No module named 'email_validator'

✅ Fix:

pip install email-validator

---

🔸 Virtual Environment Issues

- Use Python 3.11 or 3.12 (recommended)
- Avoid unstable versions like Python 3.14

---

🚀 Future Improvements

- Add PUT and DELETE APIs
- Integrate SQLite or PostgreSQL
- Add authentication (JWT)
- Implement Doctor–Patient relationship (appointments)

---

👨‍💻 Author

Developed as part of FastAPI assignment.