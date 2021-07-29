
from RequestAPI import Display



# initializes the display window and calls it
display = Display()
display.callDisplay()

# once input is gathered, it is returned
data = display.getSeachData()
# makes the request to get search options for the input data
display.chooseOptions(data)