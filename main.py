from tkinter import * 
from tkinter import ttk
import sqlite3

dataConnect = sqlite3.connect('myData.db')
cursor = dataConnect.cursor()


root = Tk()
root.title('Desktop App')

#Create a widget for text entry ---------

def upload_post(title, body):
    cursor.execute("INSERT INTO posts (title, body) VALUES (?, ?)",(title, body))
    dataConnect.commit()

def set_light_mode():
    #setting light style
    style.configure("TFrame")
    style.configure("TLabel")
    style.configure("TCheckbutton")
    sidebar.configure(style="TFrame")
    mainframe.configure(style="TFrame")
    root.configure(background="#D9D9D9")
def set_dark_mode():
    #setting dark style
    sidebar.configure(style="dark.TFrame")
    mainframe.configure(style="dark.TFrame")
    root.configure(background="#2e2e2e")
def toggle_theme():
    if night_mode_bool.get():
        set_dark_mode()
    else:
        set_light_mode()
def toggle_sidebar():
    if sidebar.winfo_ismapped():
        sidebar.grid_remove()
    else:
        sidebar.grid()

def render_home_feed():
    if len(posts_dict) > 0:
        for child in homeframe.winfo_children():
            child.destroy()
        
    cursor.execute("SELECT * FROM posts")
    rows = cursor.fetchall()
    
    for post in rows:
        frame_name = f'post_{len(posts_dict)}'
        frame = ttk.Frame(homeframe, width=200, height=150)
        frame.pack(pady=5)
        
        posts_dict[frame_name] = frame
        frame.pack(padx=5, pady=5)
        ttk.Label(frame, text=post[1]).pack()
        ttk.Label(frame, text=post[2]).pack()

root.geometry("420x420")

# frames
mainframe = ttk.Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S))

homeframe = ttk.Frame(mainframe)
homeframe.grid(column=1, row=0, sticky=(N,S))


sidebar = ttk.Frame(root, width=150)
sidebar.grid(column=2,row=0, sticky=(E,N))
sidebar.grid_remove()
ttk.Button(sidebar, text="Refresh", command=render_home_feed).pack()

#frame configure (make row/col stretch with window size)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)	
mainframe.rowconfigure(0, weight=1)	
mainframe.columnconfigure(0, weight=1)
# homeframe.columnconfigure(0, weight=1)
# homeframe.rowconfigure(0, weight=1)

#overlay frame meant for top level content -eg sidebar
# overlay = ttk.Frame(root, style="Overlay.TFrame")
# overlay.place(relx=0, rely=0, relwidth=1, relheight=1)
# overlay.lift()

#styling 
style = ttk.Style()
style.theme_use("default")

#style def's
style.configure("grey.TFrame", background="#5f5f5f")
style.configure("dark.TFrame", background="#2e2e2e")
style.configure("dark.TLabel", background="#2e2e2e", foreground="#ffffff")
style.configure("dark.TCheckbutton", background="#2e2e2e", foreground="#ffffff")
root.configure(background="#D9D9D9")

homeframe.configure(style="grey.TFrame")



#home feed frame
# ttk.Button(mainframe, text="Menu", command=lambda: (
#         sidebar.grid_remove() if menu_bool.get() else sidebar.grid(),
#         menu_bool.set(not menu_bool.get())
#     )).grid(column=4, row=0, sticky=(N,W))

#holds the frames of the home feed posts
posts_dict = {}

post_box = ttk.Frame(mainframe, width=200, height=200)
post_box.grid(column=0, row=0, sticky=(W,N))

ttk.Label(post_box, text="Title").grid(column=0, row=0, sticky=W)
title_input = StringVar()
title_field = ttk.Entry(post_box, width=7, textvariable=title_input)
title_field.grid(column=0, row=1, sticky=(W, E))

ttk.Label(post_box, text="Body").grid(column=1, row=0, sticky=W)
body_input = StringVar()
body_field = ttk.Entry(post_box, width=7, textvariable=body_input)
body_field.grid(column=1, row=1, sticky=(W, E))

ttk.Button(post_box, text="Upload", command=lambda: upload_post(title=title_input.get(), body=body_input.get())).grid(column=0, row=2, sticky=(W,E))


ttk.Button(mainframe, text="Menu", command=toggle_sidebar).grid(column=2, row=0, sticky=(N,W))
ttk.Label(sidebar, text="side bar").pack()



#night mode ----------

#Boolean Variable
night_mode_bool = BooleanVar()
#Check button
night_mode_button = ttk.Checkbutton(sidebar, text="Night Mode",
 variable=night_mode_bool, command=toggle_theme)
# night_mode_button.grid(column=3, row=1, sticky=(N,E))
night_mode_button.pack()






#Focus cursor on text box input when window ens
# meow_entry.focus()
#Pressing Enter calls upload_post function
mainframe.bind("<Return>", upload_post)
render_home_feed()
#Runs the program loop
root.mainloop()