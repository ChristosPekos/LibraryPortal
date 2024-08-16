import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host = '',
    user = '',
    passwd = '',
)

mycursor = mydb.cursor()


#mycursor.execute("CREATE DATABASE librarydb")



"""
#mycursor.execute("CREATE TABLE student (student_id int PRIMARY KEY AUTO_INCREMENT, username VARCHAR(50), password VARCHAR(50), firstname VARCHAR(50), lastname VARCHAR(50), email VARCHAR(50), phone_number VARCHAR(50), books_loaned int DEFAULT 0)")

#mycursor.execute("CREATE TABLE book (book_id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), genre VARCHAR(255), available_copies int, book_description text)")

#mycursor.execute("CREATE TABLE student_loans (loan_id int PRIMARY KEY AUTO_INCREMENT, student_id int, book_id int, FOREIGN KEY(student_id) REFERENCES student(student_id), FOREIGN KEY(book_id) REFERENCES book(book_id), day_loaned VARCHAR(200) DEFAULT %s)",(datetime.datetime.now(),))
"""


"""
sqlFormula = "INSERT INTO student (username, password, firstname, lastname, email, phone_number) VALUES (%s,%s,%s,%s,%s,%s)"
students = [('christos123', '87654321', 'Christos', 'Pekos', 'christospekos@test.com', 6933), 
            ('Takis123', '12345678', 'Takis', 'Grigoriou', 'takisgrigoriou@test.com', 6953), 
            ('Jimmy123', 'abcdefg', 'Jimmy', 'Jones', 'jimmyjones@test.com', 6956),
            ('billystudent', 'testpass', 'Vasilis', 'Ioannou', 'billyion@test.com', 6957),
            ('kostakis2000', 'asdfg', 'Kostas', 'Papas', 'kostpap@test.com', 6958),
            ('giannakisxd', 'ilovemydog', 'Giannis', 'Markou', 'giannismark@test.com', 6959),
            ('tasos45467', 'iwatchanime', 'Tasos', 'Papanikolaou', 'tasospapnk@test.com', 6960),
            ('nikolakis', 'spotifypremium', 'Nikolas', 'Rerras', 'nikosrerras@test.com', 6961),
            ('isidori', 'doglover123', 'Isidora', 'Oikonomidou', 'isidoik@test.com', 6962),
            ('kayylou', 'verylucky', 'Kuriaki', 'Lioumi', 'kaylou@test.com', 6963)]

mycursor.executemany(sqlFormula,students)
mydb.commit()

"""

"""
sqlFormula = "INSERT INTO book (name, genre, available_copies, book_description) VALUES (%s,%s,%s,%s)"
books = [('The Martian', 'Science fiction', 3, "The Martian tells the story of Mark Watney, an astronaut on the Ares 3 mission to Mars. After a terrible storm almost destroys the ship and the base, the crew of his ship believe he is dead. 1). Alone on the red planet, he has to survive until the next mission to Mars arrives."), 
            ('Outlander', 'Romance Novel', 2, "strong-willed and sensual Claire Randall leads a double life with a husband in one century, and a lover in another. Torn between fidelity and desire, she struggles to understand the pure intent of her heart."), 
            ('It ends With Us', 'Romance Novel', 1, "The book follows a girl named Lily who has just moved and is ready to start her life after college. Lily then meets a guy named Ryle and she falls for him. As she is developing feelings for Ryle, Atlas, her first love, reappears and challenges the relationship between Lily and Ryle."),
            ('In Cold Blood', 'True Crime', 4, "In Cold Blood is a non-fiction novel by American author Truman Capote, first published in 1966. It details the 1959 murders of four members of the Clutter family in the small farming community of Holcomb, Kansas."),
            ('The Notebook', 'Romance Novel', 2, "The story centers on the relationship between Noah Calhoun and Allie Nelson. Spanning over five decades, their love endures an uncertain beginning, the onset and conclusion of World War II, the death of one child, and Allie's eventual diagnosis of Alzheimer's disease"),
            ('The things We Never Got Over', 'Romance Novel', 2, "A runaway bride who finds herself in a small town she's unfamiliar with while her life falls apart. Naomi is now single, jobless, broke, homeless, and the 11-year-old niece she just found out about is suddenly in her care."),
            ('Jane Eyre', 'Romance Novel', 2, "The novel follows the story of Jane, a seemingly plain and simple girl as she battles through life's struggles. Jane has many obstacles in her life - her cruel and abusive Aunt Reed, the grim conditions at Lowood school, her love for Rochester and Rochester's marriage to Bertha."),
            ('7 days in June', 'Romance Novel', 2, "With its keen observations of creative life in America today, as well as the joys and complications of being a mother and a daughter, Seven Days in June is a hilarious, romantic story of two writers discovering their second chance at love"),
            ('Dune', 'Science Fiction', 2, "'Dune' tells the story of Paul Atreides, a brilliant and gifted young man born into a great destiny beyond his understanding, who must travel to the most dangerous planet in the universe to ensure the future of his family and his people."),
            ('The Time Machine', 'Science Fiction', 2, "One of the most radical aspects of The Time Machine is that it questions the centrality of human beings to history by challenging the notion that humans will endure in their present form forever."),
            ('Helter Skelter', 'True Crime', 4, "The book recounts and assesses the investigation, arrest, and prosecution of Charles Manson and his followers for the notorious 1969 murders of Leno and Rosemary LaBianca, actress Sharon Tate, and several others."),
            ('Alias Grace', 'True Crime', 4, "Alias Grace is based on the grisly double murder that took place in July 1843 in a village 16 miles out of Toronto, in Upper Canada, when two of Thomas Kinnear's servants, 20-year-old James McDermott and 16-year-old Grace Marks, were charged with killing Kinnear and his housekeeper and lover, Nancy Montgomery."),
            ('1776', 'Historical', 4, "In October of 1775, the Revolutionary War is just beginning. American “rebels” have fired on British soldiers at Lexington and Concord, and King George III of England proposes sending thousands of additional troops, including German mercenaries known as Hessians, to America to quell the uprising."),
            ('Beloved', 'Historical', 4, "The work examines the destructive legacy of slavery as it chronicles the life of a Black woman named Sethe, from her pre-Civil War days as a slave in Kentucky to her time in Cincinnati, Ohio, in 1873.")]


mycursor.executemany(sqlFormula,books)
mydb.commit()

"""

