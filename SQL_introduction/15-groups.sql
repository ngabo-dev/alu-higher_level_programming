-- a script that lists all records of the table second_table of the database hbtn_0c_0

SELECT `score`, COUNT(`score`) AS `number` FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
