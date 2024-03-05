import csv
from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()
root.title('Codemy.com - TreeBase')
# root.iconbitmap('c:/gui/codemy.ico')
root.geometry("1000x500")

# Add Fake Data
'''
data = [
	["John", "Elder", 1, "123 Elder St.", "Las Vegas", "NV", "89137"],
	["Mary", "Smith", 2, "435 West Lookout", "Chicago", "IL", "60610"],
	["Tim", "Tanaka", 3, "246 Main St.", "New York", "NY", "12345"],
	["Erin", "Erinton", 4, "333 Top Way.", "Los Angeles", "CA", "90210"],
	["Bob", "Bobberly", 5, "876 Left St.", "Memphis", "TN", "34321"],
	["Steve", "Smith", 6, "1234 Main St.", "Miami", "FL", "12321"],
	["Tina", "Browne", 7, "654 Street Ave.", "Chicago", "IL", "60611"],
	["Mark", "Lane", 8, "12 East St.", "Nashville", "TN", "54345"],
	["John", "Smith", 9, "678 North Ave.", "St. Louis", "MO", "67821"],
	["Mary", "Todd", 10, "9 Elder Way.", "Dallas", "TX", "88948"],
	["John", "Lincoln", 11, "123 Elder St.", "Las Vegas", "NV", "89137"],
	["Mary", "Bush", 12, "435 West Lookout", "Chicago", "IL", "60610"],
	["Tim", "Reagan", 13, "246 Main St.", "New York", "NY", "12345"],
	["Erin", "Smith", 14, "333 Top Way.", "Los Angeles", "CA", "90210"],
	["Bob", "Field", 15, "876 Left St.", "Memphis", "TN", "34321"],
	["Steve", "Target", 16, "1234 Main St.", "Miami", "FL", "12321"],
	["Tina", "Walton", 17, "654 Street Ave.", "Chicago", "IL", "60611"],
	["Mark", "Erendale", 18, "12 East St.", "Nashville", "TN", "54345"],
	["John", "Nowerton", 19, "678 North Ave.", "St. Louis", "MO", "67821"],
	["Mary", "Hornblower", 20, "9 Elder Way.", "Dallas", "TX", "88948"]

]
'''

# Do some database stuff
# Create a database or connect to one that exists
conn = sqlite3.connect('db/recruits.db')

# Create a cursor instance
c = conn.cursor()

# # Create Table
# c.execute("""CREATE TABLE if not exists customers (
# 	first_name text,
# 	last_name text,
# 	id integer,
# 	D text,
# 	city text,
# 	state text,
# 	zipcode text)
# 	""")
# # Add dummy data to table
# '''
# for record in data:
# 	c.execute("INSERT INTO customers VALUES (:first_name, :last_name, :id, :address, :city, :state, :zipcode)",
# 		{
# 		'first_name': record[0],
# 		'last_name': record[1],
# 		'id': record[2],
# 		'address': record[3],
# 		'city': record[4],
# 		'state': record[5],
# 		'zipcode': record[6]
# 		}
# 		)
# '''

# Commit changes
conn.commit()

# Close our connection
conn.close()

def query_database():
    # Clear the Treeview
    for record in my_tree.get_children():
        my_tree.delete(record)
    # Create a database or connect to one that exists
    conn = sqlite3.connect('db/recruits.db')

    # Create a cursor instance
    c = conn.cursor()

    c.execute("SELECT * FROM basic")
    global records
    records = c.fetchall()

    # Add our data to the screen
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                           tags=('oddrow',))
        # increment counter
        count += 1

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()


# Add Some Style
style = ttk.Style()

# Pick A Theme
style.theme_use('default')

# Configure the Treeview Colors
style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")

# Change Selected Color
style.map('Treeview',
          background=[('selected', "#347083")])

# Create a Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Configure the Scrollbar
tree_scroll.config(command=my_tree.yview)

# Define Our Columns
my_tree['columns'] = ("ID", "First Name", "Last Name", "Date", "Country", "City")

# Format Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("First Name", anchor=CENTER, width=140)
my_tree.column("Last Name", anchor=CENTER, width=140)
my_tree.column("ID", anchor=CENTER, width=100)
my_tree.column("Date", anchor=CENTER, width=140)
my_tree.column("City", anchor=CENTER, width=140)
my_tree.column("Country", anchor=CENTER, width=140)
# my_tree.column("Zipcode", anchor=CENTER, width=140)

# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("First Name", text="First Name", anchor=CENTER)
my_tree.heading("Last Name", text="Last Name", anchor=CENTER)
my_tree.heading("Date", text="Date", anchor=CENTER)
my_tree.heading("City", text="City", anchor=CENTER)
my_tree.heading("Country", text="Country", anchor=CENTER)
# my_tree.heading("Zipcode", text="Zipcode", anchor=CENTER)

# Create Striped Row Tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

# Move Row Up
def up():
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row) - 1)


# Move Rown Down
def down():
    rows = my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row, my_tree.parent(row), my_tree.index(row) + 1)


# Remove one record
def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)


# Remove Many records
def remove_many():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)

# Clear entry boxes
def excel(result):
    with open('recruits.csv', 'a') as f:
        w = csv.writer(f, dialect='excel')
        for record in result:
            w.writerow(record)
# Select Record
def select_record(e):

    selected = my_tree.focus()
    # Grab record values
    values = my_tree.item(selected, 'values')

def refresh():
    query_database()

# Add Buttons
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

add_button = Button(button_frame, text="Add Record")
add_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = Button(button_frame, text="Remove One Selected", command=remove_one)
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_button = Button(button_frame, text="Remove Many Selected", command=remove_many)
remove_many_button.grid(row=0, column=4, padx=10, pady=10)

move_up_button = Button(button_frame, text="Move Up", command=up)
move_up_button.grid(row=0, column=5, padx=10, pady=10)

move_down_button = Button(button_frame, text="Move Down", command=down)
move_down_button.grid(row=0, column=6, padx=10, pady=10)

excel_button = Button(button_frame, text="Save as Excel", command=lambda: excel(records))
excel_button.grid(row=0, column=7, padx=10, pady=10)

refresh_button = Button(button_frame, text="Refresh Data", command=refresh)
refresh_button.grid(row=0, column=7, padx=10, pady=10)

# Bind the treeview
my_tree.bind("<ButtonRelease-1>", select_record)
# my_tree.bind("<Double-Button-1>", opengui)

# Run to pull data from database on start
query_database()

root.mainloop()