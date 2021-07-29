import requests
from tkinter import *
from tkinter import messagebox

class Display:
    def __init__(self):
       self.searchData = []
       self.titles = []
       self.searchOptions = []
       self.dest1Options = []
       self.dest2Options = []

    # returns the search input
    def getSeachData(self):
        return self.searchData
    
    # initial window to get data
    def callDisplay(self):
     
        # function for button to set the input
        def getSearchResults():
            start = s.get()
            dest1 = fd.get()
            dest2 =sd.get()

            # input validation to see if there is missing input
            if(start == '' or dest1 == '' or dest2 == ''):
                messagebox.showinfo("showinfo", "Input Error: One or more fields are empty.")
            else:
                self.searchData = [start, dest1, dest2]
                root.quit()


        #display settings for the window
        root = Tk();
        root.geometry("800x400")
        root['background']='#6699cc'

        ins = Label(root, text="For each field, enter a page title. The pages will be searched for in the API. Then you will be prompted to select the exact pages.")
        ins['background']='#6699cc'
        ins.pack(pady=20)

        startLabel = Label(root, text="Enter Title For Start Page")
        startLabel['background']='#6699cc'
        startLabel.pack()
    
        s = Entry(root, width=50)
        s.pack()

        dest1Label = Label(root, text="Enter Title For First Destination Page")
        dest1Label['background']='#6699cc'
        dest1Label.pack()

        fd = Entry(root, width=50)
        fd.pack()

        dest2Label = Label(root, text="Enter Title For Second Destination Page")
        dest2Label['background']='#6699cc'
        dest2Label.pack()

        sd = Entry(root, width=50)
        sd.pack()

        button = Button(root, text="Submit To Search", command=getSearchResults)
        #button.grid(row=0, column=1,padx=10,pady=10)
        button['background']='#f08080'
        button.pack(pady=15)


        root.mainloop()

    # breaks down the search query to get 10 options to choose from
    def getResultList(self, result):
        data = []
        query = result['query']
        searchRes = query['search']

        resultCount = len(searchRes)

        for x in range(resultCount):
            res = searchRes[x]
            title = res['title']
            data.insert(x,title)
        return data;
    
    def chooseOptions(self, data):
        print(data)
        url = "http://en.wikipedia.org/w/api.php?action=query&list=search&format=json&srsearch=";
        searchUrl = url + data[0]
        dest1Url = url + data[1]
        dest2Url = url + data[2]

        res = requests.get(searchUrl);
        map = res.json()
        self.searchOptions = self.getResultList(map);

        res2 = requests.get(dest1Url);
        map2 = res2.json()
        self.dest1Options = self.getResultList(map2);

        res3 = requests.get(dest2Url);
        map3 = res3.json()
        self.dest2Options = self.getResultList(map3);


        print(self.searchOptions)
        print(self.dest1Options)
        print(self.dest2Options)
