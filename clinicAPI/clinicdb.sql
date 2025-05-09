-- CLINIC BOOKING SYSTEM DB

-- PATIENTS TABLE

CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    phone VARCHAR(15) UNIQUE,
    email VARCHAR(100) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- DOCTORS TABLE

CREATE TABLE doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100),
    phone VARCHAR(15) UNIQUE,
    email VARCHAR(100) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- APPOINTMENTS TABLE

CREATE TABLE appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_date DATETIME NOT NULL,
    reason TEXT,
    status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

-- TREATMENTS TABLE

CREATE TABLE treatments (
    treatment_id INT AUTO_INCREMENT PRIMARY KEY,
    appointment_id INT NOT NULL UNIQUE, -- one-to-one with appointment
    diagnosis TEXT NOT NULL,
    notes TEXT,
    
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id)
);

-- PRESCRIPTIONS TABLE

CREATE TABLE prescriptions (
    prescription_id INT AUTO_INCREMENT PRIMARY KEY,
    treatment_id INT NOT NULL,
    medicine_name VARCHAR(100) NOT NULL,
    dosage VARCHAR(100) NOT NULL,
    duration VARCHAR(50), -- e.g., '5 days', '2 weeks'

    FOREIGN KEY (treatment_id) REFERENCES treatments(treatment_id)
);

-- SAMPLE DATA INSERTS

-- Patients
INSERT INTO patients (first_name, last_name, date_of_birth, phone, email)
VALUES
('Alice', 'Kamau', '1995-07-21', '0700111222', 'alice.kamau@example.com'),
('Brian', 'Otieno', '1988-11-03', '0712345678', 'b.otieno@example.com');

-- Doctors
INSERT INTO doctors (full_name, specialization, phone, email)
VALUES
('Dr. Janet Mwangi', 'Cardiologist', '0722333444', 'janet.mwangi@clinic.com'),
('Dr. James Kariuki', 'Dermatologist', '0733555666', 'j.kariuki@clinic.com');

-- Appointments
INSERT INTO appointments (patient_id, doctor_id, appointment_date, reason)
VALUES
(1, 1, '2025-05-07 10:00:00', 'Routine heart checkup'),
(2, 2, '2025-05-08 14:30:00', 'Skin irritation and rash');

-- Treatments
INSERT INTO treatments (appointment_id, diagnosis, notes)
VALUES
(1, 'Mild hypertension', 'Recommended lifestyle changes and follow-up in 3 months'),
(2, 'Allergic dermatitis', 'Prescribed topical cream and antihistamines');

-- Prescriptions
INSERT INTO prescriptions (treatment_id, medicine_name, dosage, duration)
VALUES
(1, 'Lisinopril', '10mg once daily', '30 days'),
(2, 'Hydrocortisone cream', 'Apply twice daily', '1 week'),
(2, 'Cetirizine', '10mg once daily', '5 days');
