from tkinter import *
import json
from PIL import ImageTk, Image

root = Tk()
root.geometry('2000x1000');
root.wm_title("Template Selection Window")

root.configure(background="#b19cd9");

var1, var2, var3 = BooleanVar(root), BooleanVar(root), BooleanVar(root)
var1.set(FALSE);

canvas = Canvas(root, width=2000, height=1000, bg="#b19cd9")

image = Image.open("../Images/glassWall.png")  # PIL solution
image = image.resize((1500, 1000), Image.ANTIALIAS)

img = ImageTk.PhotoImage(image)
canvas.create_image(500, 0, anchor="nw", image=img)

canvas.create_text(200, 50, fill="black", font="Times 20 ",
                   text="Select a template for the display")

canvas.place(x=0, y=0)
Question = Label(root, text="Question", font="Times 20 ", fg="black").grid_forget()
OptionA = Label(root, text="Option A", font="Times 20 ").grid_forget()
OptionB = Label(root, text="Option B", font="Times 20 ").grid_forget()
OptionC = Label(root, text="Option C", font="Times 20 ").grid_forget()
OptionD = Label(root, text="Option D", font="Times 20 ").grid_forget()
QuestionEntry = Entry(root, width=70).grid_forget()
OptionAEntry = Entry(root, width=30).grid_forget()
OptionBEntry = Entry(root, width=30).grid_forget()
OptionCEntry = Entry(root, width=30).grid_forget()
OptionDEntry = Entry(root, width=30).grid_forget()


def writeToJson():
    person_dict = {
        "TemplateName": "Polling_Template",
        "Question": QuestionEntry,
        "OptionA": OptionAEntry,
        "OptionB": OptionBEntry,
        "OptionC": OptionCEntry,
        "OptionD": OptionDEntry
    }

    with open('../Json/data.txt', 'w') as json_file:
        json.dump(person_dict, json_file)


def clicked():
    if var1.get() == 1:
        Question.place(x=1500, y=200)
        OptionA.place(x=1040, y=550)
        OptionB.place(x=570, y=550)
        OptionC.place(x=1250, y=800)
        OptionD.place(x=1800, y=700)
        QuestionEntry.place(x=1500, y=250)
        OptionAEntry.place(x=1040, y=600)
        OptionBEntry.place(x=570, y=610)
        OptionCEntry.place(x=1250, y=850)
        OptionDEntry.place(x=1800, y=750)


PollingSystem = Checkbutton(root, text="Polling System", font="Times 20 ", var=var1, onvalue=1, offvalue=0,
                            bg="#b19cd9",
                            command=clicked).place(x=150,
                                                   y=150)
PromotionalTemplate = Checkbutton(root, text="Promotional Template", font="Times 20 ", var=var2,
                                  bg="#b19cd9").place(x=150, y=190)
TextTemplate = Checkbutton(root, text="Text Template", font="Times 20 ", var=var3, bg="#b19cd9").place(x=150,
                                                                                                       y=230)

btn = Button(root, text="Submit", command=writeToJson).place(x=200, y=300)

root.mainloop()
