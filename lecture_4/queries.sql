-- ASSIGNMENT: Student Grades Manager
-- MISSION: Create a relational database for students and their grades

-- TABLE CREATION
-- Students table stores basic student information
CREATE TABLE IF NOT EXISTS students (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  full_name TEXT,
  birth_year INTEGER
);

-- Grades table stores student grades with referential integrity
CREATE TABLE IF NOT EXISTS grades (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  student_id INTEGER,
  subject TEXT,
  grade INTEGER CHECK(grade BETWEEN 1 AND 100),
  FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
);

-- DATA CLEANUP
-- Remove existing data to avoid duplicates when re-running script
DELETE FROM grades;
DELETE FROM students;

-- DATA INSERTION
-- Insert students with their birth years
INSERT INTO students (full_name, birth_year)
VALUES
    ('Alice Johnson', 2005),
    ('Brian Smith', 2004),
    ('Carla Reyes', 2006),
    ('Daniel Kim', 2005),
    ('Eva Thompson', 2003),
    ('Felix Nguyen', 2007),
    ('Grace Patel', 2005),
    ('Henry Lopez', 2004),
    ('Isabella Martinez', 2006);

-- Insert grades for various subjects
INSERT INTO grades (student_id, subject, grade)
VALUES
    (1, 'Math', 88),
    (1, 'English', 92),
    (1, 'Science', 85),
    (2, 'Math', 75),
    (2, 'History', 83),
    (2, 'English', 79),
    (3, 'Science', 95),
    (3, 'Math', 91),
    (3, 'Art', 89),
    (4, 'Math', 84),
    (4, 'Science', 88),
    (4, 'Physical Education', 93),
    (5, 'English', 90),
    (5, 'History', 85),
    (5, 'Math', 88),
    (6, 'Science', 72),
    (6, 'Math', 78),
    (6, 'English', 81),
    (7, 'Art', 94),
    (7, 'Science', 87),
    (7, 'Math', 90),
    (8, 'History', 77),
    (8, 'Math', 83),
    (8, 'Science', 80),
    (9, 'English', 96),
    (9, 'Math', 89),
    (9, 'Art', 92);

-- REQUIRED QUERIES

-- Find all grades for a specific student (Alice Johnson)
-- Returns all subjects and grades for Alice Johnson
SELECT g.subject, g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE s.full_name = 'Alice Johnson'
ORDER BY g.subject;

-- Calculate the average grade per student
-- Computes average grade for each student, rounded to 2 decimal places
SELECT
    s.full_name,
    ROUND(AVG(g.grade), 2) AS average_grade
FROM students s
JOIN grades g ON g.student_id = s.id
GROUP BY s.id, s.full_name
ORDER BY average_grade DESC;

-- List all students born after 2004
-- Simple filter query for students born after 2004
SELECT s.full_name
FROM students s
WHERE s.birth_year > 2004;

-- List all subjects and their average grades
-- Calculates average grade for each subject across all students
SELECT
    g.subject,
    ROUND(AVG(g.grade), 2) as avg_grade
FROM grades g
GROUP BY subject;

-- Find the top 3 students with the highest average grades
-- Limits results to top 3 students by average grade
SELECT
    s.full_name,
    ROUND(AVG(g.grade), 2) as avg_grade
FROM students s
JOIN grades g ON g.student_id = s.id
GROUP BY s.id, s.full_name
ORDER BY avg_grade DESC
LIMIT 3;

-- Show all students who have scored below 80 in any subject
-- Returns distinct student names with at least one grade below 80
SELECT s.full_name
FROM students s
JOIN grades g ON g.student_id = s.id
WHERE g.grade < 80
ORDER BY s.full_name;

-- OPTIMIZATION

-- Index for faster JOIN operations on student_id
CREATE INDEX idx_grades_student ON grades(student_id);

-- Index for faster birth_year filtering
CREATE INDEX idx_students_birth ON students(birth_year);

-- Index for faster grade range queries
CREATE INDEX idx_grades_grade ON grades(grade);