# Linked list insertion

class Node:

	def __init__(self,data):
		self.data = data
		self.next = None

	def getNextNode(self):
		return self.next	

class LinkedList:

	def __init__(self):
		self.head = None

	def getPrevNode(self,i):
		p = 0
		curr = self.head
		while curr is not None and p!=i:
			curr = curr.next 
			p= p+1
		if p == i:
			return curr	

	def getLinkedlistSize(self):
		s = 0
		curr = self.head
		while curr is not None:
			curr = curr.next
			s = s+1
		return s

	def atBeginning(self,new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def atIndex(self,new_data,index):
		new_node = Node(new_data)
		prev_node = self.getPrevNode(index-1)
		new_node.next = prev_node.next
		prev_node.next = new_node

	def atEnd(self,new_data):
		new_node = Node(new_data)
		size = self.getLinkedlistSize()
		prev_node = self.getPrevNode(size-1)
		prev_node.next = new_node
		new_node.next = None

	def printList(self):
		printval = self.head
		while printval is not None:
			print (printval.data, end = "->")
			printval = printval.next


l = LinkedList()
l.head = Node("1")
n1 = Node("2")
n2 = Node("3")
l.head.next = n1
n1.next = n2
l.atBeginning("0")
l.printList()
print()
l.atIndex(4,2)
l.printList()
print()
l.atEnd(5)
l.printList()
print()

'''


list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list.headval.nextval = e2
e2.nextval = e3

list.AtBegining("Sun")

list.listprint()
'''