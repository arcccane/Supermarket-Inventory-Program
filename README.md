# Supermarket-Inventory-Program

1.	DSA Assignment  (Individual – 35%)

There are 4 components (see a to d below) to this assignment: 

a.	Part 1 - Stock Inventory – Basic features (5%)
b.	Part 1 - Stock Inventory – Search and Sort Algorithms (10%)
c.	Part 2 - Challenge Question on Algorithm (10%)
d.	Part 1 and 2 – Technical Review (10%)

Part 1 is related to the development of a Stock Inventory application
Part 2 is a challenge question on algorithm.

Part 1: Stock Inventory Application

The purpose of the Stock Inventory application is to allow the user of the application to manage the stock of a fruits store. The application will allow the user to display, add, update and remove stock items from the inventory, perform searching and sorting of stock items, and other additional features that improve the usefulness of the application for the user.

Stock Inventory – Basic features (5%)

a.	Design a suitable data structure (e.g. by making use of Python list, dictionary, objects, etc.) to manage the stock items in the fruits store. You are required to store the following stock item information: item index,  description, item selling price, item stock level and at least TWO OTHER item information of your choice. Each item will have the above attributes. The fruits store will store up to 20 different types of item.

b.	Design a menu for the application to allow the user to perform the following:
	Add items into the stock inventory
	Update selected item
	Remove items from the stock inventory
	Display items in the stock inventory
	Sort items
	Search item
	Exit Application

c.	Complete the (Add, Update, Remove and Display) operations for the inventory application


Stock Inventory – Search and Sort Algorithms (10%)
Add the following features to the stock inventory application.


d.	Complete the Sort item option. Student must implement 3 sorting algorithms. They are Bubble, Selection and Insertion Sort algorithms to sort the items in your stock inventory based on a sort key e.g. item selling price, item stock level, etc. Student can decide on which sort key to apply.

e.	Complete the Search item option. Student will apply 2 search algorithms. They are Linear and Binary Search algorithm to search for an item based on a search key. Student will decide which search key but must implement both search algorithms.

f.	Student may add in bonus features such as exception handling, advanced algorithms etc

(NOTE: You would need to apply knowledge from the practical sessions to complete these functions) 
Part 2:  Challenge Question on Algorithm (10%)

This challenge question will test you on the design and implementation of an efficient algorithm to solve the following problem.

Given the following:
i.	A sequence of positive integers, SEQ,  sorted in strictly increasing order (i.e. all the integers are distinct), and
ii.	a positive integer Z

Design and implement an algorithm with Python to check all pairs of integers X and Y in the sorted sequence such that X + Y = Z.

(NOTE: A brute-force algorithm that compares all possible pairs in the sorted sequence and check if they sum up to equal to Z will work. However, using this approach will only give you a minimal score.)

For example, if SEQ and Z are provided to your program as follow:

SEQ:
2	3	5	7	8	10	15	16	23	28

Z: 21

Then, your Python program should return:
•	X = 5
•	Y = 16
•	TRUE (since 5 + 16 = 21)


However, if SEQ and Z are provided to your program as follow:

SEQ:
2	3	5	7	8	10	15	16	23	28

Z: 3

Then, your Python program should return:
•	X = not found
•	Y = not found
•	FALSE (since there does not exist two integers X and Y in SEQ, where  sum of X and Y = Z)
