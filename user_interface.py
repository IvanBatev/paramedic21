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

    def get_current_mask(self):
        current_mask = 0x00
        lection_number = 0

        for _ , checkbox in self.lections_checkboxes.items():

            if checkbox.get() == 1:
                current_mask = current_mask | (0x1 << lection_number) 

            lection_number += 1

        return current_mask
    
    def handle_all_checkbox(self, new_mask):

        if (new_mask & 0x1) == 0x1:
            for _, checkbox in self.lections_checkboxes.items():
                checkbox.set(1)
        else: 
            for _, checkbox in self.lections_checkboxes.items():
                checkbox.set(0)

        new_mask = self.get_current_mask()
        self.previous_mask = new_mask

    def switch_all_checkbox(self, new_mask):

        if ((new_mask & 0x1) == 0x1)  and ((new_mask >> 1) < (self.previous_mask >> 1)):
            self.lections_checkboxes['Всички'].set(0)
        elif ((new_mask & 0x1) == 0x0)  and ((new_mask >> 1) == 2**self.number_of_lections -1):
            self.lections_checkboxes['Всички'].set(1)

        new_mask = self.get_current_mask()
        self.previous_mask = new_mask        

    
    def change_lection(self, dictionary_data):
        
        new_mask = self.get_current_mask()   

        if (new_mask & 0x1) != (self.previous_mask & 0x1):
            self.handle_all_checkbox(new_mask)   
        else:
            self.switch_all_checkbox(new_mask)  


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
        if (self.previous_mask & 0x1) == 0x0:
            check_mask = self.previous_mask
            for lection, checkbox in self.lections_checkboxes.items():
                if lection != 'Всички':
                    if (check_mask & 0x1) == 0x1:
                        self.filters_lections.append(lection)
                    check_mask = check_mask >> 1
                else: 
                    check_mask = check_mask >> 1
        else: 
            for lection, checkbox in self.lections_checkboxes.items():
                if lection != 'Всички':
                    self.filters_lections.append(lection)

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

        self.list_of_lections = dictionary.DictionaryData.generate_list_of_lections(dictionary_data.full_dict)
        self.number_of_lections = len(self.list_of_lections) - 1 # Don't count the "Всички" entry

        self.lections_checkboxes = {}
        for lection in self.list_of_lections:
            self.lections_checkboxes.update({lection:None})

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

        self.previous_mask = 0x1f
        for lection in self.list_of_lections:
            is_selected = BooleanVar()
            check = Checkbutton(lection_frame, text=lection, variable=is_selected, onvalue=1, offvalue=0, anchor="w", command=lambda:self.change_lection(dictionary_data))
            check.grid(padx=10, sticky='w')
            self.lections_checkboxes[lection] = is_selected
            check.select()

        self.change_lection(dictionary_data)

        latin_checkbox = Checkbutton(filters_frame, text="Latin dictionary only", variable=self.latin_only, onvalue=1, offvalue=0, anchor='w')
        latin_checkbox.grid(row=3, column=0, columnspan=2, padx=0, sticky='w')

        #self.make_filters_lists(dictionary_data)

        # Control frame
        self.control_frame = LabelFrame(self.root, text="Control", height=200)
        self.control_frame.grid(row=1, column=0, sticky='wn', pady=10, padx=10 )
        
        ask_button = Button(self.control_frame, text="Ask", width=6, command=lambda:self.ask(dictionary_data))
        ask_button.grid(row=0, column=0, pady=5, padx=10)

        # Answer text field
        self.answer_text = Text(self.root, height=23, width=115, wrap=WORD, borderwidth=5)
        self.answer_text.grid(row=3, column=0, pady=5, padx=10)


        self.root.mainloop()