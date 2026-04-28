from fastapi import APIRouter
from ..database import SessionLocal
from .. import models, schemas

router = APIRouter()

@router.post("/")
def create_doctor(data: schemas.DoctorCreate):
    db = SessionLocal()
    doctor = models.Doctor(name=data.name)
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return doctor

@router.get("/")
def get_doctors():
    db = SessionLocal()
    return db.query(models.Doctor).all()