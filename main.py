from tkinter import * 
from tkinter import ttk
import sqlite3

dataConnect = sqlite3.connect('myData.db')
cursor = dataConnect.cursor()

root = Tk()
root.title('Desktop App')

#Create a widget for text entry ---------

# item = Entry(root)
# item.grid(row=3, column=0)
# root.mainloop()


def upload_post(*args):
    # cursor.execute("INSERT INTO posts VALUES(:author,:body)")
    pass

def set_light_mode():
    #light style definition
    style.configure("light.TFrame", background="#ffffff")
    style.configure("light.TLabel", background="#ffffff", foreground="#000000")
    style.configure("light.TCheckbutton", background="#ffffff", foreground="#000000")
def set_dark_mode():
     #dark style definition
    style.configure("dark.TFrame", background="#2e2e2e")
    style.configure("dark.TLabel", background="#2e2e2e", foreground="#ffffff")
    style.configure("dark.TCheckbutton", background="#2e2e2e", foreground="#ffffff")
    mainframe.configure(style="TFrame")
#night mode toggle function
def toggle_theme():
    if night_mode_bool.get():
        set_dark_mode()
    else:
        set_light_mode()
    

# main window creation
mainframe = ttk.Frame(root)
root.geometry("420x420")
mainframe.grid(column=0,row=0, sticky=(N,W,E,S))

#styling 
style = ttk.Style()
style.theme_use("default")
mainframe.configure(style="TFrame")

#text input
meow = StringVar()
meow_entry = ttk.Entry(mainframe, width=7, textvariable=meow)
meow_entry.grid(column=2, row=4, sticky=(W, E))

#labels
ttk.Label(mainframe, text="Home Feed").grid(column=2, row=1, sticky=W)
Posts_label = StringVar()
ttk.Label(mainframe, textvariable=Posts_label).grid(column=3, row=3, sticky=W)
ttk.Button(mainframe, text="Upload", command=upload_post).grid(column=3, row=4, sticky=W)

ttk.Label(mainframe, text="caption").grid(column=2, row=3, sticky=W)
# ttk.Label(mainframe, text="likes").grid(column=2, row=2, sticky=W)


#night mode ----------

#Boolean Variable
night_mode_bool = StringVar()
#Check button
night_mode_button = ttk.Checkbutton(mainframe, text="Night Mode",
 variable=night_mode_bool, command=toggle_theme)
#Grid placement of button, col 3, row 1
night_mode_button.grid(column=3, row=1, sticky=(N,E))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)	
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

#Focus cursor on text box input when window opens
meow_entry.focus()
#Pressing Enter calls upload_post function
mainframe.bind("<Return>", upload_post)
toggle_theme()

#Runs the program loop
root.mainloop()