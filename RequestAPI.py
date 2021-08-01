import tkinter
import requests
from tkinter import *
from tkinter import messagebox


class Display:
    def __init__(self):
        self.root = Tk()
        self.searchData = []
        self.titles = []
        self.search = []
        self.target1 = []
        self.target2 = []

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
                self.root.quit()
                self.root.withdraw()

        #display settings for the window
        self.root.title("Search Page Titles")
        self.root.geometry("800x400")
        self.root['background']='#3d4849'

        ins = Label(self.root, text="For each field, enter a page title. The pages will be searched for in the API. Then you will be prompted to select the exact pages.", fg='#ffffff')
        ins['background']='#3d4849'
        ins.pack(pady=20)

        startLabel = Label(self.root, text="Search Title For Start Page", fg='#ffffff')
        startLabel['background']='#3d4849'
        startLabel.pack()
    
        s = Entry(self.root, width=50)
        s.pack()

        dest1Label = Label(self.root, text="Search Title For First Target Page", fg='#ffffff')
        dest1Label['background']='#3d4849'
        dest1Label.pack()

        fd = Entry(self.root, width=50)
        fd.pack()

        dest2Label = Label(self.root, text="Search Title For Second Target Page", fg='#ffffff')
        dest2Label['background']='#3d4849'
        dest2Label.pack()

        sd = Entry(self.root, width=50)
        sd.pack()

        button = Button(self.root, text="Submit To Search", command=getSearchResults)
        button['background']='#6699cc'
        button.pack(pady=15)

        self.root.mainloop()

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
    
    # 
    def getOptions(self, data):
        url = "http://en.wikipedia.org/w/api.php?action=query&list=search&format=json&srsearch=";
        searchUrl = url + data[0]
        dest1Url = url + data[1]
        dest2Url = url + data[2]

        # gets the responses from all the search results
        res = requests.get(searchUrl);
        map = res.json()
        self.search = self.getResultList(map);

        res2 = requests.get(dest1Url);
        map2 = res2.json()
        self.target1 = self.getResultList(map2);

        res3 = requests.get(dest2Url);
        map3 = res3.json()
        self.target2 = self.getResultList(map3);


    # function for user to choose options when they have searched for it
    def chooseStartOptions(self):

        def selected():
            # inserts the selected choices to the titles array
            self.titles.insert(0, choice.get())
            self.titles.insert(1, choice1.get())
            self.titles.insert(2, choice2.get())

            # quits once titles are in array
            top.quit()


        # initializes options window
        top = Toplevel();
        top.title("Select Titles")
        top.geometry("800x400")
        top['background']='#3d4849'

        choose = Label(top, text="Select The Title Of The Start Page:", fg='#ffffff')
        choose['background']='#3d4849'
        choose.pack()

        lab = Label(top, text="If none are selected then the first options in each list will be chosen.", fg='#ffffff')
        lab['background']='#3d4849'
        lab.pack()

        # initializes the choices for OptionMenu's
        choice = StringVar()
        choice.set(self.search[0])
        choice1 = StringVar()
        choice1.set(self.target1[0])
        choice2 = StringVar()
        choice2.set(self.target2[0])

        #options menu for all the searches
        option = OptionMenu(top,choice, *self.search)
        option.config(width=40)
        #option["background"] = '#3d4849'
        option.pack(pady=20)


        option1 = OptionMenu(top,choice1, *self.target1)
        option1.config(width=40)
        option1.pack(pady=20)

        option2 = OptionMenu(top,choice2, *self.target2)
        option2.config(width=40)
        option2.pack(pady=20,)

        # button will select the choices
        button = Button(top, text="Select Titles", command=selected)
        button['background']='#6699cc'
        button.pack()

        top.mainloop()
    
    # returns the titles once they are in the array
    def getTitles(self):
        return self.titles
