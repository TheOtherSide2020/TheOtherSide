
from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Template Selection Window")
window.geometry('400x400')

window.configure(background="white");
TemplateName = Label(window, text="TemplateName").grid(row=0, column=0)
Question = Label(window, text="Question").grid(row=1, column=0)
Username = Label(window, text="UserName").grid(row=2, column=0)

TemplateNameEntry = Entry(window).grid(row=0, column=1)
QuestionEntry = Entry(window).grid(row=1, column=1)
UsernameEntry = Entry(window).grid(row=2, column=1)


def clicked():
    res = "Polling System"
    lbl.configure(text=res)

    #call json writer to write the repsonses in the json file.



btn = ttk.Button(window, text="Submit", command="clicked").grid(row=4, column=0)



window.mainloop()
