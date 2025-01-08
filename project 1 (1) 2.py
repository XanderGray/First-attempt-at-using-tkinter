from tkinter import *
from tkinter import ttk
import os
import time
#-------------------------------------- rooms view start


def pas():
    p.destroy()
    Password = password.get()
    password.destroy()
    file = open("NnP.txt","r")
    line = file.readline()
    data = line.split(" ")
    Found = False
    while line:
        data[1] = int(data[1])
        Password = int(Password)
        if data[1]-Password == 0 and Name == data[0]:
            Found = True
            line = file.readline()
            data = line.split(" ")
        else:
            line = file.readline()
            data = line.split(" ")
    file.close()        
    if Found == False:
        w = Canvas(Logon, width= 500, height= 20, bg="red")
        w.create_text(230, 10, text='Account nonexistant please try again by exiting the website', fill="black", font=('Helvetica 12 bold'))
        w.pack()
        
    else:
        global onefive
        global sixten
        global elevenfifteen
        global sixteentwenty
        global Viewrooms
        global Pur
        global Purchase
        top = Toplevel()
        top.title("Main page")
        my_notebook2 = ttk.Notebook(top)
        my_notebook2.pack(pady=15)
        
        Viewrooms = Frame(my_notebook2, width=500, height=500)
        Viewrooms.pack(fill="both", expand=1)
        my_notebook2.add(Viewrooms, text="View the rooms")
        
        onefive = Button(Viewrooms, text='View rooms 1 - 5', padx=50, pady=50,command = onefive, fg="black", bg="white")
        onefive.pack()
        sixten = Button(Viewrooms, text='View rooms 6 - 10', padx=50, pady=50,command = sixten, fg="black", bg="white")
        sixten.pack()
        elevenfifteen = Button(Viewrooms, text='View rooms 11 - 15', padx=50, pady=50,command = elevenfifteen, fg="black", bg="white")
        elevenfifteen.pack()
        sixteentwenty = Button(Viewrooms, text='View rooms 16 - 20', padx=50, pady=50,command = sixteentwenty, fg="black", bg="white")
        sixteentwenty.pack()
        
        Avaliable = Frame(my_notebook2, width=500, height=700)
        Avaliable.pack(fill="both", expand=1)
        my_notebook2.add(Avaliable, text="View room status")
        Rooms= Canvas(Avaliable, width= 400, height= 400, bg="SpringGreen2")
        file = open("Rooms.txt","r")
        line = file.readline()
        variable = ''
        while line:
            variable = variable+line
            line = file.readline()
        file.close
        Rooms.create_text(120, 200, text=variable, fill="black", font=('Helvetica 12 bold'))
        Rooms.pack()
        
        
        Purchase = Frame(my_notebook2, width=500, height=500)
        Purchase.pack(fill="both", expand=1)
        my_notebook2.add(Purchase, text="Proceed to purchase")
        
        Pur = Button(Purchase, text='Purchase room?', padx=50, pady=50,command = purchase, fg="black", bg="white")
        Pur.pack()
        
    
def purchase():
    global number
    global Buy
    Pur.destroy()
    number = Entry(Purchase, width=50)
    number.pack()
    number.insert(0,"Please enter the room number you want in the format Room[number]")
    Buy = Button(Purchase, text='Purchase room?', padx=50, pady=50,command = buy, fg="black", bg="white")
    Buy.pack()

