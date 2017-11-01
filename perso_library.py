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
	This class defines a book by its author, its title and its publication year.
	"""
	
	# Constructor.
	def __init__(self, author,title, year) :
		
		# Attributes.
		self.author = author
		self.title = title
		self.year = year
	
	# Methods.
	def get_author(self) :
	
		return self.author
		
	def get_title(self) :
	
		return self.title
		
	def get_year(self) :
	
			return self.year
		
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
1) by author.
2) by title.
3) by year.
4) All of the above.
5) Return to main menu.
"""
empty = """
ERROR : Your library is currently empty.
"""
	
added = """
You added the following book : 
"""

no_match = """
There are no results that match your search.
"""

mod_options = """
1) Modify the book.
2) Remove the book.
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
ERROR : This choice is not one of available options.
"""

# Functions for main program.
#import books_list.
def import_books() :
	"""
	This function import existing books list or create one if none is found.
	"""
	
	if os.path.isfile("books_list.pickle") and os.path.getsize("books_list.pickle") > 0 :
	
		books_list_in = open("books_list.pickle", "rb")
		books_list = pickle.load(books_list_in)
		books_list_in.close()

	else :
	
		books_list = [] 
		
	return books_list
		 

# Find a book.
def find_book(books_list) :
	"""
	This function searchs book(s) in books list.
	"""

	if len(books_list) == 0 :
			
		print(empty)
			
	else : 
		
		books_select = []
		
		exit = 0
		
		while exit == 0 :
			
			print(find_options)
			find_choice = eval(input("Your choice : "))
	
			if find_choice == 1 :
				
				find = input("Author : ")
				
				round = 1
				
				for book in books_list :
				
					if find in book.get_author() :
						
						books_select.append(book)
						print(round, ") ", book, sep = "")
						round += 1

				if len(books_select) == 0 :
				
					print(no_match)
											
				exit = 1
				
			elif find_choice == 2 :
	
				find = input("Title : ")
				
				round = 1
				
				for book in books_list :
				
					if find in book.get_title() :
						
						books_select.append(book)
						print(round, ") ", book, sep = "")
						round += 1

				if len(books_select) == 0 :
				
					print(no_match)
											
				exit = 1
				
			elif find_choice == 3 :
			
				find = input("Publication year : ")
				
				round = 1
				
				for book in books_list :
				
					if find in book.get_year() :
					
						books_select.append(book)
						print(round, ") ", book, sep = "")
						round += 1
						
				if len(books_select) == 0 :
				
					print(no_match)
									
				exit = 1	
					
			elif find_choice == 4 :
			
				find = input("Search : ")
				
				round = 1
				
				for book in books_list :
					
					temp = book.__str__()
					
					if find in temp :
						
						books_select.append(book)
						print(round, ") ", book, sep = "")
						round += 1
				
				if len(books_select) == 0 :
				
					print(no_match)
					
				exit = 1
				
			elif find_choice == 5 :
		
				exit = 1
					
			else : 
				
				print(error)
		
		return books_select
			
# Add a book.
def add_book(books_list) :
	"""
	THis function adds a book to books list.
	"""

	temp_author = input("Author : ")
	temp_title = input("Title : ")
	temp_year = input("Publication year : ")
			
	new_book = Book(temp_author, temp_title, temp_year)
	
	return new_book

# Modify/remove a book
def mod_book(books_list) :
	"""
	This function modify/remove a book in books list.
	"""

	if len(books_list) == 0 :
			
		print(empty)
			
	else : 
		
		books_to_mod = find_book(books_list)
		
		if len(books_to_mod) == 0 :
		
			pass
			
		else :
		
			if len(books_to_mod) == 1 :
		
				print("What would your like to do with this book?")
				print(mod_options)
				mod_choice = eval(input("Your choice : "))
				
			if mod_choice == 1 :
					
				print("Add new informations :")
				rep_book = add_book(books_list)
				
				round = 0	
				for book in books_list :
						
					if book.__str__() == books_to_mod[0].__str__() :
						books_list[round] = books_to_mod[0]
						round += 1
				
				for book in books_list :
				
					print(book)
					
			else :
			
				print("Which of the previous book would you like to modify/remove?")
			
				mod_choice = input("Your choice : ")
		
# See all books.
def see_books(books_list) :
	"""
	This function displays all books contained in books list.
	"""

	if len(books_list) == 0 :
		
		print(empty)
			
	else : 
			
		print(list_pres)
		
		for book in books_list :
				
			print(book)

# Save books list.
def save_books(books_list) :
	"""
	This function saves modification to books list.
	"""
	
	exit = 0
	
	while exit is 0:
	
		print(save)
		save_choice = eval(input("Your choice : "))
		
		if save_choice == 1 :
			
			books_list_out = open("books_list.pickle", "wb")
			pickle.dump(books_list, books_list_out)
			books_list_out.close()
			
			print("Modifications saved.")
			
			exit = 1
			
		elif save_choice == 2 :
			
			exit = 1
		
		else :
	
			print(error)
	
	print(goodbye)

# Main program.
def main() :
	"""
	This function is the main program of the personal library manager.
	"""
	
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
		
			new_book = add_book(books_list)
			
			books_list.append(new_book)
			print(added)
			print(new_book)
		
		# 3) Modify/remove a book.
		elif choice == 3 :
		
			# Add option empty books list.
			mod_book(books_list)
			
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
	
	
	
	
	