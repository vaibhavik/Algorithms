#linked list deletion

class Node:

	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	def getNodeAtLoc(self,loc):
		p = 0
		curr = self.head
		while curr is not None and p!=loc:
			curr = curr.next
			p = p+1
		return curr

	def printList(self):
		printval = self.head
		while printval is not None:
			print (printval.data, end = "->")
			printval = printval.next	
		print()

	def delFromStart(self):
		curr = self.head
		self.head = curr.next
		curr.next = None	

	def delFromPosition(self,loc):
		prev_node = self.getNodeAtLoc(loc-2)
		prev_node.next = prev_node.next.next

	def deleteLinkedList(self):
		 curr = self.head
		 while curr:
		 	prev = curr.next
		 	del curr.data
		 	curr = prev
		 print("linked list deleted")

	def reverseLinkedlist(self):
		prev = None
		curr = self.head
		#nextNode = self.head.next
		while(curr):
			nextNode = curr.next
			curr.next = prev
			prev = curr
			curr = nextNode
		
		self.head = prev



l1 = LinkedList()
l1.head = Node("1")
a1 = Node("2")
l1.head.next = a1
a2 = Node("3")
a1.next = a2
l1.printList()
l1.reverseLinkedlist()
l1.printList()
#l1.delFromPosition(2)
#l1.delFromStart()
#l1.deleteLinkedList()
#l1.printList()


