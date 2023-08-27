from databaselib import mycursor,mydb
import datetime
import traceback


class Student:

    def __init__(self, student_id, username, password, first_name, last_name, email, phone_number, books_loaned):
        self.student_id = student_id
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.books_loaned = books_loaned

    @classmethod
    def student_constructor(cls,student_data):
        return cls(student_data[0],student_data[1],student_data[2],student_data[3],student_data[4],student_data[5],student_data[6], student_data[7])


class Book:
    def __init__(self, book_id, name, genre, available_copies, description):
        self.book_id = book_id
        self.name = name
        self.genre = genre
        self.available_copies = available_copies
        self.description = description
    
    @classmethod
    def book_constructor(cls, book_data):
        return cls(book_data[0], book_data[1], book_data[2], book_data[3], book_data[4])




def login():
    """
        With this method the User logs in to the library portal

    """
    try:
        student_logged_in = ()
        username_holder = input("Please type your username: ")
        password_holder = input("Please type your password: ")

        mycursor.execute("SELECT * FROM student WHERE username = %s AND password = %s", (username_holder,password_holder))

        userlog = mycursor.fetchall()
        if userlog:
            print(f'Welcome back {userlog[0][3]}')
            student_logged_in = Student.student_constructor(userlog[0])
        else:
            print("Your login details don't match")
            login()
    
        if student_logged_in:
            user_actions(student_logged_in)
            return 1
        else:
            return 0
    except Exception as e:

        print(e)
        logout = input("The values that you entered are not valid. If you wish to try again, press enter a random key and follow the instructions closely. If you wish to log out, press y: ")
        if logout == 'y':
            print("goodbye")
        else:
            login()   



def signup():
    """
        With this method, a User can sign up to the library portal. Once he
        follows the instructions, their info will be stored in the database

    """
    try:
    
        student_info =  []

        student_info.append(input("Please type your username: "))

        password_holder = input("Please type your password: ")
        confirm_password_holder = ''

        while (password_holder != confirm_password_holder) and (password_holder != ''):
            print("The passwords dont match")
            confirm_password_holder = input("Please repeat your password: ")

            if password_holder == confirm_password_holder:
                student_info.append(password_holder)

        student_info.append(input("Please type your first name: "))
        student_info.append(input("Please type your last name: "))
        student_info.append(input("Please type your email: "))
        student_info.append(input("Please type your phone number: "))

        #The program will now make sure that there isnt a user already signed with the same username or email. If there is one, the user will be asked to repeat

        mycursor.execute("SELECT username, email FROM student")
        usersign = mycursor.fetchall()
        for data in usersign:
            if data[0] == student_info[0]:
                print("There is already a user with the same username, please try again")
                signup()
            elif data[1] == student_info[4]:
                print("There is already a user with the same email, please try again")
                signup()
        mycursor.execute("INSERT INTO student (username, password, firstname, lastname, email, phone_number) VALUES (%s,%s,%s,%s,%s,%s)",student_info)
        mydb.commit()
        print("Your sign up was a success!")

    except Exception as e:
        print(e)
        logout = input("The values that you entered are not valid. If you wish to try again, press enter a random key and follow the instructions closely. If you wish to log out, press y: ")
        if logout == 'y':
            print("goodbye")
        else:
            signup()       




def user_actions(student):
    """
        With this method, once the user log in he can choose what action he wants to take

    """
    
    #due_date function is called in case the student holds a book for 30 days or over
    print(f'{student.first_name}, you have borrowed {student.books_loaned} books')
    due_date(student)
    
    
    
    #By typing 1,2 or 3, the user can choose if he wants to loan a book, return a book or exit the program
    
    action_to_take = input("Please select the action that you want to take by typing the number of the action:\n(1)Loan a book\n(2)Return a book\n(3)Exit\n")
    
    if action_to_take == '1':
        loan_a_book(student)
    elif action_to_take == '2':
        return_a_book(student)
    elif action_to_take == '3':
        pass
    else:
        print("Please follow the instructions closely")
        user_actions(student)
    
    return 1