def buy():
    global Number
    Number = number.get()
    Number = Number.title()
    number.destroy()
    test = (Number+":")
    file = open("Rooms.txt","r")
    line = file.readline()
    data = line.split(" ")
    roomfree = False
    while line:
        if data[0] == test and data[1] == "occupied\n":
            Buy.destroy()            
            Occ = Canvas(Purchase, width= 500, height= 20, bg="red")
            Occ.create_text(220, 10, text='Room occupied please try to book another by exiting the website', fill="black", font=('Helvetica 12 bold'))
            Occ.pack()
            roomfree = 'Checked'
        elif data[0] == test and data[1] == "unoccupied\n":
            roomfree = True
            
        line = file.readline()
        data = line.split(" ")
    file.close
    if roomfree == False:
            Buy.destroy()            
            Occ = Canvas(Purchase, width= 500, height= 20, bg="red")
            Occ.create_text(220, 10, text='Room unidentified please restart the website to try again', fill="black", font=('Helvetica 12 bold'))
            Occ.pack()
    
    elif roomfree == True:
        Buy.destroy()
        if Number == 'Room16' and Number == 'Room17' and Number == 'Room18' and Number == 'Room19' and Number == 'Room20':
            global price
            global Price
            Price = Canvas(Purchase, width= 500, height= 20, bg="red")
            Price.create_text(220, 10, text='Your nightly price is £100', fill="black", font=('Helvetica 12 bold'))
            Price.pack()
            price = 100
            fullcost()
            
            
        else:
            global luxury
            global Yes
            global No
            luxury = Canvas(Purchase, width= 500, height= 20, bg="red")
            luxury.create_text(220, 10, text='Would you like to pay an extra £30 per night for luxury service?', fill="black", font=('Helvetica 12 bold'))
            luxury.pack()
            Yes = Button(Purchase,padx = 50, pady = 50, text='yes', command = yes)
            Yes.pack()
            No = Button(Purchase, padx = 50, pady = 50, text='no', command = no)
            No.pack()
        
def yes():
    global price
    global Price
    global Full
    luxury.destroy()
    Yes.destroy()
    No.destroy()
    Price = Canvas(Purchase, width= 500, height= 20, bg="red")
    Price.create_text(220, 10, text='Your nightly price is £80', fill="black", font=('Helvetica 12 bold'))
    Price.pack()
    price = 80
    Full = Button(Purchase, padx = 50, pady = 50, text='Proceed', command = fullcost)
    Full.pack()
    
def no():
    global price
    global Price
    global Full
    luxury.destroy()
    Yes.destroy()
    No.destroy()
    Price = Canvas(Purchase, width= 500, height= 20, bg="red")
    Price.create_text(220, 10, text='Your nightly price is £50', fill="black", font=('Helvetica 12 bold'))
    Price.pack()
    price = 50
    Full = Button(Purchase, padx = 50, pady = 50, text='Proceed', command = fullcost)
    Full.pack()
    
def fullcost():
    global day
    global Confirm
    global p
    p = 0
    Price.destroy()
    Full.destroy()
    day = Entry(Purchase, width=50)
    day.pack()
    day.insert(0,"How many days are you staying?")
    Confirm = Button(Purchase, padx = 50, pady = 50, text='Confirm', command = days)
    Confirm.pack()

def days():
    global Days_Spent
    global p
    Days_Spent = day.get()
    if Days_Spent.isnumeric() == False and p == 0:        
            global ERROR
            ERROR = Canvas(Purchase, width= 500, height= 20, bg="red")
            ERROR.create_text(220, 10, text='Please enter numbers', fill="black", font=('Helvetica 12 bold'))
            ERROR.pack()
            p = 1
    
    elif Days_Spent.isnumeric() == False and p == 1:
            ERROR.destroy()
            ERROR = Canvas(Purchase, width= 500, height= 20, bg="red")
            ERROR.create_text(220, 10, text='Please enter numbers', fill="black", font=('Helvetica 12 bold'))
            ERROR.pack()
    
    else:
        fullcost2()
        
    
def fullcost2():
    global price
    global p
    global Days_Spent
    global FullPrice
    global digits
    global confirmation
    day.destroy()
    Confirm.destroy()
    if p == 1:
        ERROR.destroy()
    p == 0
    price = int(price)
    Days_Spent = int(Days_Spent)
    price = (price * Days_Spent)
    FullPrice = Canvas(Purchase, width= 500, height= 20, bg="red")
    FullPrice.create_text(220, 10, text=f'Your full price is £{price}', fill="black", font=('Helvetica 12 bold'))
    FullPrice.pack()
    digits = Entry(Purchase, width=50)
    digits.pack()
    digits.insert(0,"Please enter your 16 digit card number")
    confirmation = Button(Purchase, padx = 50, pady = 50, text = "Confirm", command = digitchecker)
    confirmation.pack()
    
