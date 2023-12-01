-- listind previlegs of MYSQL server
REVOKE ALL PRIVILEGES ON *.* FROM 'user_0d_1'@'localhost', 'user_0d_2'@'localhost';
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
