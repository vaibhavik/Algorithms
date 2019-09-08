# count number of times an element exists in the list

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

	def getNodeAtLoc(self,loc):
		curr = self.head
		p = 0
		#print("prev loc",loc)
		while curr is not None and p!=loc:
			curr = curr.next
			p=p+1
		return curr

	def countOccurence(self,element):
		p = 0
		curr = self.head
		while curr is not None:
			if curr.data == element:
				p = p+1
			curr = curr.next
		print(p)

	def removeDuplicates(self):
		existing = []
		curr = self.head
		loc= 0
		#prev = self.head
		while curr is not None:
			if curr.data not in existing:
				existing.append(curr.data)
				#prev.data = curr.data
			else:
				pre_node = self.getNodeAtLoc(loc-1)
				print("delete",curr.data,"prev node = ",pre_node.data)
				pre_node.next = curr.next
				print("deleted",curr.data)
				del curr.data
				curr = pre_node
				#print(curr.data)
			curr = curr.next
			loc = loc+1
			print(existing)

	def getLength(self):
		curr = self.head
		p = 0
		while curr is not None:
			curr = curr.next
			p=p+1
		return p

	def detectLoop(self):
		curr =self.head
		s = set()
		while curr is not None:
			if curr.next in s:
				print("Loop detected")
				break
			else:
				s.add(curr.next)

	def detectPalindrome(self):
		curr = self.head
		size = int(self.getLength())
		print(size)
		for i in range(0,size//2):
			if self.getNodeAtLoc(i).data != self.getNodeAtLoc(size-i-1).data:
				return False
				break


	def appendAtList(self,data):
		new_node = Node(data)
		curr = self.head
		while curr.next:
			curr = curr.next
		curr.next = new_node

	def getPrevNode(self,element):
		curr = self.head
		while curr is not None:
			if curr.next == element:
				print(curr.data,"prev el")
				break
			curr = curr.next
		return curr

	def swapNodes(self,n1,n2):
		curr = self.head
		while curr is not None:
			if curr.data == n1:
				temp1 = curr
				pre1 = self.getPrevNode(curr)
				temp1.next = curr.next
				print(pre1.data,temp1.next.data)
			if curr.data == n2:
				temp2 = curr
				pre2 = self.getPrevNode(curr)
				temp2.next = curr.next
				print(pre2.data,temp2.next.data)
			curr = curr.next	
		pre1.next = temp2
		pre2.next = temp1
		c = temp1.next
		temp1.next = temp2.next 
		temp2.next = c

#1->2->9->4->6->3
l = LinkedList()
l.head = Node("1")
a1 = Node("2")
l.head.next = a1
l.appendAtList("9")
l.appendAtList("4")
l.appendAtList("6")
l.appendAtList("3")
#l.appendAtList("5")
#l.head.next.next.next.next = l.head; 
l.printList()
#l.countOccurence("2")
#l.removeDuplicates()
#l.detectLoop()
#if(l.detectPalindrome() == False):
#	print("Not Palindrome")
#else:
#	print("palindrome")
l.swapNodes("9","6")
l.printList()
