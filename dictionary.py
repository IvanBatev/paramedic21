from tkinter import *
import json




def load_json(dictionary_file):
    with open(dictionary_file, encoding="utf8") as dict_file:
        
        # Returns JSON object as a dictionary
        full_dict = json.load(dict_file)
    
    return full_dict
    
def create_sub_dictionaries(full_dict, criteria):
    
    for entry in full_dict['dictionary']:
        for key, value in entry.items():
            if key == 'category' and value == 'аnatomy':
                anatomy_dict.update(entry)
            elif key == 'lection' and value == '1 - Въведение в анатомията':
                lection_one_dict.update(entry)
            elif key == 'lection' and value == '1 - Въведение в анатомията':
                topic_dict.update(entry)

            
    



def lookup():
    print("Lookup")
    pass
    # Clear the text 
    # my_text.delete(1.0, END)

    # Lookup a word
    

    # Add definition to text box
    


def ui():
    root = Tk()
    root.title("Paramedic 21 речник")
    root.iconbitmap('paramedic.ico')

    # Root window dimensions
    root_width = 640
    root_height = 480

    # Screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()    

    # Calculate x and y coordinates for the Tk root window 

    x = (screen_width / 2) - (root_width / 2)
    y = (screen_height / 2) - (root_height / 2)

    # set the dimensions of the root window and where it is placed
    root.geometry('%dx%d+%d+%d' % (root_width, root_height, x, y))
    root.resizable(False, False)


    # Filters Label Frame 
    anatomy = IntVar()
    all_categories = IntVar()
    lection_one = IntVar()
    lection_two = IntVar()
    lection_three = IntVar()
    all_lectures = IntVar()
    latin_only = IntVar()

    # Filters frame 
    filters_frame = LabelFrame(root, text="Filters")
    filters_frame.grid(row=0, column=0, padx=10, pady=10, sticky='w')

    # Category frame
    category_frame = LabelFrame(filters_frame, text="Category", borderwidth=0, width=200)
    category_frame.grid(row=0, column=0, sticky='nw', pady=5)

    anatomy_checkbox = Checkbutton(category_frame, text="Anatomy", variable=anatomy, onvalue=1, offvalue=0, anchor="w")
    anatomy_checkbox.grid(row=0, column=0, padx=10, sticky='w')

    all_categories_checkbox = Checkbutton(category_frame, text="All", variable=all_categories, onvalue=1, offvalue=0, anchor="w")
    all_categories_checkbox.grid(row=1, column=0, padx=10, sticky='w')
    all_categories_checkbox.select()

    # Lections frame
    lection_frame = LabelFrame(filters_frame, text="Lection", borderwidth=0, width=200)
    lection_frame.grid(row=0, column=1, sticky='e', pady=5)

    lone_checkbox = Checkbutton(lection_frame, text="1 - Въведение в анатомията", variable=lection_one, onvalue=1, offvalue=0, anchor="w")
    lone_checkbox.grid(row=0, column=0, padx=10, sticky='w')

    ltwo_checkbox = Checkbutton(lection_frame, text="2 - ОДС част 1 - Въведение и кости", variable=lection_two, onvalue=1, offvalue=0, anchor="w")
    ltwo_checkbox.grid(row=1, column=0, padx=10, sticky='w')

    lthree_checkbox = Checkbutton(lection_frame, text="3 - ОДС част 2 - Стави", variable=lection_three, onvalue=1, offvalue=0, anchor="w")
    lthree_checkbox.grid(row=2, column=0, padx=10, sticky='w')

    all_lectures_checkbox = Checkbutton(lection_frame, text="Всички", variable=all_lectures, onvalue=1, offvalue=0, anchor="w")
    all_lectures_checkbox.grid(row=0, column=1, padx=10, sticky='w')
    all_lectures_checkbox.select()

    latin_checkbox = Checkbutton(filters_frame, text="Latin dictionary only", variable=latin_only, onvalue=1, offvalue=0, anchor='w')
    latin_checkbox.grid(row=3, column=0, columnspan=2, padx=0, sticky='w')

    setup_button = Button(filters_frame, text="Setup", command=lambda: create_sub_dictionaries(full_dict, anatomy_dict, lection_one_dict, topic_dict, latin_dict))
    setup_button.grid(row=3, column=1, pady=5, padx=10, sticky='e')   

    # Control frame
    control_frame = LabelFrame(root, text="Control", height=200)
    control_frame.grid(row=2, column=0, sticky='wn', pady=10, padx=10 )

    answer_button = Button(control_frame, text="Answer", command=lambda: create_sub_dictionaries(full_dict, anatomy_dict, lection_one_dict, topic_dict, latin_dict))
    answer_button.grid(row=0, column=1, pady=5, padx=10)

    ask_button = Button(control_frame, text="Ask", width=6, command=lambda: create_sub_dictionaries(full_dict, anatomy_dict, lection_one_dict, topic_dict, latin_dict))
    ask_button.grid(row=0, column=0, pady=5, padx=10)

    # Answer text field
    answer_text = Text(root, height=12, width=76, wrap=WORD, borderwidth=5)
    answer_text.grid(row=3, column=0, pady=5, padx=10)

    root.mainloop()

if __name__ == "__main__":

    anatomy_dict = dict()
    lection_one_dict = dict()
    topic_dict = dict()
    latin_dict = dict()
    dictionary_file = 'dictionary.json'
    full_dict = load_json(dictionary_file)
    ui()