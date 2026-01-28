CREATE DATABASE IF NOT EXISTS momo_db;
USE momo_db;

-- MoMo Transaction Analyzer Database Setup Script
-- Author: EWD 14
-- Date: 2026-01-28
-- This script creates all tables, constraints, indexes, and inserts sample data.

-- Drop tables if they exist (for testing/demo purposes)
DROP TABLE IF EXISTS Transaction_Participants;
DROP TABLE IF EXISTS System_Logs;
DROP TABLE IF EXISTS Transactions;
DROP TABLE IF EXISTS Transaction_Categories;
DROP TABLE IF EXISTS Users;

-- 1. Users Table
CREATE TABLE Users (
	user_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique user/customer ID',
	phone_number VARCHAR(20) NOT NULL UNIQUE COMMENT 'User phone number',
	name VARCHAR(100) COMMENT 'User name (optional)',
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'Account creation timestamp'
);

-- 2. Transaction_Categories Table
CREATE TABLE Transaction_Categories (
	category_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique category ID',
	category_name VARCHAR(50) NOT NULL UNIQUE COMMENT 'Transaction type/category',
	description VARCHAR(255) COMMENT 'Category description'
);

-- 3. Transactions Table
CREATE TABLE Transactions (
	transaction_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique transaction ID',
	transaction_code VARCHAR(30) NOT NULL UNIQUE COMMENT 'Transaction reference code',
	transaction_date DATETIME NOT NULL COMMENT 'Date and time of transaction',
	amount DECIMAL(15,2) NOT NULL CHECK (amount > 0) COMMENT 'Transaction amount',
	description VARCHAR(255) COMMENT 'Transaction description',
	sender_id INT NOT NULL COMMENT 'FK to Users (sender)',
	receiver_id INT COMMENT 'FK to Users (receiver, optional)',
	category_id INT NOT NULL COMMENT 'FK to Transaction_Categories',
	FOREIGN KEY (sender_id) REFERENCES Users(user_id),
	FOREIGN KEY (receiver_id) REFERENCES Users(user_id),
	FOREIGN KEY (category_id) REFERENCES Transaction_Categories(category_id),
	INDEX idx_sender (sender_id),
	INDEX idx_receiver (receiver_id),
	INDEX idx_category (category_id)
);

-- 4. Transaction_Participants (Junction Table for M:N)
CREATE TABLE Transaction_Participants (
	transaction_id INT NOT NULL COMMENT 'FK to Transactions',
	user_id INT NOT NULL COMMENT 'FK to Users',
	role ENUM('sender','receiver','other') NOT NULL COMMENT 'Role in transaction',
	PRIMARY KEY (transaction_id, user_id),
	FOREIGN KEY (transaction_id) REFERENCES Transactions(transaction_id),
	FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- 5. System_Logs Table
CREATE TABLE System_Logs (
	log_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique log entry ID',
	log_time DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'Log timestamp',
	log_level VARCHAR(20) NOT NULL COMMENT 'Log severity (INFO, ERROR, etc.)',
	message TEXT NOT NULL COMMENT 'Log message',
	transaction_id INT COMMENT 'FK to Transactions (optional)',
	FOREIGN KEY (transaction_id) REFERENCES Transactions(transaction_id)
);

-- Insert sample data (5+ records per main table)

-- Users
INSERT INTO Users (phone_number, name) VALUES
	('+250788123456', 'John Doe'),
	('+250795758784', 'Jane Smith'),
	('+250782654321', 'Alice Brown'),
	('+250789654321', 'Bob Lee'),
	('+250781234567', 'Eve Kim');

-- Transaction Categories
INSERT INTO Transaction_Categories (category_name, description) VALUES
	('received', 'Money received'),
	('sent', 'Money sent'),
	('payment', 'Bill or merchant payment'),
	('transfer', 'Money transfer'),
	('airtime', 'Airtime purchase');

-- Transactions
INSERT INTO Transactions (transaction_code, transaction_date, amount, description, sender_id, receiver_id, category_id) VALUES
	('TXN001', '2026-01-12 09:00:00', 75000, 'Money received from John', 1, 2, 1),
	('TXN002', '2026-01-12 10:00:00', 25000, 'Shopping payment', 2, 3, 3),
	('TXN003', '2026-01-10 15:30:00', 15000, 'Electricity bill', 2, 4, 3),
	('TXN004', '2026-01-08 12:00:00', 50000, 'Money transfer', 3, 4, 4),
	('TXN005', '2026-01-05 08:45:00', 5000, 'Airtime purchase', 4, NULL, 5),
	('TXN006', '2025-12-30 17:00:00', 120000, 'Salary payment', 5, 1, 1);

-- Transaction Participants
INSERT INTO Transaction_Participants (transaction_id, user_id, role) VALUES
	(1, 1, 'sender'),
	(1, 2, 'receiver'),
	(2, 2, 'sender'),
	(2, 3, 'receiver'),
	(3, 2, 'sender'),
	(3, 4, 'receiver'),
	(4, 3, 'sender'),
	(4, 4, 'receiver'),
	(5, 4, 'sender'),
	(6, 5, 'sender'),
	(6, 1, 'receiver');

-- System Logs
INSERT INTO System_Logs (log_level, message, transaction_id) VALUES
	('INFO', 'Transaction imported successfully', 1),
	('INFO', 'Transaction imported successfully', 2),
	('ERROR', 'Failed to process transaction', 3),
	('INFO', 'Transaction imported successfully', 4),
	('WARN', 'Transaction missing receiver', 5);