def digitchecker():
    global p
    Digits = digits.get()
    if len(Digits) != 16 and p == 0:        
            global ERROr
            ERROr = Canvas(Purchase, width= 500, height= 20, bg="red")
            ERROr.create_text(220, 10, text='Invalid', fill="black", font=('Helvetica 12 bold'))
            ERROr.pack()
            p = 1
    
    elif len(Digits) != 16 and p == 1:
            ERROr.destroy()
            ERROr = Canvas(Purchase, width= 500, height= 20, bg="red")
            ERROr.create_text(220, 10, text='Invalid', fill="black", font=('Helvetica 12 bold'))
            ERROr.pack()
    
    else:
        fullcost3()
        
def fullcost3():
    global Security
    global confir
    global p
    FullPrice.destroy()
    digits.destroy()
    confirmation.destroy()
    if p == 1:
        ERROr.destroy()
    Security = Entry(Purchase, width=50)
    Security.pack()
    Security.insert(0,"Please enter your security number")
    confir = Button(Purchase, padx = 50, pady = 50, text = "Confirm", command = securitycheck)
    confir.pack()
    p = 0
    
def securitycheck():
    global p
    security = Security.get()
    if len(security) != 3 and p == 0:        
            global ERRor
            ERRor = Canvas(Purchase, width= 500, height= 20, bg="red")
            ERRor.create_text(220, 10, text='Invalid', fill="black", font=('Helvetica 12 bold'))
            ERRor.pack()
            p = 1
    
    elif len(security) != 16 and p == 1:
            ERRor.destroy()
            ERRor = Canvas(Purchase, width= 500, height= 20, bg="red")
            ERRor.create_text(220, 10, text='Invalid', fill="black", font=('Helvetica 12 bold'))
            ERRor.pack()
    
    else:
        FINAL()

def FINAL():
    global Number
    file = open("Rooms.txt","r")
    line = file.readline()
    data = line.split(": ")
    variable = ''
    while line:
        if data[0] == Number:
            sline = (Number + ": occupied"+"\n")
            variable = (variable+sline)
            line = file.readline()
            data = line.split(": ")
            
        else:
            variable = (variable+data[0]+": "+data[1])
            line = file.readline()
            data = line.split(": ")
    file.close()
    file = open("Rooms.txt","w")
    file.write(variable)
    file.close()
    Security.destroy()
    confir.destroy()
    FINISHED = Canvas(Purchase, width= 500, height= 20, bg="red")
    FINISHED.create_text(220, 10, text='Thank you for purchasing this room', fill="black", font=('Helvetica 12 bold'))
    FINISHED.pack()
            
    

        
    
def n():
    global p
    global password
    global Name
    nam.destroy()
    Name = name.get()
    Name = Name.title()
    name.destroy()
    file = open("NnP.txt","r")
    line = file.readline()
    data = line.split(" ")
    Found = False
    while line:
        if data[0] == Name:
            Found = True
            line = file.readline()
            data = line.split(" ")
        else:
            line = file.readline()
            data = line.split(" ")
    file.close
    if Found == False:
        w = Canvas(Logon, width= 500, height= 20, bg="red")
        w.create_text(220, 10, text='Name not found please try again by exiting the website', fill="black", font=('Helvetica 12 bold'))
        w.pack()
            
    else:
        password = Entry(Logon, width=50)
        password.pack()
        password.insert(0,"Please enter your password")
        p = Button(Logon, text='Submit name', padx=50, pady=50,command = pas, fg="black", bg="white")
        p.pack()
        
def onefive():
    onefive.destroy()
    t= Canvas(Viewrooms, width= 800, height= 100, bg="SpringGreen2")
    t.create_text(400, 10, text='Room 1- 1 bed, 1 tv,  1 bathroom', fill="black", font=('Helvetica 12 bold'))
    t.create_text(400, 30, text='Room 2- 1 bed, 1 tv,  1 bathroom', fill="black", font=('Helvetica 12 bold'))
    t.create_text(400, 50, text='Room 3- 2 beds, 1 tv, 1 bathroom', fill="black", font=('Helvetica 12 bold'))
    t.create_text(400, 70, text='Room 4- 1 bed, 1 tv, 1 bathroom with shower', fill="black", font=('Helvetica 12 bold'))
    t.create_text(400, 90, text='Room 5- 1 bed, 1 tv, 1 bathroom with shower', fill="black", font=('Helvetica 12 bold'))
    t.pack()
    
