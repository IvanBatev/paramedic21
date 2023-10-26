from tkinter import *
import dictionary
import random
from tkinter.messagebox import showerror

class UserInterface:

    def popup_window(self,title):
        popup = showerror(title='Paramedic 21', message=title, icon='question')
        

    def answer(self, definition):
        self.answer_text.delete("1.0", END)

        for subdef in definition:
            subdef = '- ' + subdef + '\n\n'
            self.answer_text.insert(END, subdef)

    def ask(self, dict_data):
        if len(dict_data.filtered_dict['filtered_dictionary']) > 0:
            random_entry = random.sample(dict_data.filtered_dict['filtered_dictionary'], 1)
            lookup_word = random_entry[0]['lookup_word']
            self.popup_window(lookup_word)
            self.answer(random_entry[0]['definition'])
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

    def change_all_lections(self):
        if self.all_lections.get() == 1:
            self.lection_one.set(1)
            self.lection_two.set(1)
            self.lection_three.set(1)
        else:
            self.lection_one.set(0)
            self.lection_two.set(0)
            self.lection_three.set(0)

    def change_lection(self, lection):
        if lection.get() == 0:
            self.all_lections.set(0)
        else: 
            if self.lection_one.get() == 1 and self.lection_two.get() == 1 and self.lection_three.get() == 1:
                self.all_lections.set(1)

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
        if self.all_lections.get() == 1:
            self.filters_lections.append('1 - Въведение в анатомията')
            self.filters_lections.append('2 - ОДС1 - Кости')
            self.filters_lections.append('3 - ОДС2 - Стави')
        else: 
            if self.lection_one.get() == 1:
                self.filters_lections.append('1 - Въведение в анатомията')
            if self.lection_two.get() == 1:
                self.filters_lections.append('2 - ОДС1 - Кости')
            if self.lection_three.get() == 1:
                self.filters_lections.append('3 - ОДС2 - Стави')


        dictionary_data.filtered_dict = dictionary.DictionaryData.filter_full_dictionary(self.filters_category, self.filters_lections, dictionary_data.full_dict)
    

    def __init__(self, title, icon, win_width, win_height, dictionary_data):

        self.filters_category = list()
        self.filters_lections = list()
        # Generate root with title and icon
        self.root = Tk()
        self.root.title(title)
        self.root.iconbitmap(icon)

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
        self.lection_one = IntVar()
        self.lection_two = IntVar()
        self.lection_three = IntVar()
        self.all_lections = IntVar()
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


        # Lections frame
        lection_frame = LabelFrame(filters_frame, text="Lection", borderwidth=0, width=200)
        lection_frame.grid(row=0, column=1, sticky='e', pady=5)

        lone_checkbox = Checkbutton(lection_frame, text="1 - Въведение в анатомията", variable=self.lection_one, onvalue=1, offvalue=0, anchor="w", command=lambda:self.change_lection(self.lection_one))
        lone_checkbox.grid(row=0, column=0, padx=10, sticky='w')

        ltwo_checkbox = Checkbutton(lection_frame, text="2 - ОДС част 1 - Въведение и кости", variable=self.lection_two, onvalue=1, offvalue=0, anchor="w", command=lambda:self.change_lection(self.lection_two))
        ltwo_checkbox.grid(row=1, column=0, padx=10, sticky='w')

        lthree_checkbox = Checkbutton(lection_frame, text="3 - ОДС част 2 - Стави", variable=self.lection_three, onvalue=1, offvalue=0, anchor="w", command=lambda:self.change_lection(self.lection_three))
        lthree_checkbox.grid(row=2, column=0, padx=10, sticky='w')

        all_lections_checkbox = Checkbutton(lection_frame, text="Всички", variable=self.all_lections, onvalue=1, offvalue=0, anchor="w", command=self.change_all_lections)
        all_lections_checkbox.grid(row=0, column=1, padx=10, sticky='w')
        all_lections_checkbox.select()
        self.change_all_lections()

        latin_checkbox = Checkbutton(filters_frame, text="Latin dictionary only", variable=self.latin_only, onvalue=1, offvalue=0, anchor='w')
        latin_checkbox.grid(row=3, column=0, columnspan=2, padx=0, sticky='w')

        self.make_filters_lists(dictionary_data)
        
        setup_button = Button(filters_frame, text="Setup", command=lambda:self.make_filters_lists(dictionary_data))
        setup_button.grid(row=3, column=1, pady=5, padx=10, sticky='e')   

        # Control frame
        self.control_frame = LabelFrame(self.root, text="Control", height=200)
        self.control_frame.grid(row=1, column=0, sticky='wn', pady=10, padx=10 )
        
        ask_button = Button(self.control_frame, text="Ask", width=6, command=lambda:self.ask(dictionary_data))
        ask_button.grid(row=0, column=0, pady=5, padx=10)

        # Answer text field
        self.answer_text = Text(self.root, height=12, width=76, wrap=WORD, borderwidth=5)
        self.answer_text.grid(row=3, column=0, pady=5, padx=10)


        self.root.mainloop()