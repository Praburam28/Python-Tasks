from fastapi import FastAPI, HTTPException
from models import DoctorCreate, Doctor, PatientCreate, Patient
import database

app = FastAPI()

# DOCTOR APIs

@app.post("/doctors", response_model=Doctor)
def create_doctor(doctor: DoctorCreate):
    new_doctor = doctor.dict()
    new_doctor["id"] = database.doctor_id_counter

    database.doctor_id_counter += 1
    database.doctors_db.append(new_doctor)

    return new_doctor


@app.get("/doctors", response_model=list[Doctor])
def get_doctors():
    return database.doctors_db


@app.get("/doctors/{doctor_id}", response_model=Doctor)
def get_doctor(doctor_id: int):
    for doc in database.doctors_db:
        if doc["id"] == doctor_id:
            return doc
    raise HTTPException(status_code=404, detail="Doctor not found")


# PATIENT APIs

@app.post("/patients", response_model=Patient)
def create_patient(patient: PatientCreate):
    new_patient = patient.dict()
    new_patient["id"] = database.patient_id_counter

    database.patient_id_counter += 1
    database.patients_db.append(new_patient)

    return new_patient


@app.get("/patients", response_model=list[Patient])
def get_patients():
    return database.patients_db