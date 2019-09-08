#Search in linked list
class Node:

	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	def searchInList(self,element):
		curr = self.head
		while curr is not None:
			if curr.data == element:
				print("found",element)
				break
			else:
				curr = curr.next

	def recurrSearchInList(self,head,element):
		if head == None:
			print("Not found")
		elif head.data == element:
			print("element found",head.data)	
		else:
			self.recurrSearchInList(head.next,element)		


	def printList(self):
		printval = self.head
		while printval is not None:
			print (printval.data, end = "->")
			printval = printval.next	
		print()


l = LinkedList()
l.head = Node("1")
a1 = Node("2")
l.head.next = a1
a2 = Node("3")
a1.next = a2
l.printList()
#l.searchInList("2")
l.recurrSearchInList(l.head,"2")