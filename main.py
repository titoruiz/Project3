from RequestAPI import Display
from graphClass import Graph

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

myList = titlesForRequest[0]
for i in range(2):
    print("i = ", i)
    myList = G.populateGraph(myList)

print("Edge between umbrella and rain exists: ", G.detectEdge("Umbrella", "Rain"))
print("Edge between rain and terrain exists: ", G.detectEdge("Rain", "Terrain"))
#G.shortestPath()
G.draw()
