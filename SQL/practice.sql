-- Q1  create database for your company xyz company and CREATE a TABLE inside a db to store emplooye info (id,name,salary)and then SELECT and view --
CREATE DATABASE google;
USE google;

CREATE TABLE emplooye(
    id INT PRIMARY KEY,
    name VARCHAR(100),
    salary INT
);
INSERT INTO emplooye
(id ,name, salary)
VALUES
(1,"jeevanshu",40000),
(2,"abhinav",40000),
(3,"vishu",40000);
 
 SELECT * FROM emplooye;

-- Q2 create a sample data of college student info and insert the data-- 
CREATE DATABASE IAMR;
USE IAMR;
CREATE Table student(
    rollno int PRIMARY KEY,
    name varchar(50),
    marks INT NOT NULL,
    grade varchar(10),
    city VARCHAR(50)
);

INSERT INTO student
(rollno,name,marks,grade,city) 
VALUES
(101,'jeevanshu',90,'A','delhi'),
(102,'abhinav',80,'B','mumbai'),
(103,'vishu',85,'C','bangalore'),
(104,'kallu',90,'A','delhi'),
(105,'piyush',85,'B','chennai');

SELECT * FROM student; -- * use for select whole table and view all coloum of table --

SELECT name,marks FROM student; -- select specific coloum of table --
SELECT  DISTINCT city FROM student; --  distinct use unique  city --

--Q3 write query to find avg marks in each city in ascending order --
select city,avg(marks) 
from student 
group by city 
 order by avg(marks) asc;

 -- Q4  A :in the kids table change the name into full name
 CREATE Table kids(
    rollno int PRIMARY KEY,
    name varchar(50),
    marks INT NOT NULL,
    grade varchar(10),
    city VARCHAR(50)
);
INSERT INTO kids
(rollno,name,marks,grade,city) 
VALUES
(101,'jeevanshu',90,'A','delhi'),
(102,'abhinav',80,'B','mumbai'),
(103,'vishu',85,'C','bangalore'),
(104,'kallu',90,'A','delhi'),
(105,'piyush',85,'B','chennai');

SELECT * FROM kids;
         ALTER TABLE student
         CHANGE name full_name VARCHAR(50); 
    --  B : delete all student who scored less than 80
         DELETE FROM kids WHERE marks<80;

    --  C : delete grade column  --
    ALTER TABLE kids
    DROP COLUMN grade;


 --Q4 find the total payment according to each payment method -- 
 CREATE TABLE payment(
    customer_id INT PRIMARY KEY,
    customer VARCHAR(20),
    mode VARCHAR(20),
    city VARCHAR(20)
 );
 INSERT INTO payment
 (customer_id,customer,mode,city)
 VALUES
 (101, 'Olivia Barrett', 'Netbanking', 'Portland'),
(102, 'Ethan Miller', 'Credit Card', 'Miami'),
(103, 'Maya Patel', 'Credit Card', 'Seattle'),
(104, 'Liam Carter', 'Netbanking', 'Denver'),
(105, 'Sophia Gomez', 'Credit Card', 'New Orleans'),
(106, 'Lucas Vance', 'Debit Card', 'Phoenix'),
(107, 'Emma Watson', 'UPI', 'Boston'),
(108, 'Aiden Clark', 'Debit Card', 'Austin'),
(109, 'Zoe Harris', 'Netbanking', 'Nashville'),
(110, 'Noah Young', 'Cash', 'San Jose'),
(111, 'Ava Mitchell', 'Debit Card', 'Chicago'),
(112, 'Mason Scott', 'UPI', 'Dallas'),
(113, 'Isabella King', 'Credit Card', 'Atlanta'),
(114, 'James Wright', 'Cash', 'Houston'),
(115, 'Amelia Green', 'UPI', 'San Diego'),
(116, 'Logan Baker', 'Netbanking', 'San Francisco'),
(117, 'Mia Adams', 'Debit Card', 'Las Vegas'),
(118, 'Benjamin Nelson', 'Credit Card', 'New York'),
(119, 'Charlotte Hill', 'UPI', 'Philadelphia'),
(120, 'Elijah Perez', 'Cash', 'Detroit');
 
SELECT mode, COUNT(customer) FROM payment GROUP BY mode;