def sixten():
    sixten.destroy()
    u= Canvas(Viewrooms, width= 800, height= 100, bg="SpringGreen2")
    u.create_text(400, 10, text='Room 6- 2 beds, 2 tv,  1 bathroom', fill="black", font=('Helvetica 12 bold'))
    u.create_text(400, 30, text='Room 7- 1 bed, 1 tv,  1 bathroom, with shower', fill="black", font=('Helvetica 12 bold'))
    u.create_text(400, 50, text='Room 8- 3 beds, 1 tv, 1 bathroom', fill="black", font=('Helvetica 12 bold'))
    u.create_text(400, 70, text='Room 9- 1 bed, 1 tv, 1 bathroom', fill="black", font=('Helvetica 12 bold'))
    u.create_text(400, 90, text='Room 10- 2 beds, 1 tv, 1 bathroom with shower', fill="black", font=('Helvetica 12 bold'))
    u.pack()
    
def elevenfifteen():
    elevenfifteen.destroy()
    v= Canvas(Viewrooms, width= 800, height= 100, bg="SpringGreen2")
    v.create_text(400, 10, text='Room 11- 1 bed, 2 tvs, 1 bathroom', fill="black", font=('Helvetica 12 bold'))
    v.create_text(400, 30, text='Room 12- 2 beds, 1 tv,  1 bathroom', fill="black", font=('Helvetica 12 bold'))
    v.create_text(400, 50, text='Room 13- 1 bed, 1 tv, 1 bathroom', fill="black", font=('Helvetica 12 bold'))
    v.create_text(400, 70, text='Room 14- 1 bed, 1 tv, 1 bathroom', fill="black", font=('Helvetica 12 bold'))
    v.create_text(400, 90, text='Room 15- 1 bed, 1 tv, 1 bathroom with shower', fill="black", font=('Helvetica 12 bold'))
    v.pack()
    
def sixteentwenty():
    sixteentwenty.destroy()
    w= Canvas(Viewrooms, width= 800, height= 100, bg="SpringGreen2")
    w.create_text(450, 10, text='Room 16- 1 bed, 2 tvs, 1 bathroom with shower, required luxury service', fill="black", font=('Helvetica 12 bold'))
    w.create_text(450, 30, text='Room 17- 2 beds, 1 tv,  1 bathroom with shower, required luxury service', fill="black", font=('Helvetica 12 bold'))
    w.create_text(450, 50, text='Room 18- 1 bed, 1 tv, 1 bathroom with shower, required luxury service', fill="black", font=('Helvetica 12 bold'))
    w.create_text(450, 70, text='Room 19- 1 bed, 1 tv, 1 bathroom with shower, required luxury service', fill="black", font=('Helvetica 12 bold'))
    w.create_text(450, 90, text='Room 20- 2 beds, 1 tv, 2 bathrooms with shower, required luxury service', fill="black", font=('Helvetica 12 bold'))
    w.pack()
    
#---------------------------------------------------------------------------------------- rooms view end    
root = Tk()

my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=15)

CreateAccount = Frame(my_notebook, width=500, height=500)
CreateAccount.pack(fill="both", expand=1)

SignOut = Frame(my_notebook, width=500, height=500)
SignOut.pack(fill="both", expand=1)

Logon = Frame(my_notebook, width=500, height=500)
Logon.pack(fill="both", expand=1)

#the viewing rooms tab
my_notebook.add(Logon, text="Log on")
my_notebook.add(SignOut, text="Sign out")
my_notebook.add(CreateAccount, text="Create account")

name = Entry(Logon, width=50)
name.pack()
name.insert(0,"Please enter your name")

nam = Button(Logon, text='Submit name', padx=50, pady=50,command = n, fg="black", bg="white")
nam.pack()



    


my_menu = Menu(root)
root.config(menu=my_menu)


file_menu = Menu(my_menu)
my_menu.add_cascade(label="Escape", menu=file_menu)
file_menu.add_command(label="Exit website", command=root.quit)

#------------------------------------------------------------------------------- Room view menu

root.mainloop()