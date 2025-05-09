from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PatientBase(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: Optional[datetime] = None
    phone: Optional[str] = None
    email: Optional[str] = None

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    patient_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class DoctorBase(BaseModel):
    full_name: str
    specialization: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None

class DoctorCreate(DoctorBase):
    pass

class Doctor(DoctorBase):
    doctor_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: datetime
    reason: Optional[str] = None
    status: Optional[str] = "Scheduled"

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    appointment_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class TreatmentBase(BaseModel):
    appointment_id: int
    diagnosis: str
    notes: Optional[str] = None

class TreatmentCreate(TreatmentBase):
    pass

class Treatment(TreatmentBase):
    treatment_id: int

    class Config:
        from_attributes = True

class PrescriptionBase(BaseModel):
    treatment_id: int
    medicine_name: str
    dosage: str
    duration: Optional[str] = None

class PrescriptionCreate(PrescriptionBase):
    pass

class Prescription(PrescriptionBase):
    prescription_id: int

    class Config:
        from_attributes = True