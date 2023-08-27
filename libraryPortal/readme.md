INSTALL INSTRUCTIONS

For the program to work, you need to have mysql and a python 3 version installed.

Once those are installed, you need to go to the databaselib.py file and: 

1.type your system's info (host, user, passwd ) inside the ''. 

2.Once you do that, you need to comment out and run the
#mycursor.execute("CREATE DATABASE librarydb") command.

3.once you do that, in the mysql connector{}  type: database = 'librarydb'.

4.Next you need to remove the """ """ from each comment and run it. Now the database is good to go!




RUN INSTRUCTIONS

To run the program, run the lib.py file.

Once you run the lib.py module, you have  2 options:

1.You can choose to sign up, and a new user will be created, while his data will be stored in the database

2.You can choose to log in, so here are some data of users already created:

username = Takis123
password = 12345678

username = Jimmy123
password = abcdefg

If you want to use another account you can look at the databaselib.py module for more user data.

Once you are logged in, the program will guide you through with instructions.

In case you want to check how the program changes the database data, copy and paste these in the lib.py module:


mycursor.execute("SELECT * FROM student")

myresult = mycursor.fetchall() 

for row in myresult:
    print(row)


mycursor.execute("SELECT * FROM book")

myresult = mycursor.fetchall()

for row in myresult:
    print(row)


mycursor.execute("SELECT * FROM student_loans")

myresult = mycursor.fetchall()

for row in myresult:
    print(row)