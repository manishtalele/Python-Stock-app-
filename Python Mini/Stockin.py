from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image, ImageDraw, ImageFont
import datetime
import tkcalendar as Cal
from tkinter import messagebox
import pymysql


# All function

# logout Function

# var names
username = "username_txt"
# logout function

def Logout():
    temp = messagebox.askyesno("Warring", "Do you want to Close")
    if (temp):
        stockin.destroy()
        import Main

def cleardata():
    for record in instock_tv.get_children():
        instock_tv.delete(record)
    for record in outstock_tv.get_children():
        outstock_tv.delete(record)

def Insert():
    hour = str(e.hour)
    minute = str(e.minute)
    sec = str(e.second)
    day = str(e.day)
    month = str(e.month)
    year = str(e.year)
    realtime = (hour + ":" + minute + ":" + sec)
    realdate = (year + "-" + month + "-" + day)
    Time = (hr.get() + ":" + mins.get())
    stock_name = name.get()
    date_forinsert = date.get()
    sql = "INSERT INTO stockin VALUES (%s,%s,%s,%s,%s,%s)"
    cur.execute(sql, (date_forinsert, stock_name,
                Time, username, realtime, realdate))
    conn.commit()
    name.delete(0, 'end')
    date.delete(0, 'end')
    hr.delete(0, 'end')
    mins.delete(0, 'end')
    cleardata()
    stockcall(instock_tv , outstock_tv)
    return True


# sql treeveiw query
conn = pymysql.connect(
    host="localhost", user="root", password="root", database="stock")
cur = conn.cursor()


def stockcall(instock_tv , outstock_tv):
    sql = "select * from stockin"
    cur.execute(sql)
    rows = cur.fetchall()
    sql = "select * from stockout"
    cur.execute(sql)
    rows_out = cur.fetchall()
    for i in rows:
        instock_tv.insert('', 'end', values=i)
    for i in rows_out:
        outstock_tv.insert('', 'end', values=i)
    return rows, rows_out


# stockin to make a stockin window and set the window size
stockin = Tk()
stockin.geometry("1366x768")
stockin.configure(bg='#FFFFFF')
stockin.title("Retail Management")


# header image input
header = ImageTk.PhotoImage(Image.open("image/in_head.png"))
head = Label(image=header)
head.configure(bg='#FFFFFF')
head.place(relx=0.40, anchor=NE)

# User and login details
Frame = Image.open("image/Userdetails_bg.png")

#  details to the frame
e = datetime.datetime.now()
# Username = (" User: Tejas")
# Logindata = (" Login date: %s-%s-%s" % (e.day, e.month, e.year))
# Frame_img = ImageDraw.Draw(Frame)
# Frame_img.text((12, 12), Username, fill="#000000")
# Frame_img.text((12, 24), Logindata, fill="#000000")
# Frame = ImageTk.PhotoImage(Frame)
# frame = Label(image=Frame)
# frame.configure(bg='#FFFFFF')
# frame.place(relx=0.40, rely=0.2, anchor=NE)




#  data btn and label
date_txt = Label(stockin, text='Date: ')
date_hint = Label(stockin, text='YYYY-MM-DD')
date_txt.configure(font=('Arial Rounded MT', 20), bg='#FFFFFF')
date_txt.place(relx=0.08, rely=0.53, anchor=NE)
date_hint.configure(font=('Arial Rounded MT', 14), bg='#FFFFFF')
date_hint.place(relx=0.17, rely=0.54, anchor=NE)
#  select btn for date
Date_txt = Canvas(stockin, width=1, height=1)
Date_txt.place(relx=0.3, rely=0.6, anchor=NE)
date = Entry(stockin, width=17, font=('Arial Rounded MT', 15), borderwidth=2,
             highlightcolor="black", justify="center", textvariable="datetxt")
Date_txt.create_window(450, 250, window=date)
date.place(relx=0.39, rely=0.54, anchor=NE)


# Name txt for stock
Name_txt = Label(stockin, text='Name of the Stock:')
Name_txt.configure(font=('Arial Rounded MT', 20), bg='#FFFFFF')
Name_txt.place(relx=0.2, rely=0.64, anchor=NE)
name_txt = Canvas(stockin, width=1, height=1)
name_txt.place(relx=0.3, rely=0.6, anchor=NE)
name = Entry(stockin, width=17, font=('Arial Rounded MT', 15), borderwidth=2,
             highlightcolor="black", justify="center", textvariable="Usertxt")
