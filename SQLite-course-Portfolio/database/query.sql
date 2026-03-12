PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT
);
INSERT INTO customers VALUES(1,'Alice','alice@example.com','0712345678');
INSERT INTO customers VALUES(2,'Bob','bob@example.com','0723456789');
COMMIT;
