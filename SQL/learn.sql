CREATE DATABASE collage;

USE collage;
/* CREATE TABLE*/
CREATE TABLE student(
    rollno INT PRIMARY KEY,
    name VARCHAR(50)
);
-- SELECT & view all coloum --

SELECT * FROM student;

-- INSERT in TABLE--

INSERT INTO student
(rollno,name)
VALUES
(1,'jeevanshu'),
(2,"abhinav"),
(3,"kallu"),
(4,"piyush");

-- primary key --
CREATE Table city(
    id int,
    name varchar(50),
    age INT,
    city varchar(50),
    PRIMARY KEY(id,name) -- it gives unique combination of id and name --
);

INSERT INTO city
(id,name,age,city)
VALUES
(1,'jeevanshu',20,'Delhi'),
(2,'abhinav',22,'Mumbai'),
(1,'kallu',21,'Bangalore'),
(4,'piyush',23,'mumbai');


SELECT * FROM city;
SELECT name,city FROM city;
SELECT DISTINCT id FROM city; -- distinct use unique id --

-- where clause --
SELECT * FROM city WHERE age>21;
SELECT * FROM city WHERE city='Delhi';
SELECT * FROM city where age>21 AND city='mumbai';

-- limit clause --
SELECT * FROM city LIMIT 2; -- limit use for select only 2 row of table
SELECT * FROM city WHERE age>21 LIMIT 2 ; 

-- order by clause --
select * from city order by age desc;
select * from city order by age asc;
select * from city order by city desc;
select * from city order by city asc;

-- aggregate function :- count(),sum(),avg(),min(),max() --
SELECT MAX(age) FROM city;
SELECT MIN(age) FROM city;
SELECT AVG(age) FROM city;
SELECT COUNT(id) FROM city;

-- group by clause :- groups row that have same value in summary rows . 
CREATE Table students(
    rollno int PRIMARY KEY,
    name varchar(50),
    marks INT NOT NULL,
    grade varchar(10),
    city VARCHAR(50)
);
INSERT INTO students(rollno, name, marks, grade, city)
 VALUES
(101, 'Anil', 78, 'C', 'Pune'),
(102, 'Bhumika', 93, 'A', 'Mumbai'),
(103, 'Chetan', 85, 'B', 'Delhi'),
(104, 'Dhruv', 96, 'A', 'Delhi'),
(105, 'Eman', 12, 'F', 'Delhi'),
(106, 'Farah', 82, 'B', 'Delhi'),
(107, 'Gaurav', 67, 'C', 'Noida'),
(108, 'Harsh', 91, 'A', 'Gurgaon'),
(109, 'Isha', 74, 'C', 'Pune'),
(110, 'Jatin', 88, 'B', 'Mumbai');
SELECT city, COUNT(rollno) 
FROM students 
GROUP BY city ; 

-- having clause :- used to filter the records after group by clause --
SELECT city, COUNT(rollno) 
FROM students 
GROUP BY city 
HAVING max(marks)>85;

--# General order of clauses :- select, from, where, group by, having, order by, limit --

-- default value --
CREATE table emp(
    id INT,
    salary INT DEFAULT 10000,
    PRIMARY KEY(id) 
);

INSERT INTO emp(id)VALUES(101);
SELECT * FROM emp;

# UPDATE COMMAND :- update the value of a column in a table --
SET SQL_SAFE_UPDATES = 0; -- 0 = safe mode off , 1 = safe mode on --
UPDATE students
SET grade = 'o'
WHERE grade ='A';

SELECT * FROM students;

# DELETE COMMAND :- delete the row from a table --
DELETE FROM students
WHERE marks < 30;

SELECT * FROM students;



