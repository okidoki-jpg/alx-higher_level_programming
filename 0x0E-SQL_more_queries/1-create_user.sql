/**
 * Create the MySQL server user user_0d_1 with all
 * privileges
 */

-- Create the user_0d_1 user and set their password to user_0d_1_pwd
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user_0d_1 user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Flush to save the privileges
FLUSH PRIVILEGES;
