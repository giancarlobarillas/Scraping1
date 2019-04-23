from tkinter import *

from reddit_scrape import *

from twitter_scrape import *

fields = ('Consumer Key:','Consumer secret:','Access token:','Latitude:','Longitude:','Radius:')


def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

def Reddit_GUI():

    for widget in toolbar2.winfo_children():
        widget.destroy()
        
    l1 = Label(toolbar2, text = "Subreddit you wish to scrape: ")

    l1.pack()

    e1 = Entry(toolbar2)

    e1.pack(side=TOP, fill=X, padx=5, pady=5)

    btn1 = Button(toolbar2, text = "Submit", width = 16, command = lambda:  Reddit_Scrape(e1.get()))

    btn1.pack(side = TOP, padx = 10, pady = 10)

    toolbar2.pack(fill = X, expand = True)
    
def Twitter_GUI():

    for widget in toolbar2.winfo_children():
        widget.destroy()

    ents = makeform(toolbar2, fields)

    toolbar2.bind('<Return>', (lambda event, e=ents: fetch(e)))

    btn1 = Button(toolbar2, text = "Submit", width = 16, command = Twitter_Scrape)

    btn1.pack(side = TOP, padx = 10, pady = 10)
    
    toolbar2.pack(fill = X, expand = True)

window = Tk()

toolbar2 = Frame(window)
 
window.title("Scraping tool")

toolbar = Frame(window)

btn1 = Button(toolbar, text="Reddit", width = 16, command = Reddit_GUI)

btn1.pack(side = LEFT, padx = 10, pady = 10)

btn2 = Button(toolbar, text="Twitter", width = 16, command = Twitter_GUI)

btn2.pack(side = LEFT, padx = 10, pady = 10)

toolbar.pack(side = TOP, fill = X)

window.mainloop()


