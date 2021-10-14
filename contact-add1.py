from  tkinter import *
# initialize windows
root.geometry('400 x 400')
root.config(bg = 'SlateGrey3')
root.resizable(0,0)
root.title("DataFlair-AddressBook")

## Add contact List
contactlist = [
    ['Parv Maheswari',  '0176738493'],
    ['David Sharma',  '2684430000'],
    ['Mandish Kabra',   '4338354432'],
    ['Prisha Modi','6834552341'],
    ['Rahul kaushik',   '1234852689'],
    ['Johena Shaa' , '2119876543'],
]

Name = StringVar()
Number = StringVar()
frame = Frame(root)
frame.pack(side=RIGHT)
scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=12)
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)

## Define functions
def Selected():
    return int(select.curselection()[0])

def AddContact():
    contactlist.append([Name.get(), Number.get()])
    Select_set()


