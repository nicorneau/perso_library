"""
perso_library.py
This is a program to keep track of a personal library.
@author : Nicolas Corneau-Tremblay
@sdate : 27/10/17
"""

# Book class.
class Book(object):
	"""
	This is a class defining a book by its author, its title and its publication year.
	"""
	
	# Constructor.
	def __init__(self, author,title, year) :
		
		# Attributes.
		self.author = author
		self.title = title
		self.year = year
	
	# Methods.
	def __str__(self) :
		info = "%s (%s) - %s" % (self.author, self.year, self.title)
		
		return info

# List of potential messages.
welcome = """
=========================================
Welcome to your personal library manager.
========================================= """
	
home = """
What would you like to do?
Choose one of the following options :
"""

main_options = """
1) Find a book.
2) Add a book.
3) Modify/remove a book.
4) See all books.
5) Quit.
"""

find_options = """
Find a book :
1) by title.
2) by author.
3) by date.
4) All of the above.
5) Return to main menu.
"""
empty = """
ERROR : Your library is currently empty.
"""
	
added = """
You added the following book : 
"""

list_pres = """
This is all the book(s) contained 
in your personal library :
"""
	
goodbye = """
=========================================
		Goodbye!
=========================================
"""
	
error = """
ERROR : This choice is not in the options list.
"""

# Functions for options.
# Find a book.
def find_book(books_list) :

	if len(books_list) == 0 :
			
		print(empty)
			
	else : 
	
		print(find_options)
		find_choice = eval(input("Your choice : "))
	
		if find_choice == 1 :
				
			find = input("Author : ")
			
		elif find_choice == 2 :
	
			print("2")
				
		elif find_choice == 5 :
		
			return
					
		else : 
				
			print(error)
			
# Add a book.
def add_book(books_list) :

			temp_author = input("Author : ")
			temp_title = input("Title : ")
			temp_year = input("Publication year : ")
			
			new_book = Book(temp_author, temp_title, temp_year)
			books_list.append(new_book)
			
			print(added)
			
			print(new_book)
			
# See all books.
def see_books :

	if len(books_list) == 0 :
		
		print(empty)
			
	else : 
			
		print(list_pres)
		
		for book in books_list :
				
			print(book)


# Main program.
def main() :
	
	# Add importation of an existing list.
	books_list = []

	
	print(welcome)
	
	end = False
	
	while end == False :
	
		print(home)
		print(main_options)
	
		choice = eval(input("Your choice : "))
	
		# 1) Find a book.
		if choice == 1 :
		
			find_book(books_list)

	
		# 2) Add a book.
		elif choice == 2 :
		
			add_book(books_list)
		
		# 3) Modify/remove a book.
		elif choice == 3 :
		
			print("Work in progress.")
			
		# 4) See al books.
		elif choice == 4 :
		
			see_books(books_list)
		
		# 5) Quit.
		elif choice == 5 :
		
			print(goodbye)
			
			# Add choice to save or not modification.
		
			end = True
			
		# Other inputs.
		else :
		
			print(error)	
	
if __name__ == "__main__" :
	main()
	
	
	
	
	