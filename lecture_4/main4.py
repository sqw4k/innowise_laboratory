#program for create database

import sqlite3

#error handling
try:
    school_db = sqlite3.connect('school.db')

    #create cursor
    cursor = school_db.cursor()

    #create student table
    cursor.execute(""" CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        birth_year INTEGER
        );
    """)

    #create grades table
    cursor.execute(""" CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject TEXT,
        grade INTEGER CHECK(grade BETWEEN 1 AND 100),
        FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
        );
    """)

    #delete old data if it exists
    cursor.execute("DELETE FROM grades")
    cursor.execute("DELETE FROM students")
    #also delete autoincrements
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='students'")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='grades'")

    #insert data
    cursor.execute(""" INSERT INTO students (full_name, birth_year) VALUES 
        ('Alice Johnson', 2005),
        ('Brian Smith', 2004),
        ('Carla Reyes', 2006),
        ('Daniel Kim', 2005),
        ('Eva Thompson', 2003),
        ('Felix Nguyen', 2007),
        ('Grace Patel', 2005),
        ('Henry Lopez', 2004),
        ('Isabella Martinez', 2006);
    """)

    cursor.execute(""" INSERT INTO grades (student_id, subject, grade) VALUES 
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
    """)
    school_db.commit()
    print("Database created successfully!")
except Exception as e:
    print(f"Error: {e}")
    school_db.rollback()
finally:
    school_db.close()