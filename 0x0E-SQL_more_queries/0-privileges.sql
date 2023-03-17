-- Lists all privileges of the MySQL users user_0d_1 and user_0d_2 on the local server (localhost)

-- Switch to the mysql system database
USE mysql;

-- Display the privileges for each user using SHOW GRANTS
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
