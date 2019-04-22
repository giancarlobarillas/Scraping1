from tkinter import *

from twitter_scrape import *

from reddit_scrape import *

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

    for widget in reddit_toolbar.winfo_children():
        widget.destroy()
        
    for widget in twitter_toolbar.winfo_children():
        widget.destroy()

    reddit_toolbar.update()

    l1 = Label(reddit_toolbar, text = "Subreddit you wish to scrape: ")

    l1.pack()

    e1 = Entry(reddit_toolbar)

    e1.pack(side=TOP, fill=X, padx=5, pady=5)

    btn1 = Button(reddit_toolbar, text = "Submit", width = 16, command = Reddit_Scrape)

    btn1.pack(side = TOP, padx = 10, pady = 10)

    reddit_toolbar.pack(fill = X, expand = True)
    
def Twitter_GUI():

    for widget in reddit_toolbar.winfo_children():
        widget.destroy()
        
    for widget in twitter_toolbar.winfo_children():
        widget.destroy()

    twitter_toolbar.update()

    ents = makeform(twitter_toolbar, fields)

    twitter_toolbar.bind('<Return>', (lambda event, e=ents: fetch(e)))

    btn1 = Button(twitter_toolbar, text = "Submit", width = 16, command = Twitter_Scrape)

    btn1.pack(side = TOP, padx = 10, pady = 10)
    
    twitter_toolbar.pack(fill = X, expand = True)

window = Tk()
 
window.title("Scraping tool")

toolbar = Frame(window)

reddit_toolbar = Frame(window)

twitter_toolbar = Frame(window)

btn1 = Button(toolbar, text="Reddit", width = 16, command = Reddit_GUI)

btn1.pack(side = LEFT, padx = 10, pady = 10)

btn2 = Button(toolbar, text="Twitter", width = 16, command = Twitter_GUI)

btn2.pack(side = LEFT, padx = 10, pady = 10)

toolbar.pack(side = TOP, fill = X)

window.mainloop()


