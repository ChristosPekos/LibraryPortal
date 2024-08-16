<h1 align="center" id="title">Public School Library Portal</h1>

<p id="description">Mock application for a public school library portal where students can browse through books and borrow the book of interest. The user logs in the application and the menu guides them through the preferred course of action.</p>

<h2>📷Project Screenshots</h2>
<img align="left" src="https://github.com/ChristosPekos/LibraryPortal/blob/cef07cf9ef5f2c2948b558c92cecbdbe659abafb/images/screenshot1.png" alt="screenshot1" width="300" height="200">
<img align="center" src="https://github.com/ChristosPekos/LibraryPortal/blob/cef07cf9ef5f2c2948b558c92cecbdbe659abafb/images/screenshot2.png" alt="screenshot2" width="500" height="200">
<img align="center" src="https://github.com/ChristosPekos/LibraryPortal/blob/cef07cf9ef5f2c2948b558c92cecbdbe659abafb/images/screenshot3.png" alt="screenshot3" width="400" height="200">
<img align="center" src="https://github.com/ChristosPekos/LibraryPortal/blob/cef07cf9ef5f2c2948b558c92cecbdbe659abafb/images/screenshot4.png" alt="screenshot4" width="900" height="600">
<img align="center" src="https://github.com/ChristosPekos/LibraryPortal/blob/cef07cf9ef5f2c2948b558c92cecbdbe659abafb/images/screenshot5.png" alt="screenshot5" width="600" height="200">


<h2>🛠️ Installation Steps:</h2>


For the program to work you need to have mysql and a python 3 version installed.

Then, run this command in your cmd:
```
pip install mysql-connector-python
```

Once those are installed you need to go to the databaselib.py file and:


<p>1. database connection</p>


type your system's info (host user passwd ) inside the ''.


<p>2. database initialization</p>


Once you do that you need to comment out and run the #mycursor.execute("CREATE DATABASE librarydb") command.



Then in the mysql connector{} type: database = 'librarydb'.


<p>3. adding data to the database</p>


Next you need to remove the """ """ from each comment and run it. Now the database is good to go!




<h2>🚀 How to Run</h2>


 <p>To run the program run the lib.py file.</p> 
 <p>Once you run the lib.py module you have 2 options: </p> 
 <p>1.You can choose to sign up and a new user will be created while his data will be stored in the database </p> 
 <p>2.You can choose to log in so here are some data of users already created: username = Takis123 password = 12345678.</p>  
 <p>Once you are logged in the program will guide you through with instructions. </p> 
 <p>In case you want to check how the program changes the database data copy and paste these in the lib.py module: </p> 

 ```
 mycursor.execute("SELECT * FROM student") 
 myresult = mycursor.fetchall() 
 for row in myresult: print(row) 
 mycursor.execute("SELECT * FROM book") 
 myresult = mycursor.fetchall() 
 for row in myresult: print(row) 
 mycursor.execute("SELECT * FROM student_loans") 
 myresult = mycursor.fetchall() 
 for row in myresult: print(row)
 ```




  
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   mysql
*   Python
