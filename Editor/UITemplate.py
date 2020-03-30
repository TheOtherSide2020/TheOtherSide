from tkinter import *
from tkinter import ttk
import json
from PIL import ImageTk, Image

root = Tk()
root.geometry('2000x1000')
root.wm_title("The Other Side")

root.configure(background="#b19cd9")


# contentEditor Button
def pollingTemplate():
    polling = Tk()
    polling.geometry('2000x1000')
    polling.wm_title("Template Selection Window")

    polling.configure(background="#b19cd9")

    var1, var2, var3 = BooleanVar(polling), BooleanVar(polling), BooleanVar(polling)
    var1.set(FALSE)

    canvas = Canvas(polling, width=2000, height=1000, bg="#b19cd9")
    image = Image.open("../Images/glassWall.png")
    image = image.resize((1500, 1000), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image, master=canvas)

    canvas.create_image(500, 0, anchor="nw", image=img)
    canvas.create_text(200, 50, fill="black", font="Times 20 ",
                       text="Content List")

    canvas.place(x=0, y=0)
    QuestionEntry = Entry(polling, width=70).place(x=1500, y=250)

    OptionAEntry = Entry(polling, width=30).place(x=1040, y=600)

    OptionBEntry = Entry(polling, width=30).place(x=570, y=610)

    OptionCEntry = Entry(polling, width=30).place(x=1250, y=850)

    OptionDEntry = Entry(polling, width=30).place(x=1800, y=750)
    Question = Label(polling, text="Question", font="Times 20 ", fg="black").place(x=1500, y=200)
    OptionA = Label(polling, text="Option A", font="Times 20 ").place(x=1040, y=550)
    OptionB = Label(polling, text="Option B", font="Times 20 ").place(x=570, y=550)
    OptionC = Label(polling, text="Option C", font="Times 20 ").place(x=1250, y=800)
    OptionD = Label(polling, text="Option D", font="Times 20 ").place(x=1800, y=700)

    def jsonWrite():

        person_dict = {

            "TemplateName": "Polling_Template",
            "Question": QuestionEntry,
            "OptionA": OptionAEntry,
            "OptionB": OptionBEntry,
            "OptionC": OptionCEntry,
            "OptionD": OptionDEntry
        }
        with open('../Json/PollingSystemRecords.txt', 'w') as json_file:
            json.dump(person_dict, json_file)

    btn = Button(polling, text="Submit", command=jsonWrite).place(x=200, y=300)

    polling.mainloop()


def openContentEditorScreen():
    contentEditor = Tk()
    contentEditor.geometry('2000x1000');
    contentEditor.wm_title("Content Editor")
    contentEditor.configure(background="#b19cd9");

    Header = Label(contentEditor, text="Select your template", font="Arial 30 ", bg="#b19cd9", fg="black").place(x=800,
                                                                                                                 y=100)

    # available templates
    ShowcaseTemplate = Button(contentEditor, text="Showcase", width=35, height=15, font="Arial 20 ",
                              fg="black").place(x=100, y=200)
    PollingTemplate = Button(contentEditor, text="Polling Template", width=35, height=15, font="Arial 20 ",
                             fg="black", command=pollingTemplate).place(x=700, y=200)
    ConversationTemplate = Button(contentEditor, text="Conversation", width=35, height=15, font="Arial 20 ",
                                  fg="black").place(x=1300, y=200)


ContentEditorButton = Button(root, text="Content Editor", width=35, height=15, font="Arial 20 ", fg="black",
                             command=openContentEditorScreen).place(
    x=400, y=200)


def openDataCollectionScreen():
    dataCollection = Tk()
    dataCollection.geometry('2000x1000')
    dataCollection.wm_title("Content Editor")
    dataCollection.configure(background="#b19cd9")


# Data collection button
DataCollectionButton = Button(root, text="Data Collection", width=35, height=15, font="Arial 20 ", fg="black",
                              command=openDataCollectionScreen).place(
    x=1100, y=200)

root.mainloop()
