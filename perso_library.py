"""
Name : perso_library.py
Description : This is a program to keep track of a personal library.
Author : Nicolas Corneau-Tremblay
Date : 27/10/17
"""

import os
import pickle

# Book class
class Book(object):
	"""
	This class defines a book by its author, its title and its publication year.
	"""
	
	# Constructor
	def __init__(self, author,title, year) :
		
		# Attributes
		self.author = author
		self.title = title
		self.year = year
	
	# Methods
	def get_author(self) :
	
		return self.author
		
	def get_title(self) :
	
		return self.title
		
	def get_year(self) :
	
			return self.year
		
	def __str__(self) :
		info = "%s (%s) - %s" % (self.author, self.year, self.title)
		
		return info

# List of potential messages
welcome = """
=========================================
Welcome to your personal library manager.
========================================= """
	
home = """
What would you like to do?
Select one of the following
options by entering the number
corresponding to your choice :
"""

main_options = """
1) Find a book
2) Add a book
3) Modify/remove a book
4) See all books
5) Clear personal library
6) Quit
"""

search = """
Enter book author, title and/or publication date.
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
1) Modify the book
2) Remove the book
3) Return to main menu
"""

del_options = """
Are you sure you want to clear your personal library?
1) Yes
2) No
"""

list_pres = """
This is all the book(s) contained 
in your personal library :
"""

save = """
Would you like to save your modification(s)?
1) Yes
2) No
"""

goodbye = """
=========================================
		Goodbye!
=========================================
"""
	
error = """
ERROR : This choice is not one of available options.
"""

# Functions for main program
# Import books_list
def import_books() :
	"""
	This function import existing books list or create one if none is found.
	"""
	
	if os.path.isfile("books_list.pickle") \
	and os.path.getsize("books_list.pickle") > 0 :
	
		books_list_in = open("books_list.pickle", "rb")
		books_list = pickle.load(books_list_in)
		books_list_in.close()

	else :
	
		books_list = [] 
		
	return books_list
		 

# Find a book
def find_book(books_list) :
	"""
	This function searchs book(s) in books list.
	"""

	# Empty books list
	if len(books_list) == 0 :
			
		print(empty)
	
	# Non-empty books list
	else : 
		
		books_select = []
		
		print(search)
		find = input("Search for : ")
				
		for i, book in enumerate(books_list) :
					
			temp = book.__str__()
					
			if find in temp :
						
				books_select.append(book)
				print(i + 1, ") ", book, sep = "")
				
		if len(books_select) == 0 :
				
			print(no_match)
			
		return books_select


# Add a book
def add_book(books_list) :
	"""
	This function adds a book to books list.
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
		
		# Empty books list to modify
		if len(books_to_mod) == 0 :
		
			pass
		
		#Non-empty books list to modify
		else :
			
			# Books list to modify of length equals to one
			if len(books_to_mod) == 1 :
		
				print("What would your like to do with this book?")
				print(mod_options)
				mod_choice = eval(input("Your choice : "))
				
				# Modify
				if mod_choice == 1 :
					
					print("Add new informations :")
					rep_book = add_book(books_list)
				
					for i, book in enumerate(books_list) :
						
						if book.__str__() == books_to_mod[0].__str__() :
						
							books_list[i] = rep_book
						
					print("The book has been correctly modified.")
				
				# Delete
				elif mod_choice == 2 :
					
					for i, book in enumerate(books_list) :
						
						if book.__str__() == books_to_mod[0].__str__() :
						
							del books_list[i]
							
					print("The book has been correctly deleted.")
					
				elif mod_choice == 3 :
				
					pass
				
				# Error
				else :
					
					print(error)
			
			# Books list to modify of length greater to one
			else :
			
				print("Which of the previous book would you like to modify/remove?")
			
				mod_choice = input("Your choice : ")
			
		return books_list
		
# See all books
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


# Clear personal library
def clear_books(books_list) :
	"""
	This function clear the personal library
	"""
	print(del_options)
	del_choice = input("Your choice : ")
	
	if del_choice == "1" :
	
		books_list = []
		
		print("Your personal library is now empty.")
		
	elif del_choice == "2" :
	
		pass
		
	else :
	
		print(error)
		
	return books_list
	
	
# Save books list
def save_books(books_list) :
	"""
	This function saves modification to books list.
	"""
	
	exit = 0
	
	while exit == 0:
	
		print(save)
		save_choice = eval(input("Your choice : "))
		
		if save_choice == 1 :
			
			books_list_out = open("books_list.pickle", "wb")
			pickle.dump(books_list, books_list_out)
			books_list_out.close()
			
			print("Modification(s) saved.")
			
			exit = 1
			
		elif save_choice == 2 :
			
			exit = 1
		
		else :
	
			print(error)
	
	print(goodbye)

# Main program
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
	
		choice = input("Your choice : ")
	
		# 1) Find a book
		if choice == "1" :
		
			find_book(books_list)
	
		# 2) Add a book
		elif choice == "2" :
		
			new_book = add_book(books_list)
			
			books_list.append(new_book)
			print(added)
			print(new_book)
		
		# 3) Modify/remove a book
		elif choice == "3" :
		
			# Add option empty books list
			mod_book(books_list)
			
		# 4) See all books
		elif choice == "4" :
		
			see_books(books_list)
			
		# 5) Clear personal library
		elif choice == "5" :
		
			books_list = clear_books(books_list)
		
		# 6) Quit
		elif choice == "6" :
			
			save_books(books_list)
			
			end = True
			
		# Other inputs
		else :
		
			print(error)	
	
# Run main program
if __name__ == "__main__" :
	main()
	
	
	
	
	