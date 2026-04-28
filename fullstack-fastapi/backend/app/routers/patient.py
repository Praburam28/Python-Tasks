from fastapi import APIRouter
from ..database import SessionLocal
from .. import models, schemas

router = APIRouter()

@router.post("/")
def create_patient(data: schemas.PatientCreate):
    db = SessionLocal()
    patient = models.Patient(name=data.name)
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

@router.get("/")
def get_patients():
    db = SessionLocal()
    return db.query(models.Patient).all()