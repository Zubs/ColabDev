--DATABASE SCHEMA FOR ADMIN REGISTRATION

-- 1. Admin Registration Table

CREATE TABLE user (
    registration_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL, -- Typically the password should be hashed. this should be handled on the backend SHA-256 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- 2. Admin Password Reset Table

CREATE TABLE password_reset (
    reset_id INT AUTO_INCREMENT PRIMARY KEY,
    admin_id INT NOT NULL,
    reset_token VARCHAR(255) NOT NULL,
    token_expires DATETIME NOT NULL,
    token_used TINYINT(1) NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (admin_id) REFERENCES registration_admin(registration_id) ON DELETE CASCADE
);
