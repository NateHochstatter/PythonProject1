import sqlite3

conn = sqlite3.connect("Course.db")

#returns a database cursor object to execute sql statement
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS User")
cursor.execute("DROP TABLE IF EXISTS Course")
cursor.execute("DROP TABLE IF EXISTS Student")
cursor.execute("create table User ( " + "userId integer not null, username varchar(32) not null, "
                                        "password varchar(32) not null, primary key (userId))")

cursor.execute("insert into User (userId, username, password) values (1, 'stan0001', '@chapter1')")
cursor.execute("insert into User (userId, username, password) values (2, 'britt0002', 'password123')")

cursor.execute("create table Course ( " + "courseId char(5) not null, subjectId char(4) not null, "
                                        "courseNumber integer not null, title varchar(50) not null, "
                                        "numOfCredits integer not null, primary key (courseId))")

cursor.execute("insert into Course (courseId, subjectId, courseNumber, title, numOfCredits) values ("
               "'11111', 'CS', 1030, 'Python Programing 1', 3)")
cursor.execute("insert into Course (courseId, subjectId, courseNumber, title, numOfCredits) values ("
               "'11112', 'CS', 2030, 'Python Programing 2', 3)")

cursor.execute("create table Student ( " + "studentId integer, name varchar(30, age integer, gender char(1), "
                                           "major char(6), phone varchar(12), userId integer, foreign key (userId) "
                                           "references User(userId), primary key (studentId))")

cursor.execute("insert into Student (studentId, name, age, gender, major, phone, userId) values("
               "700300001, 'Stan Smith', 23, 'M', 'CS', '816-111-1111', 1)")