INSERT INTO library_management.user_login (user_id, user_password, first_name, last_name, sign_up_on, email_id)
VALUES 
    ('user1', 'password1', 'John', 'Doe', '2023-01-15', 'john.doe@example.com'),
    ('user2', 'password2', 'Jane', 'Smith', '2023-02-20', 'jane.smith@example.com'),
    ('user3', 'password3', 'Michael', 'Johnson', '2023-03-25', 'michael.johnson@example.com'),
    ('user4', 'password4', 'Emily', 'Brown', '2023-04-10', 'emily.brown@example.com'),
    ('user5', 'password5', 'David', 'Wilson', '2023-05-05', 'david.wilson@example.com'),
    ('user6', 'password6', 'Sarah', 'Taylor', '2023-06-20', 'sarah.taylor@example.com'),
    ('user7', 'password7', 'Emma', 'Miller', '2023-07-15', 'emma.miller@example.com');

INSERT INTO library_management.publisher (publisher_id, publisher_name, distributor_name, releases_count, last_release_date)
VALUES 
    ('pub1', 'Penguin Books', 'Penguin Random House', 150, '2023-05-10'),
    ('pub2', 'HarperCollins', 'HarperCollins Publishers', 120, '2023-04-15'),
    ('pub3', 'Oxford University Press', 'Oxford University Press', 90, '2023-06-20'),
    ('pub4', 'Random House', 'Random House Publishing Group', 100, '2023-07-05'),
    ('pub5', 'Simon & Schuster', 'Simon & Schuster', 80, '2023-06-25');

INSERT INTO library_management.author (author_id, first_name, last_name, publications_count)
VALUES 
    ('auth1', 'George', 'Orwell', 10),
    ('auth2', 'J.K.', 'Rowling', 15),
    ('auth3', 'Stephen', 'King', 20),
    ('auth4', 'Agatha', 'Christie', 30),
    ('auth5', 'Jane', 'Austen', 12);

INSERT INTO library_management.books (book_id, book_code, book_name, author_id, publisher_id, book_version, release_date, available_from, is_available)
VALUES 
    ('book1', 'B001', '1984', 'auth1', 'pub1', 'First Edition', '1949-06-08', '1949-06-15', true),
    ('book2', 'B002', 'Harry Potter and the Philosopher''s Stone', 'auth2', 'pub2', '20th Anniversary Edition', '1997-06-26', '1997-07-05', true),
    ('book3', 'B003', 'The Shining', 'auth3', 'pub3', 'Revised Edition', '1977-01-28', '1977-02-10', true),
    ('book4', 'B004', 'Murder on the Orient Express', 'auth4', 'pub4', 'Deluxe Edition', '1934-01-01', '1934-01-15', true),
    ('book5', 'B005', 'Pride and Prejudice', 'auth5', 'pub5', 'Collector''s Edition', '1813-01-28', '1813-02-10', true);

INSERT INTO library_management.staff (staff_id, first_name, last_name, staff_role, start_date, last_date, is_active, work_shift_start, work_shift_end)
VALUES 
    ('staff1', 'Emily', 'Davis', 'Librarian', '2023-01-02', NULL, true, '08:00:00', '16:00:00'),
    ('staff2', 'David', 'Brown', 'Assistant Librarian', '2023-02-15', NULL, true, '10:00:00', '18:00:00'),
    ('staff3', 'Sarah', 'Wilson', 'Cataloguer', '2023-03-20', NULL, true, '09:00:00', '17:00:00'),
    ('staff4', 'Michael', 'Clark', 'Library Assistant', '2023-04-05', NULL, true, '11:00:00', '19:00:00');

INSERT INTO library_management.readers (reader_id, first_name, last_name, registered_on, books_issued_total, books_issued_current, is_issued, last_issue_date, total_fine, current_fine)
VALUES 
    ('reader1', 'Mark', 'Robinson', '2023-04-10', 10, 2, true, '2023-06-15', 5.50, 2.50),
    ('reader2', 'Emma', 'White', '2023-05-20', 8, 1, true, '2023-07-01', 3.25, 1.25),
    ('reader3', 'Daniel', 'Lee', '2023-06-30', 5, 0, false, NULL, 0.00, 0.00),
    ('reader4', 'Sophia', 'Taylor', '2023-07-15', 3, 1, true, '2023-07-20', 1.75, 0.75);

INSERT INTO library_management.books_issue (book_id, issued_to, issued_on, return_on, current_fine, fine_paid, payment_transaction_id)
VALUES 
    ('book1', 'reader1', '2023-06-15', '2023-07-01', 2.50, true, 'PAY123'),
    ('book2', 'reader2', '2023-07-01', '2023-07-15', 1.25, false, NULL),
    ('book3', 'reader1', '2023-07-10', NULL, 0.00, false, NULL),
    ('book4', 'reader3', '2023-07-05', '2023-07-20', 0.75, false, NULL);
