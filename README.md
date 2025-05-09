# Clinic Booking System API

A CRUD API for managing a clinic booking system with patients, doctors, appointments, treatments, and prescriptions.

## Features

- Patient management (create, read, update, delete)
- Doctor management (create, read, update, delete)
- Appointment scheduling and tracking
- Treatment records with diagnoses
- Prescription management

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your MySQL credentials:
      DB_HOST=localhost
      DB_NAME=clinicdb
      DB_USER=your_username
      DB_PASSWORD=your_password
4. Run the FastAPI server: `uvicorn app.main:app --reload`

## API Documentation

After running the server, access the interactive API docs at:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Database Schema

The database schema includes 5 tables:
- patients
- doctors
- appointments
- treatments
- prescriptions

My ERD diagram
![alt text](<Clinicdb system.png>)

See the `clinicdb.sql` file for the complete schema definition.

## Running the Application
1. Create a .env file in your project root with your MySQL credentials:

DB_HOST=localhost
DB_NAME=clinicdb
DB_USER=your_username
DB_PASSWORD=your_password

2. Run the FastAPI server: Enter this into yoour teminal

`uvicorn app.main:app --reload`

3. Access the API documentation at:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

4. Upon running the applicaion successfully, the fastAPI will provide you with a graphical user  interface where you can manipulate the data to your liking.

