from tkinter import *
import dictionary
import random
from tkinter.messagebox import showerror

class UserInterface:

    def popup_window(self,title):
        popup = showerror(title='Paramedic 21', message=title, icon='question')
        

    def answer(self, latin, definition):
        self.answer_text.delete("1.0", END)
        latin = latin.upper() + '\n\n'
        self.answer_text.insert(END, latin)

        for subdef in definition:
            subdef = '- ' + subdef + '\n'
            self.answer_text.insert(END, subdef)

    def ask(self, dict_data):
        if len(dict_data.filtered_dict['filtered_dictionary']) > 0:
            random_entry = random.sample(dict_data.filtered_dict['filtered_dictionary'], 1)
            lookup_word = random_entry[0]['lookup_word']
            self.popup_window(lookup_word)
            self.answer(random_entry[0]['latin'],random_entry[0]['definition'])
        else:
            self.popup_window("Empty filtered dictionary!")


    def change_all_categories(self):
        if self.all_categories.get() == 1:
            self.anatomy.set(1)
        else:
            self.anatomy.set(0)


    def change_category(self, category):
        if category.get() == 1:
            self.all_categories.set(1)
        else:
            self.all_categories.set(0)

    def change_all_lections(self, dictionary_data):
        if self.lections[0].get() == 1:
            for lection in self.lections[1:]:
                lection.set(1)
        else:
            for lection in self.lections[1:]:
                lection.set(0)
        self.make_filters_lists(dictionary_data)

    def change_lection(self, lection, dictionary_data):
        if lection.get() == 0:
            self.lections[0].set(0)
        else: 
            if self.lections[1].get() == 1 and self.lections[2].get() == 1 and self.lections[3].get() == 1 and self.lections[4].get() == 1:
                self.lections[0].set(1)
        self.make_filters_lists(dictionary_data)

    def make_filters_lists(self, dictionary_data):
        # Clear obsolete data
        self.filters_lections.clear()
        self.filters_category.clear()

        # fill in categories list
        if self.all_categories.get() == 1:
            self.filters_category.append('anatomy')
        else: 
            if self.anatomy.get() == 1:
                self.filters_category.append('anatomy')

        # fill in lections list
        if self.lections[0].get() == 1:
            for i in range(self.num_of_lections-1):
                self.filters_lections.append(self.lection_names[i])
                print("self.filters_lections" + self.filters_lections[i])
        else: 
            if self.lections[1].get() == 1:
                self.filters_lections.append('1 - Въведение в анатомията')
            if self.lections[2].get() == 1:
                self.filters_lections.append('2 - ОДС1 - Кости')
            if self.lections[3].get() == 1:
                self.filters_lections.append('3 - ОДС2 - Стави')
            if self.lections[4].get() == 1:
                self.filters_lections.append('4 - ОДС3 - Мускули')

        print("Categories:",self.filters_category)
        print("Lections:",self.filters_lections)

        dictionary_data.filtered_dict = dictionary.DictionaryData.filter_full_dictionary(self.filters_category, self.filters_lections, dictionary_data.full_dict, self.latin_only)
    

    def __init__(self, title, icon, win_width, win_height, dictionary_data):

        self.filters_category = list()
        self.filters_lections = list()
        # Generate root with title and icon
        self.root = Tk()
        self.root.title(title)
        self.root.iconbitmap(icon)

        # Number of lections (number of lections + 1 [index 0] for all lections options)
        self.num_of_lections = 5

        # Root window dimensions
        self.root_width = win_width
        self.root_height = win_height

        # Screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()    

        # Calculate x and y coordinates for the Tk root window 
        self.x = (screen_width / 2) - (self.root_width / 2)
        self.y = (screen_height / 2) - (self.root_height / 2)

        # set the dimensions of the root window and where it is placed
        self.root.geometry('%dx%d+%d+%d' % (self.root_width, self.root_height, self.x, self.y))

        # Not resizable
        self.root.resizable(False, False)

        # Filters Label Frame 
        self.anatomy = IntVar()
        self.all_categories = IntVar()

        # self.lections is list of IntVar()s used in Checkboxes for lections. all_lections is [0]
        self.lections = []
        checkboxes = []

        for i in range(self.num_of_lections):
            self.lections.append(IntVar())

        self.lection_names = dictionary.DictionaryData.generate_list_of_lections(dictionary_data.full_dict)
        print(self.lection_names)

        self.latin_only = IntVar()

        # Filters frame 
        filters_frame = LabelFrame(self.root, text="Filters")
        filters_frame.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        # Category frame
        category_frame = LabelFrame(filters_frame, text="Category", borderwidth=0, width=200)
        category_frame.grid(row=0, column=0, sticky='nw', pady=5)

        anatomy_checkbox = Checkbutton(category_frame, text="Anatomy", variable=self.anatomy, onvalue=1, offvalue=0, anchor="w", command=lambda:self.change_category(self.anatomy))
        anatomy_checkbox.grid(row=0, column=0, padx=10, sticky='w')

        all_categories_checkbox = Checkbutton(category_frame, text="All", variable=self.all_categories, onvalue=1, offvalue=0, anchor="w", command=self.change_all_categories)
        all_categories_checkbox.grid(row=1, column=0, padx=10, sticky='w')
        all_categories_checkbox.select()
        self.change_all_categories()

        lection_checkboxes = [None] * self.num_of_lections

        # Lections frame
        lection_frame = LabelFrame(filters_frame, text="Lection", borderwidth=0, width=200)
        lection_frame.grid(row=0, column=1, sticky='e', pady=5)

        for i in range(self.num_of_lections):
            if i != 0:
                lection_checkboxes[i] = Checkbutton(lection_frame, text=self.lection_names[i-1], variable=self.lections[i], onvalue=1, offvalue=0, anchor="w", command=lambda:self.change_lection(self.lections[i], dictionary_data))
                lection_checkboxes[i].grid(row=i-1, column=0, padx=10, sticky='w')
            else:
                lection_checkboxes[i] = Checkbutton(lection_frame, text="Всички", variable=self.lections[i], onvalue=1, offvalue=0, anchor="w", command=lambda:self.change_all_lections(dictionary_data))
                lection_checkboxes[i].grid(row=i, column=1, padx=10, sticky='w')
                lection_checkboxes[i].select()

        self.change_all_lections(dictionary_data)

        latin_checkbox = Checkbutton(filters_frame, text="Latin dictionary only", variable=self.latin_only, onvalue=1, offvalue=0, anchor='w')
        latin_checkbox.grid(row=3, column=0, columnspan=2, padx=0, sticky='w')

        self.make_filters_lists(dictionary_data)

        # Control frame
        self.control_frame = LabelFrame(self.root, text="Control", height=200)
        self.control_frame.grid(row=1, column=0, sticky='wn', pady=10, padx=10 )
        
        ask_button = Button(self.control_frame, text="Ask", width=6, command=lambda:self.ask(dictionary_data))
        ask_button.grid(row=0, column=0, pady=5, padx=10)

        # Answer text field
        self.answer_text = Text(self.root, height=23, width=115, wrap=WORD, borderwidth=5)
        self.answer_text.grid(row=3, column=0, pady=5, padx=10)


        self.root.mainloop()