from tkinter import *
from PyDictionary import PyDictionary

root = Tk()
root.title("Paramedic 21 речник")
root.iconbitmap('paramedic.ico')
root.geometry("570x500")


def read_json():
    pass
def lookup():
    # Clear the text 
    my_text.delete(1.0, END)

    # Lookup a word
    

    # Add definition to text box
    


def ui():
    my_labelframe = LabelFrame(root, text="Enter a word")
    my_labelframe.pack(pady=20)

    my_entry = Entry(my_labelframe, font=("Helvetica", 28))
    my_entry.grid(row=0, column=0, padx=0, pady=10)

    my_button = Button(my_labelframe, text="Lookup", command=lookup)
    my_button.grid(row=0, column=1, padx=10)

    my_text = Text(root, height=20, width=65, wrap=WORD)
    my_text.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":

    ui()
