from pydantic import BaseModel

class DoctorCreate(BaseModel):
    name: str

class PatientCreate(BaseModel):
    name: str

class AppointmentCreate(BaseModel):
    doctor_id: int
    patient_id: int