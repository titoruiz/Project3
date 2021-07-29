import networkx as nx
import matplotlib.pyplot as plot

class Graph:
	# a dictionary and graph object
	def __init__(self):
		self.visual = []
		self.path = []
		self.path2 = []
		self.G = nx.Graph()

	# adds an edge to the dictionary
	def addEdge(self,a,b):
		temp = [a,b]
		self.visual.append(temp)
		self.G.add_edge(a,b, color='green')

	def draw(self):
		pos = nx.circular_layout(self.G)

		edges = self.G.edges()
		colors = [self.G[u][v]['color'] for u,v in edges]
		nx.draw_networkx(self.G, pos, edge_color= colors, node_color='violet', node_size=600)
		plot.show()

	# changes edge color to green to red for path
	def red(self,a,b):
		# removes the black edge and adds it back but in green
		self.G.remove_edge(a,b)
		self.G.add_edge(a,b, color='red')
	
	# gets a sublist of the path list
	def getSublist(self, begin, last, first):
		list = []
		curr = begin
		# iterates and adds all names in sublist range
		while(curr < last):
			# gets sublist of path if first is true
			if first:
				list.append(self.path[curr])
			else:
				list.append(self.path2[curr])
			curr += 1
		return list

	# shows the path for path
	def showPath(self, first, length):
		list1 = self.getSublist(0, length - 1, first)
		list2 = self.getSublist(1, length, first)

		# changes edges to green
		for i in range(length - 1):
			self.red(list1[i], list2[i])

	# compares for shortest path and displays path
	def compare(self):
		length = len(self.path)
		length2 = len(self.path2)

		# will show the path for shortest path
		if length2 < length:
			plot.title(label='{n} is Shortest Path'.format(n=self.path2[length2 -1]))
			self.showPath(False, length2)
		# will show both paths
		elif length == length2:
			plot.title(label='Equal Paths')
			self.showPath(True, length)
			self.showPath(False, length2)
		else:
			plot.title(label='{n} is Shortest Path'.format(n=self.path[length -1]))
			self.showPath(True, length)

	# call for Dijkstras algorithm
	def Dijkstras(self, start, target1, target2):
		self.path = nx.shortest_path(self.G, source=start, target=target1, weight=None)
		self.path2 = nx.shortest_path(self.G, source=start, target=target2, weight=None)
		self.compare()

	# add start and target
	def shortestPath(self):
		visited = []
		value = 1
		#visited["Elon"] = str(value)
		print(visited)
	# this function will do a BFS type for unweighted graphs
	# will have vsited array with length array as well and queuu


	#red will be used to change the edge color for 

G = Graph()
G.addEdge("Tim", "Elon")
G.addEdge("Russ", "Elon")
G.addEdge("Russ", "Mike")
G.addEdge("H", "Mike")
G.addEdge("Mike", "T")
G.addEdge("Russ", "Tim")

G.addEdge("T", "E")
G.addEdge("Russ", "E")
G.addEdge("Russ", "M")
G.addEdge("H", "Me")
G.addEdge("M", "T")
G.addEdge("R", "Tim")


#check D's algo
G.Dijkstras("Elon", "Mike", "T")
#G.shortestPath()
G.draw()