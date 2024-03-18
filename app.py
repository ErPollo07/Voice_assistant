from tkinter import *
from tkinter.ttk import *
import json


with open('settings.json') as f:
    settings = json.load(f)

def on_select(event):
    selected_lang = cb_lang_selector.get()
    
    # write the selected value
    settings['lang'] = selected_lang
    
    # write the file with the selected_lang
    with open('settings.json', 'w') as f:
        json.dump(settings, f, indent=4)

    # Check if the selected language is "None" or not
    if selected_lang != "None":
        lbl_warning_lang.grid_remove()  # Hide the label if "None" is selected
    else:
        lbl_warning_lang.grid()  # Show the label if any other language is selected

window = Tk()
window.title("Voice assistant settings")

lbl_lang = Label(window, text="Language", font=("Calibri", 20))
lbl_lang.grid(column=0, row=0)

cb_lang_selector = Combobox(window)
cb_lang_selector['values'] = ("None", "it-IT", "en-US", "en-UK")
cb_lang_selector.grid(column=1, row=0)

# set the default value of the combobox for selecting the language is None
cb_lang_selector.current(0)

# call the function 
cb_lang_selector.bind("<<ComboboxSelected>>", on_select)

lbl_warning_lang = Label(window, text="You must select a language", font=("Calibri", 10), anchor=CENTER)

# Initially hide the warning label
lbl_warning_lang.grid(column=0, row=1, columnspan=2, sticky='ew')
    
window.mainloop()
