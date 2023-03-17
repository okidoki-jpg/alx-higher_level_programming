-- Create database hbtn_0d_2 if it doesn't already exist

CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;

-- Create user user_0d_2 if it doesn't already exist and set the password to user_0d_2_pwd
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege to user_0d_2 on database hbtn_0d_2
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
