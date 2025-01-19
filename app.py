'''
Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton, PanedWindow, Radiobutton,
Scale, Scrollbar, and Spinbox. The other six are new: Combobox, Notebook, Progressbar,
Separator, Sizegrip and Treeview
'''

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


H1 = ("Arial", 35, "bold")
H2 = ("Arial", 24, "bold")
H3 = ("Arial", 18, "bold")
BODY = ("Arial", 18)

def toSearch(event):
    app.show_frame(Page1)

def toCreate(event):
    app.show_frame(Page2)

class TkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry("400x600")
        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# START PAGE
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Recipe Book", font=H1)
        label.pack(pady=(20,155))

        label = ttk.Label(self, text="What would you like help with?", font=H3)
        label.pack(pady=(0, 20))
        bigFrame = tk.Frame(self)

        # Search
        searchFrame = tk.Frame(bigFrame)

        image = Image.open("icons/search.png").convert("RGBA").resize((55, 55))
        photo = ImageTk.PhotoImage(image)

        # Create the button with the icon
        searchImage = tk.Label(searchFrame, image=photo)
        searchImage.image = photo
        searchImage.pack(pady=(12, 0))

        searchLabel = tk.Label(searchFrame, text="Find recipe", font=BODY)
        searchLabel.pack(padx=7, pady=(10, 12))

        searchFrame.pack(side='left', padx=(0, 15))

        searchFrame.bind("<Button-1>", toSearch)
        searchLabel.bind("<Button-1>", toSearch)
        searchImage.bind("<Button-1>", toSearch)

        # Create

        createFrame = tk.Frame(bigFrame)

        image = Image.open("icons/create.png").convert("RGBA").resize((55, 55))
        photo = ImageTk.PhotoImage(image)

        # Create the button with the icon
        createImage = tk.Label(createFrame, image=photo)
        createImage.image = photo
        createImage.pack(pady=(12, 0))

        createLabel = tk.Label(createFrame, text="Create recipe", font=BODY)
        createLabel.pack(padx=7, pady=(10, 12))

        createFrame.pack()

        createFrame.bind("<Button-1>", toCreate)
        createLabel.bind("<Button-1>", toCreate)
        createImage.bind("<Button-1>", toCreate)

        bigFrame.pack()

# SEARCH PAGE
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Find", font=H1)
        label.grid(row=0, column=4, padx=10, pady=10)

        # Switches to homepage
        button1 = ttk.Button(self, text="Home", command=lambda: controller.show_frame(StartPage))
        button1.grid(row=1, column=1, padx=10, pady=10)


# CREATE PAGE
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Create", font=H1)
        label.grid(row=0, column=4, padx=10, pady=10)

        # Switches to homepage
        button2 = ttk.Button(self, text="Home", command=lambda: controller.show_frame(StartPage))
        button2.grid(row=2, column=1, padx=10, pady=10)


app = TkinterApp()
app.mainloop()
