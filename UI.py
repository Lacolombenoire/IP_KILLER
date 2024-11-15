import tkinter as tk
from ERASER import *
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import messagebox


def select_file() :
    filepath = askopenfilename()
    if ERASER.is_texte_filepath(filepath) :
        File_src_entry.delete(0, tk.END)
        File_src_entry.insert(0, filepath)


def select_folder() :
    filepath = askdirectory()
    
    filepath_Entry.delete(0, tk.END)
    filepath_Entry.insert(0, filepath)


def IP_Killer() :
    src_file = File_src_entry.get()
    file_destination = filepath_Entry.get()
    file_name = namefile_entry.get()
    
    try :
        ERASER.ip_killer(src_file, file_destination, file_name)
    except Exception as e :
        
        messagebox.showerror("Error", e)

    else :
        messagebox.showinfo("showinfo",  "The file " + file_name + ".txt was created")

    
    

window = tk.Tk()
window.geometry("300x300")
window.title("IP killer")




File_src_entry = tk.Entry(window)
File_src_label = tk.Label(window, text="File source : ")
File_src_button = tk.Button(window, text="Browse...", command=select_file)



File_src_label.grid(row=0,column=0)
File_src_entry.grid(row=0, column=1)
File_src_button.grid(row=0, column=2)


filepath_label = tk.Label(window, text="Filepath : ")
filepath_Entry = tk.Entry(window)
filepath_Button = tk.Button(window, text="Browse...", command=select_folder)



filepath_label.grid(row=1, column=0)
filepath_Entry.grid(row=1, column=1)
filepath_Button.grid(row=1, column=2)


namefile_entry = tk.Entry(window)
namefile_label = tk.Label(window, text="File name : ")

namefile_label.grid(row=2, column=0)
namefile_entry.grid(row=2, column=1)




IP_killer_button = tk.Button(window, text="IP KILL", command=IP_Killer)


IP_killer_button.grid(row=3, column=1)








window.mainloop()

































