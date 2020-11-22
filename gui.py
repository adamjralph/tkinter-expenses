# tkinter gui

from tkinter import *
#from PIL import ImageTk,Image
import sqlite3
import pandas as pd


root = Tk()
root.title('Database tkinter gui')
root.geometry('800x800')

# Create a database
conn = sqlite3.connect('data_expenses.db')

# Create cursor
c = conn.cursor()

# Create Table
c.execute("""CREATE TABLE expenses (
        item text,
        price integer,
        category text,
        date text
        )""")

# Create Submit function for database
def submit():

    conn = sqlite3.connect('data_expenses.db')

    c = conn.cursor()

    c.execute("INSERT INTO expenses VALUES (:item, :price, :category, :date)",
            {
                'item': item.get(),
                'price': price.get(),
                'category': category.get(),
                'date': date.get()
            })

    conn.commit()

    conn.close()
    # Clear text boxes
    item.delete(0, END)
    price.delete(0, END)
    category.delete(0, END)
    date.delete(0, END)

# Create query function
def query():

    conn = sqlite3.connect('data_expenses.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM expenses")
    records = c.fetchall()
    # Loop through results
    print_records = ''
    for record in records[0]:
        print_records += str(record) + '\n'

    query_label = Label(root, text=print_records)
    query_label.grid(row=6, column=0, columnspan=2)

    conn.commit()
    conn.close()

    return

def show_dataframe():

    conn = sqlite3.connect('data_expenses.db')
    query = "SELECT *, oid FROM expenses"
    df = pd.read_sql_query(query, conn)
    df_label = Label(root, text=df)
    df_label.grid(row=8, column=0, columnspan=2)


# Create entry boxes
item = Entry(root, width=30)
item.grid(row=0, column=1, padx=20)
price = Entry(root, width=30)
price.grid(row=1, column=1, padx=20)
category = Entry(root, width=30)
category.grid(row=2, column=1, padx=20)
date = Entry(root, width=30)
date.grid(row=3, column=1, padx=20)
# Create entry labels
item_label = Label(root, text='Item Name')
item_label.grid(row=0, column=0)
price_label = Label(root, text='Item Price')
price_label.grid(row=1, column=0)
category_label = Label(root, text='Category')
category_label.grid(row=2, column=0)
date_label = Label(root, text='Date')
date_label.grid(row=3, column=0)

# Create a Submit button
submit_button = Button(root, text='Add record to Database', command=submit)
submit_button.grid(row=4, column=0, columnspan=2, pady=10, padx =10, ipadx=150)

# Create a query button
query_button = Button(root, text='Show records', command=query)
query_button.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=150)

# Create a Show dataframe button
dataframe_button = Button(root, text='Show dataframe', command=show_dataframe)
dataframe_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=150)

# Commit change
conn.commit()

# Close connection
conn.close()

root.mainloop()
