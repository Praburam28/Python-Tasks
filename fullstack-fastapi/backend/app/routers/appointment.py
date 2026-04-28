from fastapi import APIRouter
from ..database import SessionLocal
from .. import models, schemas

router = APIRouter()

@router.post("/")
def create_appointment(data: schemas.AppointmentCreate):
    db = SessionLocal()
    appointment = models.Appointment(
        doctor_id=data.doctor_id,
        patient_id=data.patient_id
    )
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment

@router.get("/")
def get_appointments():
    db = SessionLocal()
    return db.query(models.Appointment).all()