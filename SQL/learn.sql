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

# Foreign Key () REFERENCES ()

CREATE TABLE department(
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

INSERT INTO department
(dept_id,dept_name)
VALUES
(1,'Computer Science'),
(2,'Mathematics'),
(3,'Physics'),
(4,'Chemistry');

UPDATE department
SET dept_id = 4
WHERE dept_id = 6;

select * from department;

CREATE Table teacher(
    teacher_id INT PRIMARY KEY,
    teacher_name VARCHAR(50),
    dept_id INT,
    FOREIGN KEY(dept_id) REFERENCES department(dept_id)
    on DELETE CASCADE -- when you delete a row in the parent table, the child table is also deleted 
    on UPDATE CASCADE -- when you update a row in the parent table, the child table is also updated
)

INSERT INTO teacher
(teacher_id,teacher_name,dept_id)
VALUES
(1,'Rahul',1),
(2,'Ravi',2),
(3,'Raj',3),
(4,'Rajesh',4);

select * from teacher;

# alter table :- add column, drop column, modify column, rename column --

ALTER TABLE teacher
ADD COLUMN salary int NOT NULL DEFAULT 30000 ;

ALTER TABLE teacher
DROP COLUMN salary;

ALTER TABLE teacher
RENAME COLUMN new_salary TO salary;

ALTER TABLE teacher 
MODIFY COLUMN salary int NOT NULL DEFAULT 40000;

# truncate table :- delete all rows from a table but not the structure of the table --
TRUNCATE TABLE teacher;

# join :- inner join, left join, right join, full outer join --
# join :- used to combine rows from two or more tables based on a related column between them --
SELECT * FROM student;
SELECT * from city;

# inner join :- returns records that have matching values in both tables --
 --Alias = short name of table --
SELECT * 
FROM student AS s  
INNER JOIN city AS c
ON s.rollno = c.id;

# left join :- returns all records from the left table and the matched records from the right table --
SELECT *  
FROM student AS s  
LEFT JOIN city AS c
ON s.rollno = c.id;

# right join :- returns all records from the right table and the matched records from the left table --
SELECT *    
FROM student AS s  
RIGHT JOIN city AS c
ON s.rollno = c.id;

# full outer join = union :- returns all records when there is match in left table and right table --
SELECT *    
FROM student AS s  
FULL OUTER JOIN city AS c
ON s.rollno = c.id;

# left excluisive join :- returns all records from the left table and the unmatched records from the right table --
SELECT *    
FROM student AS s  
LEFT OUTER JOIN city AS c
ON s.rollno = c.id;

# right excluisive join :- returns all records from the right table and the unmatched records from the left table --
SELECT *    
FROM student AS s  
RIGHT OUTER JOIN city AS c
ON s.rollno = c.id;

# self join :- used to join a table to itself as if the table were two tables, temporarily renaming at least one table in the SQL statement --
CREATE TABLE employee(
    id INT PRIMARY KEY,
    name VARCHAR(50),
    manager_id INT
);
INSERT INTO employee
(id,name,manager_id)
VALUES
(1,'jeevanshu',4),
(2,'abhinav',3),
(3,'vishu',2),
(4,'kallu',NULL),
(5,'piyush',4);

SELECT * FROM employee;

SELECT * 
FROM employee AS  a
JOIN employee AS  b 
ON a.id = b.manager_id;
