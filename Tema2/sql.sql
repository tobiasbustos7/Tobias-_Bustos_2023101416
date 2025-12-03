-- Script para crear la base de datos y tablas para Ganadería Paraguay

-- Tabla para almacenar las solicitudes de contacto
CREATE TABLE IF NOT EXISTS contact_requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    preferred_time VARCHAR(50) NOT NULL,
    cattle_type VARCHAR(50) NOT NULL,
    request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);