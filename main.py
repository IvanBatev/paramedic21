import user_interface
import dictionary

def main():

    # Generate the full dictionary
    dictionary_file = 'dictionary.json'
    dictionary_data = dictionary.DictionaryData(dictionary_file)

    # Create the UI 
    program_title = "Paramedic 21 речник"
    icon = 'paramedic.ico'
    window_width = 640
    window_height = 480

    ui = user_interface.UserInterface(program_title,icon, window_width, window_height, dictionary_data)

    # If filters are applied, generate the corresponding dictionaries
    # if ui.all_categories == 1 and ui.all_lectures 
    anatomy_dict = dict()
    lection_one_dict = dict()
    latin_dict = dict()
    
    ui.root.mainloop()

if __name__ == "__main__":
    main()

