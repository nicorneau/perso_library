"""
perso_library.py
This is a program to keep track of a personal library.
@author : Nicolas Corneau-Tremblay
@sdate : 27/10/17
"""

import os
import pickle

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

save = """
Would you like to save your modification(s)?
1) Yes.
2) No.
"""

goodbye = """
=========================================
		Goodbye!
=========================================
"""
	
error = """
ERROR : This choice is not in the options list.
"""

# Functions for main program.
#import books_list.
def import_books() :
	
	if os.path.isfile("books_list.pickle") and os.path.getsize("books_list.pickle") > 0 :
	
		books_list_in = open("books_list.pickle", "rb")
		books_list = pickle.load(books_list_in)
		books_list_in.close()

	else :
	
		books_list = [] 
		
	return books_list
		 

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
def see_books(books_list) :

	if len(books_list) == 0 :
		
		print(empty)
			
	else : 
			
		print(list_pres)
		
		for book in books_list :
				
			print(book)

# Save books list.
def save_books(books_list) :
	
	exit = 0
	
	while exit is 0:
	
		print(save)
		save_choice = input("Your choice : ")
		
		if save_choice is "1" :
			
			books_list_out = open("books_list.pickle", "wb")
			pickle.dump(books_list, books_list_out)
			books_list_out.close()
			
			print("Modifications saved.")
			
			exit = 1
			
		elif save_choice is "2" :
			
			exit = 1
		
		else :
	
			print(error)
	
	print(goodbye)

# Main program.
def main() :
	
	# Import an existing list or create an empty one if none is found.
	books_list = import_books()
	
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
			# Add option empty books list.
			
		# 4) See al books.
		elif choice == 4 :
		
			see_books(books_list)
		
		# 5) Quit.
		elif choice == 5 :
			
			save_books(books_list)
			
			end = True
			
		# Other inputs.
		else :
		
			print(error)	
	
# Run main program.
if __name__ == "__main__" :
	main()
	
	
	
	
	