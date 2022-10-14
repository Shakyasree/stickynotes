from tkinter  import *

color_bg="white"
color_fg="Black"
Menu_bg ="Black"

MainWindow = Tk()
MainWindow.geometry('350x200')
MainWindow.title('quick notes')
MainWindow.wm_resizable(False,False)

def change_appearnce(color_bg,color_fg):
    NotesArea['bg']=color_bg
    NotesArea['fg']=color_fg
def white_on_black():
   color_bg="Black"
   color_fg="white"
   NotesArea.configure(insertbackground="white")
   Menubar['bg']=Menu_bg
   change_appearnce(color_bg,color_fg)
def Default():
    global color_bg,color_fg
    Menubar['bg']="green"
    change_appearnce(color_bg,color_fg)
def Black_on_orange():
    color_bg= "Orange"
    color_fg= "Black"
    Menubar['bg']="green"
    change_appearnce(color_bg,color_fg)

Menubar = Menu(MainWindow,bg=Menu_bg)
Appearence = Menu(Menubar,tearoff=0)

Menubar.add_cascade(label="appearence",menu=Appearence)
Appearence.add_command(label="White on black",command=white_on_black)
Appearence.add_command(label="Default",command=Default)
Appearence.add_command(label="Black on Orange",command=Black_on_orange)
MainWindow.config(menu=Menubar)
NotesArea = Text(MainWindow,bg=color_bg,fg=color_fg,font="ubuntu 15 bold")
NotesArea.pack(fill=BOTH)

MainWindow.mainloop()
