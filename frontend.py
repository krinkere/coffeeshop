from Tkinter import *

window = Tk()

l1 = Label(window, text='Name')
l1.grid(row=0, column=0)

name_text = StringVar()
e1 = Entry(window, textvariable=name_text)
e1.grid(row=0, column=1)

l2 = Label(window, text='Street Address')
l2.grid(row=0, column=2)

street_text = StringVar()
e2 = Entry(window, textvariable=street_text)
e2.place(x=310, y=0, width=406)

l3 = Label(window, text='City')
l3.grid(row=1, column=0)

city_text = StringVar()
e3 = Entry(window, textvariable=city_text)
e3.grid(row=1, column=1)

l4 = Label(window, text='State')
l4.grid(row=1, column=2)

state_text = StringVar()
e4 = Entry(window, textvariable=state_text)
e4.grid(row=1, column=3)

l5 = Label(window, text='Zip Code')
l5.grid(row=1, column=4)

zip_text = StringVar()
e5 = Entry(window, textvariable=zip_text)
e5.grid(row=1, column=5)

list1 = Listbox(window, height=6, width=55)
list1.grid(row=2, column=0, rowspan=7, columnspan=4)
sb1 = Scrollbar(window)
# sb1.grid(row=2, column=2)
sb1.place(x=470, y=90, height=100)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = Button(window, text="View All", width=12)
b1.grid(row=2, column=5)

b2 = Button(window, text="Search", width=12)
b2.grid(row=3, column=5)

b3 = Button(window, text="Add", width=12)
b3.grid(row=4, column=5)

b4 = Button(window, text="Update", width=12)
b4.grid(row=5, column=5)

b5 = Button(window, text="Delete", width=12)
b5.grid(row=6, column=5)

b6 = Button(window, text="Close", width=12)
b6.grid(row=7, column=5)

window.mainloop()