-- Create schema if not exists
CREATE SCHEMA IF NOT EXISTS library_management;

-- User login table
CREATE TABLE IF NOT EXISTS library_management.user_login (
    user_id VARCHAR(50) PRIMARY KEY,
    user_password TEXT,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    sign_up_on DATE,
    email_id VARCHAR(100)
);

-- Publisher table
CREATE TABLE IF NOT EXISTS library_management.publisher (
    publisher_id VARCHAR(50) PRIMARY KEY,
    publisher_name VARCHAR(100),
    distributor_name VARCHAR(100),
    releases_count INT,
    last_release_date DATE
);

-- Author table
CREATE TABLE IF NOT EXISTS library_management.author (
    author_id VARCHAR(50) PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    publications_count INT
);

-- Books table
CREATE TABLE IF NOT EXISTS library_management.books (
    book_id VARCHAR(50) PRIMARY KEY,
    book_code VARCHAR(20),
    book_name VARCHAR(200),
    author_id VARCHAR(50),
    publisher_id VARCHAR(50),
    book_version VARCHAR(50),
    release_date DATE,
    available_from DATE,
    is_available BOOLEAN,
    FOREIGN KEY (author_id) REFERENCES library_management.author(author_id),
    FOREIGN KEY (publisher_id) REFERENCES library_management.publisher(publisher_id)
);

-- Staff table
CREATE TABLE IF NOT EXISTS library_management.staff (
    staff_id VARCHAR(50) PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    staff_role VARCHAR(100),
    start_date DATE,
    last_date DATE,
    is_active BOOLEAN,
    work_shift_start TIME,
    work_shift_end TIME
);

-- Readers table
CREATE TABLE IF NOT EXISTS library_management.readers (
    reader_id VARCHAR(50) PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    registered_on DATE,
    books_issued_total INT,
    books_issued_current INT,
    is_issued BOOLEAN,
    last_issue_date DATE,
    total_fine DECIMAL(10, 2),
    current_fine DECIMAL(10, 2)
);

-- Books issue table
CREATE TABLE IF NOT EXISTS library_management.books_issue (
    issue_id SERIAL PRIMARY KEY,
    book_id VARCHAR(50),
    issued_to VARCHAR(50),
    issued_on DATE,
    return_on DATE,
    current_fine DECIMAL(10, 2),
    fine_paid BOOLEAN,
    payment_transaction_id VARCHAR(100),
    FOREIGN KEY (book_id) REFERENCES library_management.books(book_id),
    FOREIGN KEY (issued_to) REFERENCES library_management.readers(reader_id)
);

-- Settings table (singleton table for system-wide settings)
CREATE TABLE IF NOT EXISTS library_management.settings (
    setting_id SERIAL PRIMARY KEY,
    book_issue_count_per_reader INT,
    fine_per_day DECIMAL(10, 2),
    book_return_in_days INT
);

-- Insert default settings
INSERT INTO library_management.settings (book_issue_count_per_reader, fine_per_day, book_return_in_days)
VALUES (5, 0.50, 14);
