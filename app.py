'''
Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton, PanedWindow, Radiobutton,
Scale, Scrollbar, and Spinbox. The other six are new: Combobox, Notebook, Progressbar,
Separator, Sizegrip and Treeview
'''

from recipe import *

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from add_recipe_to_csv import *
from search import *
from chatgbt_resipes import *
from convert import *
import sv_ttk



H1 = ("Arial", 35, "bold")
H2 = ("Arial", 24, "bold")
H3 = ("Arial", 18, "bold")
BODY = ("Arial", 16)

def toSearch(event):
    app.show_frame(Page1)

def toCreate(event):
    app.show_frame(Page2)

def toHome(event):
    app.show_frame(StartPage)




class TkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Byte 'n Bite")
        self.geometry("500x600")

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

        label = ttk.Label(self, text="Byte 'n Bite", font=H1)
        label.pack(pady=(20,155))

        label = ttk.Label(self, text="What would you like help with?", font=H3)
        label.pack(pady=(0, 40))
        bigFrame = tk.Frame(self)

        # Search
        searchFrame = ttk.Frame(bigFrame)

        image = Image.open("icons/search.png").convert("RGBA").resize((55, 55))
        photo = ImageTk.PhotoImage(image)

        # Create the button with the icon
        searchImage = ttk.Label(searchFrame, image=photo)
        searchImage.image = photo
        searchImage.pack(pady=(12, 0))

        searchLabel = ttk.Label(searchFrame, text="Find recipe", font=BODY)
        searchLabel.pack(padx=7, pady=(10, 12))

        searchFrame.pack(side='left', padx=(0, 15))

        searchFrame.bind("<Button-1>", toSearch)
        searchLabel.bind("<Button-1>", toSearch)
        searchImage.bind("<Button-1>", toSearch)

        # Create

        createFrame = ttk.Frame(bigFrame)

        image = Image.open("icons/create.png").convert("RGBA").resize((55, 55))
        photo = ImageTk.PhotoImage(image)

        # Create the button with the icon
        createImage = ttk.Label(createFrame, image=photo)
        createImage.image = photo
        createImage.pack(pady=(12, 0))

        createLabel = ttk.Label(createFrame, text="Create recipe", font=BODY)
        createLabel.pack(padx=7, pady=(10, 12))

        createFrame.pack()

        createFrame.bind("<Button-1>", toCreate)
        createLabel.bind("<Button-1>", toCreate)
        createImage.bind("<Button-1>", toCreate)

        bigFrame.pack()


