
class AdjList:
	
	# attributes of node in linked list - data and next
	def __init__(self,data):
		self.vertex = data
		self.next = None


class Graph:

	# initialise with graph = empty array equal to vertex number
	def __init__(self,V):
		self.V = V
		self.graph = [None] * self.V
		#print(self.graph) ==> [None, None, None, None, None]


	def add_edge(self,src,dest):
		#Add edge from source to dest and from dest to source also since it is an undirected graph

		node = AdjList(src)
		node.next = self.graph[dest]
		self.graph[dest] = node

		node = AdjList(dest)
		node.next = self.graph[src]
		self.graph[src] = node

		print("edge added ",src,"->",dest)

	def printGraph(self):
		for i in range(self.V):
			print("adj list for vertext - ",i)
			temp = self.graph[i] #object - <__main__.AdjList object at 0x107e42f28>
			while temp:
				print(temp.vertex,"->",end="")
				temp=temp.next
			print("")

if __name__ == '__main__':
	V = 5
	graph = Graph(V)
	graph.add_edge(0,1)
	graph.add_edge(0,4)
	graph.add_edge(1,4)
	graph.add_edge(4,3)
	graph.add_edge(1,3)
	graph.add_edge(2,3)
	graph.add_edge(1,2)
	graph.printGraph()

'''
O/P ---
edge added  0 -> 1
edge added  0 -> 4
edge added  1 -> 4
edge added  4 -> 3
edge added  1 -> 3
edge added  2 -> 3
edge added  1 -> 2
adj list for vertext -  0
4 ->1 ->
adj list for vertext -  1
2 ->3 ->4 ->0 ->
adj list for vertext -  2
1 ->3 ->
adj list for vertext -  3
2 ->1 ->4 ->
adj list for vertext -  4
3 ->1 ->0 ->
'''

