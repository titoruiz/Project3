from RequestAPI import Display
from graphClass import Graph
from mapScraper import Map
import time

# initializes the display window and calls it
display = Display()
display.callDisplay()

# once input is gathered, it is returned
data = display.getSeachData()
# makes the request to get search options for the input data
display.getOptions(data)
display.chooseStartOptions()

# gets the titles for API requests
titlesForRequest = display.getTitles()

G = Graph();

it = time.time()
# do graph implementation
myList = titlesForRequest[0]
for i in range(2):
    print("i = ", i)
    myList = G.populateGraph(myList)

myList = G.populateGraph(myList)
ft = time.time()

print("Edge between umbrella and rain exists: ", G.detectEdge("Umbrella", "Rain"))
print("Edge between rain and terrain exists: ", G.detectEdge("Rain", "Terrain"))

G.Dijkstras(self, "Umbrella", "Rain", "Terrain")
G.draw()

mt = time.time()
# do map implementation
myMap = Map(titlesForRequest)
myMap.create_map
mf = time.time()

# time for how long each implementation takes
gt = ft - it
mt = mf - mt

if gt >= mt:
    print("Map implementation is more effective at finding shortest path.")
else:
    print("Graph implementation is more effective at finding shortest path.")