# SEARCH PAGE
class Page1(tk.Frame):
    def bind_mouse_wheel(self):
        self.canvas.bind("<Enter>", self.enable_mouse_wheel)
        self.canvas.bind("<Leave>", self.disable_mouse_wheel)

    def enable_mouse_wheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)

    def disable_mouse_wheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")

    def on_mouse_wheel(self, event):
        self.canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # PAGE SETUP

        # Canvas
        self.canvas = tk.Canvas(self)
        self.canvas.pack(side="left", fill="both", expand=True)

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Frame
        self.contentFrame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.contentFrame, anchor="nw")

        # Bind frame position to scrollbar
        self.contentFrame.bind("<Configure>", self.update_scroll_region)

        # Bind mouse wheel scrolling
        self.bind_mouse_wheel()

        titleFrame = tk.Frame(self.contentFrame)

        label = ttk.Label(titleFrame, text="Search", font=H1)
        label.pack(side='left', padx=(20, 170), pady=(20, 0))

        image = Image.open("icons/home.png").convert("RGBA").resize((30, 30))
        photo = ImageTk.PhotoImage(image)


        # Create the button with the icon
        homeImage = ttk.Label(titleFrame, image=photo)
        homeImage.image = photo
        homeImage.pack(pady=(22, 0), padx=(20, 10))

        titleFrame.pack(pady=(0, 125))

        homeImage.bind("<Button-1>", toHome)




        self.entryText = ttk.Entry(self.contentFrame, width=30)
        self.entryText.pack(pady=(0, 15), ipady=4)


        submitButton = ttk.Button(self.contentFrame, text="Submit", command=lambda: self.submitFilters(self.entryText.get()))
        submitButton.pack(ipadx=5, ipady=5)

        self.title = ttk.Label(self.contentFrame, text="Click submit to find recipes!", font=H3)
        self.title.pack(pady=(45, 30))

        self.shownRecipes = []

    def submitFilters(self, prompt):
        for element in self.shownRecipes:
            element.destroy()

        self.shownRecipes = []

        self.title.config(text="Results")

        results = search(prompt.split(", "))

        if results is None:
            self.shownRecipes.append(ttk.Label(self.contentFrame, text="No results found.\nWould you like to generate or create a new one?", justify="center"))
            self.shownRecipes[-1].pack(pady=(0, 50))

            buttonFrame = ttk.Frame(self.contentFrame)

            generate = ttk.Button(buttonFrame, text="Generate", command=())
            generate.pack(side="left", padx=15)

            create = ttk.Button(buttonFrame, text="Create", command=lambda: toCreate(None))
            create.pack(side="left")

            buttonFrame.pack()

            self.shownRecipes.append(generate)
            self.shownRecipes.append(create)

        elif type(results) == int:
            self.title.config(text="Please enter some ingredients.")

        else:
            for recipe in results:
                button = ttk.Button(self.contentFrame, text=recipe.name, command=lambda:self.displayRecipe(recipe))
                button.pack()
                self.shownRecipes.append(button)



    def update_scroll_region(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def displayRecipe(self, recipe):
        popup = tk.Toplevel(self)
        popup.title(recipe.name)

        # Add content to the popup window
        label = tk.Label(popup, text=recipe)
        label.pack(pady=20)

        close_button = ttk.Button(popup, text="Close", command=popup.destroy)
        close_button.pack(pady=(0, 20))

    def displayGeneratedRecipe(self, recipe):
        popup = tk.Toplevel(self)
        popup.title(recipe.name)

        # Add content to the popup window
        label = tk.Label(popup, text=recipe)
        label.pack(pady=20)

        buttonFrame = ttk.Frame(popup)

        ingredients = ",".join(recipe.ingredients.keys())
        amounts = ",".join(recipe.ingredients.values())

        for i in range(len(recipe.instructions)):
            recipe.instructions[i] = str(i + 1) + ". " + recipe.instructions[i].get()
        instructions = ", ".join(recipe.instructions)

        keep_button = ttk.Button(buttonFrame, text="Save", command=lambda: input_to_csv(recipe.name, ingredients, amounts, instructions, recipe.servings, recipe.time))
        keep_button.pack(pady=(0, 20), padx=(0, 15))

        close_button = ttk.Button(buttonFrame, text="Close", command=popup.destroy)
        close_button.pack(pady=(0, 20))

        buttonFrame.pack()

    def generateRecipe(self, prompt):
        generated_recipe = convert_json_to_recipe(generate_recipe(prompt.split(", ")))
        self.displayGeneratedRecipe(generated_recipe)


# CREATE PAGE
class Page2(tk.Frame):

    def bind_mouse_wheel(self):
        self.canvas.bind("<Enter>", self.enable_mouse_wheel)
        self.canvas.bind("<Leave>", self.disable_mouse_wheel)

    def enable_mouse_wheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)

    def disable_mouse_wheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")

    def on_mouse_wheel(self, event):
        self.canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Canvas
        self.canvas = tk.Canvas(self)
        self.canvas.pack(side="left", fill="both", expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Frame
        self.contentFrame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.contentFrame, anchor="nw")

        # Bind frame position to scrollbar
        self.contentFrame.bind("<Configure>", self.update_scroll_region)

        # Bind mouse wheel scrolling
        self.bind_mouse_wheel()

        titleFrame = tk.Frame(self.contentFrame)

        label = ttk.Label(titleFrame, text="Create", font=H1)
        label.pack(side='left', padx=(20, 200), pady=(20, 0))

        image = Image.open("icons/home.png").convert("RGBA").resize((30, 30))
        photo = ImageTk.PhotoImage(image)

        # Create the button with the icon
        homeImage = ttk.Label(titleFrame, image=photo)
        homeImage.image = photo
        homeImage.pack(pady=(22, 0))

        titleFrame.pack(pady=(0, 50))

        homeImage.bind("<Button-1>", toHome)

        self.name = ttk.Entry(self.contentFrame, width=15)
        self.name.insert(0, "New Recipe")
        self.name.pack(padx=(20, 185), pady=(0, 40), ipady=4)

        ingredientsFrame = tk.Frame(self.contentFrame)

        ttk.Label(ingredientsFrame, text="Ingredients", font=H2).pack(side="left", padx=(10, 80), pady=(0, 30))

        image = Image.open("icons/create.png").convert("RGBA").resize((20, 20))
        photo = ImageTk.PhotoImage(image)

        # Create the button with the icon
        addImage = ttk.Label(ingredientsFrame, image=photo)
        addImage.image = photo
        addImage.pack(side="left", padx=(100, 0), pady=(0, 30))

        addImage.bind("<Button-1>", self.createIngredientsInput)

        ingredientsFrame.pack()

        self.ingredientsEntryFrame = ttk.Frame(self.contentFrame)

        self.ingredients = []
        self.createIngredientsInput(None)
        self.createIngredientsInput(None)

        self.ingredientsEntryFrame.pack()

        instructionsFrame = ttk.Frame(self.contentFrame)
        ttk.Label(instructionsFrame, text="Instructions", font=H2).pack(side="left", padx=(10, 80), pady=(0, 30))

        image = Image.open("icons/create.png").convert("RGBA").resize((20, 20))
        photo = ImageTk.PhotoImage(image)

        # Create the button with the icon
        addImage = ttk.Label(instructionsFrame, image=photo)
        addImage.image = photo
        addImage.pack(side="left", padx=(100, 0), pady=(0, 30))

        addImage.bind("<Button-1>", self.createInstructionsInput)

        instructionsFrame.pack(pady=(25, 0))

        self.instructionsEntryFrame = ttk.Frame(self.contentFrame)

        self.instructions = []
        self.createInstructionsInput(None)
        self.createInstructionsInput(None)

        self.instructionsEntryFrame.pack(pady=(0, 15))

        timeFrame = ttk.Frame(self.contentFrame)

        timeLabel = ttk.Label(timeFrame, text="Time to cook:")
        timeLabel.pack(side="left", padx=(0, 15))
        self.time = ttk.Entry(timeFrame, width=5)
        self.time.pack(side="left")

        timeFrame.pack()

        servingsFrame = ttk.Frame(self.contentFrame)

        servingsLabel = ttk.Label(servingsFrame, text="Servings:")
        servingsLabel.pack(side="left", padx=(0, 41), pady=15)
        self.servings = ttk.Entry(servingsFrame, width=5)
        self.servings.pack(side="left", pady=(10, 30))

        servingsFrame.pack()

        ttk.Button(self.contentFrame, text="Save", command=self.saveRecipe).pack(padx=(25, 0), pady=(0, 25), ipadx=5, ipady=5)



        self.servings = ttk.Entry()


    def update_scroll_region(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def createIngredientsInput(self, event):
        entryFrame = ttk.Frame(self.ingredientsEntryFrame)

        bullet = ttk.Label(entryFrame, text="\u2022", font=H3)
        entry1 = ttk.Entry(entryFrame, width=15)
        entry2 = ttk.Entry(entryFrame, width=10)

        bullet.pack(side="left", padx=20, pady=(0, 5))
        entry1.pack(side="left", ipady=4, padx=(0, 25), pady=(0, 10))
        entry2.pack(side="left", ipady=4, pady=(0, 10))

        entryFrame.pack()
        self.ingredients.append((entry1, entry2))

    def createInstructionsInput(self, event):
        entryFrame = ttk.Frame(self.instructionsEntryFrame)

        num = ttk.Label(entryFrame, text=(str(len(self.instructions) + 1) + "."), font=H3)
        entry = ttk.Entry(entryFrame, width=27)

        num.pack(side="left", padx=20, pady=(0, 5))
        entry.pack(side="left", ipady=4, pady=(0, 10))

        entryFrame.pack()
        self.instructions.append(entry)

    def saveRecipe(self):
        name = self.name.get()
        time = self.time.get()
        servings = self.servings.get()

        instructions = list_to_instructions(self.instructions)
        ingredients = list_to_ingredients(self.ingredients)
        ingredients_amount = list_to_amounts(self.ingredients)

        input_to_csv(name, ingredients, ingredients_amount, instructions, servings, time)

app = TkinterApp()
sv_ttk.set_theme("dark")
app.mainloop()