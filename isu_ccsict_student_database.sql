use isu_students_database;

create table isu_ccsict_student_info

(
Student_ID varchar(40) NOT NULL,
Last_Name varchar(100) NOT NULL,
First_Name varchar(100) NOT NULL,
Birthday date NOT NULL,
Address varchar(200) NOT NULL,
Phone_Number varchar(20) NOT NULL,
School_Department varchar(50) NOT NULL,
Course varchar (50) NOT NULL,
Student_Year varchar(50) NOT NULL
);

INSERT INTO isu_ccsict_student_info (Student_ID, Last_Name, First_Name, Birthday, Address, Phone_Number, School_Department, Course, Student_Year)
VALUES('21-10935', 'Comia', 'Dhon Amado', '2002-06-05', 'Labinab Cauayan City Isabela', '09XXXXXXXXX', 'CCSICT', 'BSCS', '2nd'),
('21-10948', 'Ganiola', 'Reymerson', '2003-04-05', 'Palanan', '09XXXXXXXXX', 'CCSICT', 'BSCS', '2nd'),
('21-10952', 'Delos Reyes', 'John Paul', '2003-03-30', 'Santiago Quirino Isabela', '09XXXXXXXXX', 'CCSICT', 'BSCS', '2nd'),
('21-11566', 'Morete', 'Christian Arthur', '2003-12-31', 'Guabal Cauayan City Isabela', '09XXXXXXXXX', 'CCSICT', 'BSCS', '2nd');

