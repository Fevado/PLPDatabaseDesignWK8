from .database import get_db_connection
from datetime import datetime

# Patient CRUD operations
def create_patient(patient):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO patients (first_name, last_name, date_of_birth, phone, email)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        patient.first_name, patient.last_name, patient.date_of_birth,
        patient.phone, patient.email
    ))
    conn.commit()
    patient_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return patient_id

def get_patient(patient_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM patients WHERE patient_id = %s"
    cursor.execute(query, (patient_id,))
    patient = cursor.fetchone()
    cursor.close()
    conn.close()
    return patient

def get_patients(skip: int = 0, limit: int = 100):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM patients LIMIT %s OFFSET %s"
    cursor.execute(query, (limit, skip))
    patients = cursor.fetchall()
    cursor.close()
    conn.close()
    return patients

def update_patient(patient_id, patient):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
    UPDATE patients SET 
    first_name = %s, 
    last_name = %s, 
    date_of_birth = %s, 
    phone = %s, 
    email = %s 
    WHERE patient_id = %s
    """
    cursor.execute(query, (
        patient.first_name, patient.last_name, patient.date_of_birth,
        patient.phone, patient.email, patient_id
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return patient_id

def delete_patient(patient_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM patients WHERE patient_id = %s"
    cursor.execute(query, (patient_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return patient_id

# Doctor CRUD operations (similar pattern)
def create_doctor(doctor):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO doctors (full_name, specialization, phone, email)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (
        doctor.full_name, doctor.specialization,
        doctor.phone, doctor.email
    ))
    conn.commit()
    doctor_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return doctor_id

def get_doctor(doctor_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM doctors WHERE doctor_id = %s"
    cursor.execute(query, (doctor_id,))
    doctor = cursor.fetchone()
    cursor.close()
    conn.close()
    return doctor

def get_doctors(skip: int = 0, limit: int = 100):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM doctors LIMIT %s OFFSET %s"
    cursor.execute(query, (limit, skip))
    doctors = cursor.fetchall()
    cursor.close()
    conn.close()
    return doctors

def update_doctor(doctor_id, doctor):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
    UPDATE doctors SET 
    full_name = %s, 
    specialization = %s, 
    phone = %s, 
    email = %s 
    WHERE doctor_id = %s
    """
    cursor.execute(query, (
        doctor.full_name, doctor.specialization,
        doctor.phone, doctor.email, doctor_id
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return doctor_id

def delete_doctor(doctor_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM doctors WHERE doctor_id = %s"
    cursor.execute(query, (doctor_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return doctor_id

# Appointment CRUD operations
def create_appointment(appointment):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO appointments (patient_id, doctor_id, appointment_date, reason, status)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        appointment.patient_id, appointment.doctor_id,
        appointment.appointment_date, appointment.reason,
        appointment.status
    ))
    conn.commit()
    appointment_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return appointment_id

def get_appointment(appointment_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT a.*, p.first_name as patient_first_name, p.last_name as patient_last_name,
    d.full_name as doctor_name, d.specialization
    FROM appointments a
    JOIN patients p ON a.patient_id = p.patient_id
    JOIN doctors d ON a.doctor_id = d.doctor_id
    WHERE a.appointment_id = %s
    """
    cursor.execute(query, (appointment_id,))
    appointment = cursor.fetchone()
    cursor.close()
    conn.close()
    return appointment

def get_appointments(skip: int = 0, limit: int = 100):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT a.*, p.first_name as patient_first_name, p.last_name as patient_last_name,
    d.full_name as doctor_name, d.specialization
    FROM appointments a
    JOIN patients p ON a.patient_id = p.patient_id
    JOIN doctors d ON a.doctor_id = d.doctor_id
    LIMIT %s OFFSET %s
    """
    cursor.execute(query, (limit, skip))
    appointments = cursor.fetchall()
    cursor.close()
    conn.close()
    return appointments

def update_appointment(appointment_id, appointment):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
    UPDATE appointments SET 
    patient_id = %s, 
    doctor_id = %s, 
    appointment_date = %s, 
    reason = %s, 
    status = %s 
    WHERE appointment_id = %s
    """
    cursor.execute(query, (
        appointment.patient_id, appointment.doctor_id,
        appointment.appointment_date, appointment.reason,
        appointment.status, appointment_id
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return appointment_id

def delete_appointment(appointment_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM appointments WHERE appointment_id = %s"
    cursor.execute(query, (appointment_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return appointment_id

# Treatment and Prescription CRUD operations
def create_treatment(treatment):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO treatments (appointment_id, diagnosis, notes)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (
        treatment.appointment_id, treatment.diagnosis, treatment.notes
    ))
    conn.commit()
    treatment_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return treatment_id

def get_treatment(treatment_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT t.*, a.appointment_date, p.patient_id, p.first_name as patient_first_name, 
    p.last_name as patient_last_name, d.full_name as doctor_name
    FROM treatments t
    JOIN appointments a ON t.appointment_id = a.appointment_id
    JOIN patients p ON a.patient_id = p.patient_id
    JOIN doctors d ON a.doctor_id = d.doctor_id
    WHERE t.treatment_id = %s
    """
    cursor.execute(query, (treatment_id,))
    treatment = cursor.fetchone()
    cursor.close()
    conn.close()
    return treatment

def create_prescription(prescription):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO prescriptions (treatment_id, medicine_name, dosage, duration)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (
        prescription.treatment_id, prescription.medicine_name,
        prescription.dosage, prescription.duration
    ))
    conn.commit()
    prescription_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return prescription_id

def get_prescriptions_by_treatment(treatment_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM prescriptions WHERE treatment_id = %s"
    cursor.execute(query, (treatment_id,))
    prescriptions = cursor.fetchall()
    cursor.close()
    conn.close()
    return prescriptions