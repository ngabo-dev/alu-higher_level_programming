-- updating the score of Bob to 10 using only the name field

UPDATE second_name(id INT, name VARCHAR, score INT);
SET score = 10
WHERE name = 'Bob';
