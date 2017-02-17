from Tkinter import *
import backend


def view_command():
    list1.delete(0, END)
    for shop in backend.view_address():
        list1.insert(END, shop)


def search_command():
    list1.delete(0, END)
    shops = backend.search(name_text.get(), street_text.get(), city_text.get(), state_text.get(), zip_text.get())
    if len(shops) == 0:
        list1.delete(0, END)
        list1.insert(END, "No matches found")
    else:
        for shop in shops:
            list1.insert(END, shop)


def add_command():
    result = backend.insert(name_text.get(), street_text.get(), city_text.get(), state_text.get(), zip_text.get())
    if result == -1:
        list1.delete(0, END)
        list1.insert(END, "Not a valid address")
    else:
        view_command()


def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])
    e5.delete(0, END)
    e5.insert(END, selected_tuple[5])


def delete_command():
    shop_id = selected_tuple[0]
    backend.delete(shop_id)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    view_command()


def update_command():
    shop_id = selected_tuple[0]
    backend.update(shop_id, name_text.get(), street_text.get(), city_text.get(), state_text.get(), zip_text.get())
    view_command()


def show_map_command():
    backend.show_map()


window = Tk()
window.wm_title("Coffee Shops Next to me")

l1 = Label(window, text='Name')
l1.grid(row=0, column=0)

name_text = StringVar()
e1 = Entry(window, textvariable=name_text)
e1.grid(row=0, column=1)

l2 = Label(window, text='Street Address')
l2.grid(row=0, column=2)

street_text = StringVar()
e2 = Entry(window, textvariable=street_text)
e2.place(x=310, y=0, width=470)

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
sb1.place(x=470, y=60, height=100)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=4)

b2 = Button(window, text="Search", width=12, command=search_command)
b2.grid(row=3, column=4)

b3 = Button(window, text="Add", width=12, command=add_command)
b3.grid(row=2, column=5)

b4 = Button(window, text="Update", width=12, command=update_command)
b4.grid(row=3, column=5)

b5 = Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=4, column=5)

b5 = Button(window, text="Show Map", width=12, command=show_map_command)
b5.grid(row=4, column=4)

b7 = Button(window, text="Close", width=12, command=window.destroy)
b7.grid(row=8, column=5)


window.mainloop()