name_txt.create_window(450, 250, window=name)
name.place(relx=0.39, rely=0.65, anchor=NE)


# Time  txt and Btn
time_txt = Label(stockin, text='Time:')
time_txt.configure(font=('Arial Rounded MT', 20), bg='#FFFFFF')
time_txt.place(relx=0.08, rely=0.75, anchor=NE)
#  select btn for Time
# hr txt and input box
hr_txt = Label(stockin, text='Hour')
hr_txt.configure(font=('Arial Rounded MT', 14), bg='#FFFFFF')
hr_txt.place(relx=0.28, rely=0.76, anchor=NE)
Hr_txt = Canvas(stockin, width=1, height=1)
Hr_txt.place(relx=0.3, rely=0.6, anchor=NE)
hr = Entry(stockin, width=5, font=('Arial Rounded MT', 10), borderwidth=2,
           highlightcolor="black", justify="center", textvariable="hrtxt")
Hr_txt.create_window(10, 30, window=hr)
hr.place(relx=0.31, rely=0.765, anchor=NE)
# mins txt and input box
min_txt = Label(stockin, text='Minutes')
min_txt.configure(font=('Arial Rounded MT', 14), bg='#FFFFFF')
min_txt.place(relx=0.36, rely=0.76, anchor=NE)
Min_txt = Canvas(stockin, width=1, height=1)
Min_txt.place(relx=0.3, rely=0.6, anchor=NE)
mins = Entry(stockin, width=5, font=('Arial Rounded MT', 10), borderwidth=2,
             highlightcolor="black", justify="center", textvariable="mintxt")
Min_txt.create_window(10, 30, window=mins)
mins.place(relx=0.39, rely=0.765, anchor=NE)

# Insert Btn
insert_img = ImageTk.PhotoImage(Image.open("image/InsertBtn.png"))
InsertBtn = Button(stockin, image=insert_img, command=Insert)
InsertBtn.configure(bd=0, bg='#ffffff')
InsertBtn.place(relx=0.4, rely=0.85, anchor=NE)

# Logout Btn
Logout_img = ImageTk.PhotoImage(Image.open("image/LogoutBtn.png"))
LogoutBtn = Button(stockin, image=Logout_img, command=Logout)
LogoutBtn.configure(bd=0, bg='#ffffff')
LogoutBtn.place(relx=0.14, rely=0.85, anchor=NE)


# Instock table txt
instock_txt = Label(stockin, text='In Stock Table:')
instock_txt.configure(font=('Arial Rounded MT', 20), bg='#FFFFFF')
instock_txt.place(relx=0.6, anchor=NE)
# Instock table view
instock_tv = ttk.Treeview(stockin, columns=(1, 2, 3), show="headings", height=14)
instock_tv['columns'] = ('Date', 'Name', 'Time')
instock_tv.column('Date', anchor=CENTER, width=200)
instock_tv.column('Name', anchor=CENTER, width=200)
instock_tv.column('Time', anchor=CENTER, width=200)
# instock_tv.column(, width=0, stretch=NO)
instock_tv.heading(0, text="Date")
instock_tv.heading(1, text="Name")
instock_tv.heading(2, text="Time")




instock_tv.place(relx=0.88, rely=0.07, anchor=NE)

# Outstock table txt
outstock_txt = Label(stockin, text='Out Stock Table:')
outstock_txt.configure(font=('Arial Rounded MT', 20), bg='#FFFFFF')
outstock_txt.place(relx=0.62, rely=0.5, anchor=NE)
# outstock table view
outstock_tv = ttk.Treeview(stockin, columns=(1, 2, 3), show="headings", height=14)
outstock_tv['columns'] = ('Date', 'Name', 'Time')
outstock_tv.column('Date', anchor=CENTER, width=200)
outstock_tv.column('Name', anchor=CENTER, width=200)
outstock_tv.column('Time', anchor=CENTER, width=200)
outstock_tv.heading(0, text="Date")
outstock_tv.heading(1, text="Name")
outstock_tv.heading(2, text="Time")

rows, rows_out = stockcall(instock_tv , outstock_tv)

outstock_tv.place(relx=0.88, rely=0.55, anchor=NE)

# to run the window
stockin.state('zoomed')
stockin.mainloop()
