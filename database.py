from mysql.connector import connection
print("hi")
mydb = connection.MySQLConnection(
    host ="localhost",
    user ="root",
    password ="Shraddha#14",database ="college7")
db_cursor = mydb.cursor()
print("connected ")
# db_cursor.execute("create database college7")
# print("database created")
# db_cursor.execute("create table student(stu_id int primary key,std_name varchar(20),std_class varchar(20))")
# print("table created")
# db_cursor.execute("show tables")
# for i in db_cursor:
#     print(i)

# db_cursor.execute("INSERT INTO student VALUES (1, 'richa', 'data science')")
# mydb.commit()
# print(db_cursor.rowcount, "record inserted")

# db_cursor.execute("SELECT * FROM student")
# # Fetch all the rows from the query result
# db_select = db_cursor.fetchall()
# # Print the fetched records
# print(db_select)



# db_cursor.execute("delete from student where stu_id =1")
# mydb.commit()
# print(db_cursor.rowcount,"row deleted")

# db_cursor.execute("UPDATE student SET std_name = 'nilu' WHERE stu_id = 1")
# mydb.commit()
# print(db_cursor.rowcount, "record updated")



