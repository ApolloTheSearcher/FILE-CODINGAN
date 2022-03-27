CREAT TABLE friends(
    id INTEGER,
    name TEXT,
    birthday DATE
);

INSERT INTO friends(id, name, birthday)
VALUES (1, "Ororo Munroe", "1940-05-30");
INSERT INTO friends(id, name, birthday)
VALUES (2, "Gentha Ardaana", "2005-01-27");
INSERT INTO friends(id, name, birthday)
VALUES (3, "Gibran", "1992-01-24");

-- Mengganti nama Ororo Munroe
UPDATE friends
SET name = "Storm"
WHERE id = 1;

-- Menambahkan column email 
ALTER TABLE friends
ADD COLUMN email TEXT;
-- jika belum di isi maka columnya akan null

-- menambahkan email ke id 1
UPDATE friends
SET email = "storm@codecademy.com"
WHERE id = 1;

-- jika kita ingin mendelete column 1
-- DELETE FROM friends
-- WHERE id = 1;

-- Untuk menampilkan tabel
SELECT * FROM friends;