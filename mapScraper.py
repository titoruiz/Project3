import requests
from collections import deque
import time
page_links = dict()
link_parents = dict()
origin = ""
destination_1 = ""
destination_2 = ""
distance_1 = 0
distance_2 = 0
dest1_found = False
dest2_found = False
#request and parses links on given page
def get_all_links(title):
    s = requests.Session()
    #request format
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
    "action": "query",
    "format": "json",
    "titles": title,
    "prop": "links"
    }
    response = s.get(url=URL, params=PARAMS)
    data = response.json()
    pages = data["query"]["pages"]
    page_titles = []
    #collect links into page_titles
    for key, val in pages.items():
        if "pageid" in val:
            for link in val["links"]:
                page_titles.append(link.get("title"))
    return page_titles

#checks if either destination has been reached
def check_for_destination():
    if page_links.get(destination_1) is not None:
        global dest1_found
        dest1_found = True
        global distance_1
        distance_1 = page_links.get(destination_1)
    if destination_2 in page_links:
        global dest2_found
        dest2_found = True
        global distance_2
        distance_2 = page_links.get(destination_2)
#recursive function to fill map with adjacent links
def scraper(site, count):
    queue = deque()
    gotlinks = get_all_links(site)
    for l in gotlinks:
        queue.append([l, site, count])
    while queue:
        check_for_destination()
        if ((not dest1_found) or (not dest2_found)) and (count < 20):
            temp, base, dist = queue.popleft()
            if temp in page_links and (dist > page_links.get(temp)):
                continue
            elif temp in page_links and (dist < page_links.get(temp)):
                page_links[temp] = dist
                link_parents[temp] = base
            page_links[temp] = dist
            link_parents[temp] = base
            gotlinks = get_all_links(temp)
            for i in gotlinks:
                queue.append([i, temp, dist+1])
        else:
            break
def output_format():
    global origin
    if (dest1_found and dest2_found):
        print("Destination articles found!")
        print("Path to", destination_1 + ":")
        stack = deque()
        current_entry = destination_1
        while not current_entry == origin:
            stack.append(link_parents.get(current_entry))
            current_entry = link_parents.get(current_entry)
        while stack:
            print(stack.pop())
        print(destination_1)
        print("Distance from origin:", distance_1, "\n")
        print("Path to", destination_2 + ":")
        current_entry = destination_2
        while not current_entry == origin:
            stack.append(link_parents.get(current_entry))
            current_entry = link_parents.get(current_entry)
        while stack:
            print(stack.pop())
        print(destination_2)
        print("Distance from origin:", distance_2, "\n")
        if (distance_1 < distance_2):
            print(destination_1, "is closer to", origin, "than", destination_2)
            print("It is", distance_1, "connections away from", origin )
        elif (distance_2 < distance_1):
            print(destination_2, "is closer to", origin, "than", destination_1)
            print("It is", distance_2, "connections away from", origin )
        elif (distance_1 == distance_2):
            print(destination_1, "and", destination_2, "are the same amount of connections away from", origin)
    if dest1_found and (not dest2_found):
        print("Only destination article 1 found!")
        print("Path to", destination_1 + ":")
        stack = deque()
        current_entry = destination_1
        while not current_entry == origin:
            stack.append(link_parents.get(current_entry))
            current_entry = link_parents.get(current_entry)
        print(current_entry)
        while stack.empty:
            print(stack.pop())
        print("Distance from origin:", distance_1, "\n")
    if dest2_found and (not dest1_found):
        print("Only destination article 2 found!")
        print("Path to", destination_2 + ":")
        stack = deque()
        current_entry = destination_2
        while not current_entry == origin:
            stack.append(link_parents.get(current_entry))
            current_entry = link_parents.get(current_entry)
        print(current_entry)
        while stack:
            print(stack.pop())
        print("Distance from origin:", distance_2, "\n")
    if (not dest2_found) and (not dest1_found):
        print("Unable to find destination articles.")
def insert_function():
    origin = array[0]
    destination_1 = array[1]
    destination_2 = array[2]
    page_links[origin] = 0
    link_parents[origin] = None
    counter = 1
    #call function to scrape page for valid urls
    scraper(origin, counter)
    output_format()
start_time = time.time()
insert_function()
print("--- %s seconds ---" % (time.time() - start_time))
