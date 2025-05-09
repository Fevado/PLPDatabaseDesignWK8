from fastapi import FastAPI, HTTPException
from . import crud
from .schemas import (
    PatientCreate, Patient, DoctorCreate, Doctor,
    AppointmentCreate, Appointment, TreatmentCreate,
    Treatment, PrescriptionCreate, Prescription
)
from typing import List

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Clinic Booking System API",
        "docs": {
            "swagger": "http://127.0.0.1:8000/docs",
            "redoc": "http://127.0.0.1:8000/redoc"
        }
    }

# Patients endpoints
@app.post("/patients/", response_model=Patient)
def create_patient(patient: PatientCreate):
    patient_id = crud.create_patient(patient)
    return {**patient.dict(), "patient_id": patient_id, "created_at": None}

@app.get("/patients/{patient_id}", response_model=Patient)
def read_patient(patient_id: int):
    patient = crud.get_patient(patient_id)
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@app.get("/patients/", response_model=List[Patient])
def read_patients(skip: int = 0, limit: int = 100):
    patients = crud.get_patients(skip=skip, limit=limit)
    return patients

@app.put("/patients/{patient_id}", response_model=Patient)
def update_patient(patient_id: int, patient: PatientCreate):
    updated_id = crud.update_patient(patient_id, patient)
    if updated_id is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {**patient.dict(), "patient_id": patient_id}

@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int):
    deleted_id = crud.delete_patient(patient_id)
    if deleted_id is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"message": "Patient deleted successfully"}

# Doctors endpoints
@app.post("/doctors/", response_model=Doctor)
def create_doctor(doctor: DoctorCreate):
    doctor_id = crud.create_doctor(doctor)
    return {**doctor.dict(), "doctor_id": doctor_id, "created_at": None}

@app.get("/doctors/{doctor_id}", response_model=Doctor)
def read_doctor(doctor_id: int):
    doctor = crud.get_doctor(doctor_id)
    if doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor

@app.get("/doctors/", response_model=List[Doctor])
def read_doctors(skip: int = 0, limit: int = 100):
    doctors = crud.get_doctors(skip=skip, limit=limit)
    return doctors

@app.put("/doctors/{doctor_id}", response_model=Doctor)
def update_doctor(doctor_id: int, doctor: DoctorCreate):
    updated_id = crud.update_doctor(doctor_id, doctor)
    if updated_id is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return {**doctor.dict(), "doctor_id": doctor_id}

@app.delete("/doctors/{doctor_id}")
def delete_doctor(doctor_id: int):
    deleted_id = crud.delete_doctor(doctor_id)
    if deleted_id is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return {"message": "Doctor deleted successfully"}

# Appointments endpoints
@app.post("/appointments/", response_model=Appointment)
def create_appointment(appointment: AppointmentCreate):
    appointment_id = crud.create_appointment(appointment)
    return {**appointment.dict(), "appointment_id": appointment_id, "created_at": None}

@app.get("/appointments/{appointment_id}", response_model=Appointment)
def read_appointment(appointment_id: int):
    appointment = crud.get_appointment(appointment_id)
    if appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment

@app.get("/appointments/", response_model=List[Appointment])
def read_appointments(skip: int = 0, limit: int = 100):
    appointments = crud.get_appointments(skip=skip, limit=limit)
    return appointments

@app.put("/appointments/{appointment_id}", response_model=Appointment)
def update_appointment(appointment_id: int, appointment: AppointmentCreate):
    updated_id = crud.update_appointment(appointment_id, appointment)
    if updated_id is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return {**appointment.dict(), "appointment_id": appointment_id}

@app.delete("/appointments/{appointment_id}")
def delete_appointment(appointment_id: int):
    deleted_id = crud.delete_appointment(appointment_id)
    if deleted_id is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return {"message": "Appointment deleted successfully"}

# Treatments endpoints
@app.post("/treatments/", response_model=Treatment)
def create_treatment(treatment: TreatmentCreate):
    treatment_id = crud.create_treatment(treatment)
    return {**treatment.dict(), "treatment_id": treatment_id}

@app.get("/treatments/{treatment_id}", response_model=Treatment)
def read_treatment(treatment_id: int):
    treatment = crud.get_treatment(treatment_id)
    if treatment is None:
        raise HTTPException(status_code=404, detail="Treatment not found")
    return treatment

# Prescriptions endpoints
@app.post("/prescriptions/", response_model=Prescription)
def create_prescription(prescription: PrescriptionCreate):
    prescription_id = crud.create_prescription(prescription)
    return {**prescription.dict(), "prescription_id": prescription_id}

@app.get("/treatments/{treatment_id}/prescriptions", response_model=List[Prescription])
def read_prescriptions_by_treatment(treatment_id: int):
    prescriptions = crud.get_prescriptions_by_treatment(treatment_id)
    if not prescriptions:
        raise HTTPException(status_code=404, detail="No prescriptions found for this treatment")
    return prescriptions