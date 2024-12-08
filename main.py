import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as tmb

window = tk.Tk()
window.title("Notepad")
window.geometry("400x400")

file_name = ""

def write_to_file(file_name):
    text = content_text.get(1.0, "end")
    with open(file_name, "w") as file:
        file.write(text)

def open_file():
    global file_name
    file_name = fd.askopenfilename()
    with open(file_name) as file:
        text = file.read()
        content_text.delete(1.0, "end")
        content_text.insert(1.0, text)
        file_label["text"] = f"File: {file_name}"

def save_as_file():
    global file_name
    file_name = fd.asksaveasfilename()
    write_to_file(file_name)
    file_label["text"] = f"File: {file_name}"
    tmb.showinfo("Saving file", f"Saving in {file_name}")
def save_file():
    if file_name == "":
        save_as_file()
    else:
        write_to_file(file_name)
        tmb.showinfo("Saving file", f"Saving in {file_name}")

def new_file():
    result = tmb.askokcancel("Creation New File", "Are you sure? All of the text will be deleted!")
    if result == True:
        global file_name
        file_name = ""
        content_text.delete(1.0, "end")
        file_label["text"] = f"File: {file_name}"
    else:
        return

def about():
    tmb.showinfo("About Program", "New - Deletes everything that you didn't save\nOpen - it opens a saved file\nSave - It saves your file\nSave As - it saves your file as a new one")


content_text = tk.Text(window, wrap="word", bg="#6495ED", fg="#191970")
content_text.place(x=0, y=0, relheight=1, relwidth=1)

file_label = tk.Label(window, text=f"File: {file_name}", bg="#6495ED", fg="#191970")
file_label.place(relx=0, rely=1, anchor = "sw")

main_menu = tk.Menu(window, type="menubar")
window.configure(menu=main_menu)

new_file_icon = tk.PhotoImage(file="new_file.gif")
open_file_icon = tk.PhotoImage(file="open_file.gif")
save_file_icon = tk.PhotoImage(file="save_file.gif")

file_menu = tk.Menu(main_menu, tearoff=0, bg="black", fg="white")
main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", image=new_file_icon, compound="left", command=new_file)
file_menu.add_command(label="Open", image=open_file_icon, compound="left", command=open_file)
file_menu.add_command(label="Save", image=save_file_icon, compound="left", command=save_file)
file_menu.add_command(label="Save As", image=save_file_icon, compound="left", command=save_as_file)

help_menu = tk.Menu(main_menu, tearoff=0, bg="black", fg="white")
main_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Creator")
help_menu.add_command(label="License")
help_menu.add_command(label="About", command=about)

help_menu = tk.Menu()





window.mainloop()