def loan_a_book(student):
    
    """
        With this method, The user can choose the book that he wants to loan
    
    """
    
    try:
        
        #The different genres of books that exist in the database will be presented to the user so he can choose

        mycursor.execute("SELECT distinct(genre) from book")
        book_genres = mycursor.fetchall()
        counter=1
        
        for genre in book_genres:
            print(f'({counter})' + genre[0])
            counter+=1
        book_genre = int(input("Please select the genre of the books that you want to see: "))

        
        # A detailed list of all the books where their genre is the previous selection of the user
        mycursor.execute("SELECT * FROM book WHERE genre = %s", book_genres[book_genre-1])
        
        book_collection = mycursor.fetchall()
        for book in book_collection:
            print(f'Book id: {book[0]}\nBook title: {book[1]}\nBook Genre: {book[2]}\nAvailable copies: {book[3]}\nDescription:{book[4]}\n')
        
        book_selection = int(input("Please type the id of the book that you want to loan: "))
        
        if student.books_loaned == 3:
            print("You already have 3 books in your possesion")
        else:
            book_selection = (book_selection,)
            mycursor.execute("SELECT* FROM book WHERE book_id = %s ",(book_selection))
            book_selected = mycursor.fetchall()
            new_book = Book.book_constructor(book_selected[0])


            if new_book.available_copies > 0:
                mycursor.execute("INSERT INTO student_loans (student_id, book_id, day_loaned) VALUES (%s, %s, %s)",(student.student_id, new_book.book_id,datetime.datetime.now()))
                mycursor.execute("UPDATE student SET books_loaned = %s WHERE student_id = %s",(student.books_loaned+1, student.student_id))
                mycursor.execute("UPDATE book SET available_copies= %s WHERE book_id = %s",(new_book.available_copies-1,new_book.book_id,))
                mydb.commit()
                print(f'You have successfully borrowed the book {new_book.name}')
            else:
                print("There are no available copies from the book that you selected")
        
        return 1

    except Exception as e:
        print(e)
        logout = input("The values that you entered are not valid. If you wish to try again, follow the instructions closely. If you wish to log out, press y")
        if logout == 'y':
            print("goodbye")
        else:
            loan_a_book(student)





def return_a_book(student):
    """
    With this method, the student can return a book that he has loaned previously
    """
    try:
        if student.books_loaned > 0:
            mycursor.execute("SELECT * FROM student_loans WHERE student_id = %s", (student.student_id,))
            loans_of_student = mycursor.fetchall()

            print("Here are the books that you have loaned:")
            counter = 1
            for loan in loans_of_student:
                mycursor.execute("SELECT * from book WHERE book_id = %s", (loan[2],))
                booksloaned = mycursor.fetchall()

                for book in booksloaned:
                    print(f'Book {counter}\nID: {book[0]}\nBook title: {book[1]}\nBook genre:{book[2]}\n')
                    counter+=1
            
            book_to_return = int(input('Please select the book that you want to return by typing its id: '))

            for loan in loans_of_student:
                if (loan[1] == student.student_id) and (loan[2] == book_to_return):
                    mycursor.execute("DELETE FROM student_loans WHERE student_id = %s AND book_id = %s", (student.student_id,book_to_return))
                    mycursor.execute("UPDATE student SET books_loaned=%s WHERE student_id = %s", (student.books_loaned-1,student.student_id))
                    mycursor.execute("UPDATE book SET available_copies =available_copies+1 WHERE book_id  = %s",(book_to_return,))
                    mydb.commit()
                    print("You have returned the book")
                    break
        
        else:
            print("You have no books to return")
        
        return 1
    
    except Exception as e:
        print(e)
        logout = input("The values that you entered are not valid. If you wish to try again, follow the instructions closely. If you wish to log out, press y: ")
        if logout == 'y':
            print("goodbye")
        else:
            return_a_book(student)    

    

        

def due_date(student):
    """
    This method checks if the student has loaned a book for over 30 days and asks him to return it
    """
    try:
        mycursor.execute("SELECT * FROM student_loans WHERE student_id = %s", (student.student_id,))
        loans_of_student = mycursor.fetchall()
        for loan in loans_of_student:

            delta = datetime.datetime.now() - datetime.datetime.strptime(loan[3], '%Y-%m-%d %H:%M:%S.%f')
            if delta.days >= 30:
                mycursor.execute("SELECT name FROM book WHERE book_id = %s", (loan[2],))
                book = mycursor.fetchall()
                print(f'There have been 30 days since you loaned the book named {book[0]}. You will be immediately given the option to return it.')
                if return_a_book(student) == 1:
                    print("Thank You for returning the book")
        
        return 1
    
    except Exception as e:
        print(e)  


