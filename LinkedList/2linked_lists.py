#2 linked list operations
class Node:

	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	def printList(self):
		curr = self.head
		while curr is not None:
			print(curr.data,end = "->")
			curr = curr.next
		print()

	def appendAtList(self,data):
		new_node = Node(data)
		curr = self.head
		while curr.next:
			curr = curr.next
		curr.next = new_node

	def intersectionList(self,l2)
		


l1 = LinkedList()
l1.head = Node("1")
a1 = Node("2")
l1.head.next = a1
l1.appendAtList("3")
l1.appendAtList("4")
l1.appendAtList("6")
l2 =LinkedList()
l2.head = Node("2")
b1 = Node("4")
l2.head.next = b1
l2.appendAtList("6")
l2.appendAtList("8")
l1.printList()
l2.printList()