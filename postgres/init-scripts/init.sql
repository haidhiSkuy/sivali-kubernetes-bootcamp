CREATE TABLE patients (
    patient_id SERIAL PRIMARY KEY,
    patient_name VARCHAR(255) NOT NULL,
    alzheimer_status VARCHAR(100)
);

INSERT INTO patients (patient_name, alzheimer_status) VALUES
('John Doe', 'Positive'),
('Jane Smith', 'Negative'),
('Alice Johnson', 'Unknown');
