from pydantic import BaseModel, EmailStr, Field

# Doctor Model
class DoctorCreate(BaseModel):
    name: str
    specialization: str
    email: EmailStr
    is_active: bool = True


class Doctor(DoctorCreate):
    id: int


# Patient Model
class PatientCreate(BaseModel):
    name: str
    age: int = Field(..., gt=0)  # age > 0 validation
    phone: str


class Patient(PatientCreate):
    id: int