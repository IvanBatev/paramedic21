import user_interface
import dictionary
import os
from tkinter.messagebox import showerror


def main():

    #Input files
    icon_file = 'paramedic.ico'
    dictionary_file = 'dictionary.json'

    # Generate the full dictionary
    if os.path.exists(dictionary_file):
        dictionary_data = dictionary.DictionaryData(dictionary_file)
    else:
        err = showerror(title='DICTIONARY', message='ADD DICTIONARY TO THE PROGRAM FOLDER', icon='error')
        return -1

    # Create the UI 
    program_title = "Paramedic 21 речник"
    window_width = 960
    window_height = 640

    ui = user_interface.UserInterface(program_title,icon_file, window_width, window_height, dictionary_data)

    ui.root.mainloop()

if __name__ == "__main__":
    main()


