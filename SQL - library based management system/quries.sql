-- Retrieve all books issued to a specific reader
SELECT b.book_id, b.book_name, b.author_id, a.first_name AS author_first_name, a.last_name AS author_last_name
FROM library_management.books_issue bi
JOIN library_management.books b ON bi.book_id = b.book_id
JOIN library_management.author a ON b.author_id = a.author_id
WHERE bi.issued_to = 'reader1';

-- List all books published by a specific publisher
SELECT b.book_id, b.book_name, b.release_date
FROM library_management.books b
JOIN library_management.publisher p ON b.publisher_id = p.publisher_id
WHERE p.publisher_name = 'Penguin Books';

-- Calculate the total number of books issued by each reader
SELECT r.reader_id, r.first_name, r.last_name, COUNT(bi.book_id) AS total_books_issued
FROM library_management.readers r
LEFT JOIN library_management.books_issue bi ON r.reader_id = bi.issued_to
GROUP BY r.reader_id, r.first_name, r.last_name;

-- Retrieve details of books issued by readers with fines greater than $1.00
SELECT bi.book_id, b.book_name, bi.issued_to, bi.current_fine
FROM library_management.books_issue bi
JOIN library_management.books b ON bi.book_id = b.book_id
JOIN library_management.readers r ON bi.issued_to = r.reader_id
WHERE r.current_fine > 1.00;

-- List all books with their availability status (available or not)
SELECT book_id, book_name, CASE WHEN is_available THEN 'Available' ELSE 'Not Available' END AS availability_status
FROM library_management.books;

-- Find the top 3 authors with the highest publications count
SELECT author_id, first_name, last_name, publications_count
FROM library_management.author
ORDER BY publications_count DESC
LIMIT 3;

-- Total fine collected by the library
SELECT SUM(total_fine) AS total_fine_collected
FROM library_management.readers;

-- Find the average number of books issued per reader
SELECT AVG(books_issued_total) AS avg_books_issued_per_reader
FROM library_management.readers;
