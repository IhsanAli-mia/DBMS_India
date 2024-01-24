#IMPORTING MODULES
import tkinter as tk
from tkinter import ttk, Menubutton,Menu,IntVar,Canvas,messagebox
import tkinter.font as tkf
import sqlite3
from PIL import ImageTk,Image 

#INITIALIZING CONNECTION
curse = sqlite3.connect('test.db')

cc = curse.execute("SELECT [Owner Name] FROM house_details WHERE [House Number] = 2")
for row in cc:
    print(row)

#OPENING WINDOW
home = tk.Tk()
home.title("Palli")
home.state('zoomed')


img = ImageTk.PhotoImage(Image.open("mosque.png"))  
panel = tk.Label(home, image = img)
panel.place(x = 400,y = 100)



def openHouse():
    global window
    window = tk.Toplevel()
    window.title("Palli")
    window.state('zoomed')
   
    global tv
    tv = ttk.Treeview(window,columns =('House No.','Owner Name','Address','Mahal No.','Phone No.','Whatsapp No.','Payment Due'),show='headings',height = 25)
    style = ttk.Style()
    vsb2 = ttk.Scrollbar(window, orient="vertical", command=tv.yview)
    vsb2.place(x=1340 ,y=100,height = 530)
    tv.configure(yscrollcommand=vsb2.set)
    style.configure("Treeview.Heading",font = ('Oswald',14))
    style.configure("Treeview.Column",font = ('Georgia',10))

    tv.column('#0', width=0, stretch="NO")
    tv.column('House No.', anchor="center", width=100)
    tv.column('Owner Name', anchor="center", width=200)
    tv.column('Address', anchor="center", width=300)
    tv.column('Mahal No.', anchor="center", width=200)
    tv.column('Phone No.', anchor="center", width=100)
    tv.column('Whatsapp No.', anchor="center", width=150)
    tv.column('Payment Due', anchor="center", width=150)

    tv.heading('#0', text='', anchor="center")
    tv.heading('House No.', text='House No.', anchor="center")
    tv.heading('Owner Name', text='Owner Name', anchor="center")
    tv.heading('Address', text='Address', anchor="center")
    tv.heading('Mahal No.', text='Mahal No.', anchor="center")
    tv.heading('Phone No.', text='Phone No.', anchor="center")
    tv.heading('Whatsapp No.', text='Whatsapp No.', anchor="center")
    tv.heading('Payment Due', text='Payment Due', anchor="center")

    cc = curse.execute("SELECT * FROM house_details")
    c = 0 
    for i in cc:
        print(i)
        tv.insert(parent='', index=c, iid=c, text='', values= (i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        c = c + 1

    tv.place(x = 150,y = 100)

    tv.bind("<ButtonRelease-1>",select)
    tv.bind("<Control-c>",copy)    

    add = tk.Button(
	    window,
	    text = "Add House",
    	command = addHouse,
        font =("Tahoma",12,'bold'),
        bg='#00AB66'
	    )
    add.place(x = 120,y = 750,anchor = "center")

    edi = tk.Button(
	    window,
	    text = "Edit House",
	    command = edithou,
        font =("Tahoma",12,'bold'),
        bg='#00AB66'
	    )
    edi.place(x = 400,y = 750,anchor = "center")

    ser = tk.Button(
	    window,
	    text = "Search Name",
	    command = searchName,
        font =("Tahoma",12,'bold'),
        bg='#00AB66'
	    )
    ser.place(x = 710,y = 750,anchor = "center")

    res = tk.Button(
	    window,
	    text = "Refresh",
	    command = refresh3,
        font =("Tahoma",12,'bold'),
        bg='#00AB66'
	    )
    res.place(x = 960,y = 750,anchor = "center")


    pai = tk.Button(
	    window,
	    text = "Update Payment",
	    command = paid,
        font =("Tahoma",12,'bold'),
        bg='#00AB66'
	    )
    pai.place(x = 1170,y = 750,anchor = "center")

    refa = tk.Button(
	    window,
	    text = "Delete",
	    command = delete1,
        font =("Tahoma",12,'bold'),
        bg='#00AB66'
	    )
    refa.place(x = 1370,y = 750,anchor = "center")

    



    window.mainloop()

def openFamily():
    global window1
    window1= tk.Toplevel()
    window1.title("Palli")
    window1.state('zoomed')
   
    global tv2
    tv2= ttk.Treeview(window1,columns =('SNo','Name','Gender','Owner of House','Relation to Owner','Age','Date of Birth','Occupation','Salary'),show='headings',height =25)
    vsb1 = ttk.Scrollbar(window1, orient="vertical", command=tv2.yview)
    vsb1.place(x=1419 ,y=130,height = 500)
    tv2.configure(yscrollcommand=vsb1.set)
#style = ttk.Style()
#style.configure("Treeview.Heading",font = (None,100))

    tv2.column('#0', width=0, stretch="NO")
    tv2.column('SNo', anchor="center", width=100)
    tv2.column('Name', anchor="center", width=200)
    tv2.column('Gender', anchor="center", width=150)
    tv2.column('Owner of House', anchor="center", width=200)
    tv2.column('Relation to Owner', anchor="center", width=150)
    tv2.column('Age', anchor="center", width=100)
    tv2.column('Date of Birth', anchor="center", width=150)
    tv2.column('Occupation', anchor="center", width=150)
    tv2.column('Salary', anchor="center", width=150)

    tv2.heading('#0', text='', anchor="center")
    tv2.heading('SNo', text='SNo', anchor="center")
    tv2.heading('Name', text='Name', anchor="center")
    tv2.heading('Gender', text='Gender', anchor="center")
    tv2.heading('Owner of House', text='Owner of House', anchor="center")
    tv2.heading('Relation to Owner', text='Relation to Owner', anchor="center")
    tv2.heading('Age', text='Age', anchor="center")
    tv2.heading('Date of Birth', text='Date of Birth', anchor="center")
    tv2.heading('Occupation', text='Occupation', anchor="center")
    tv2.heading('Salary', text='Salary', anchor="center")

    cc = curse.execute("SELECT * FROM family_details ORDER BY CAST(S_No AS INT)")
    d = 0 
    for fj in cc:
        print(fj)
        tv2.insert(parent='', index=d, iid=d, text='', values= (fj[0],fj[1],fj[2],fj[3],fj[4],fj[5],fj[6],fj[7],fj[8]))
        d = d + 1
    tv2.place(x = 85,y = 100)
    

    m10 = Menubutton(
        window1,
        text = "SNo",
        width = 10,
        anchor = "center",
        font =("Oswald",12,'bold'),
        bg = '#99FF99'
    )
    m10.place(x = 85,y = 100)

    m20 = Menubutton(
        window1,
        text = "Name",
        width = 20,
        anchor = "center",
        font =("Oswald",12,'bold'),
        bg = '#99FF99'
    )
    m20.place(x = 180,y = 100)

    m30 = Menubutton(
        window1,
        text = "Gender",
        width = 22,
        anchor = "center",
        font =("Oswald",12,'bold'),
        bg = '#99FF99'
    )
    m30.menu = Menu(m30,tearoff =0)
    m30["menu"]=m30.menu
    m30.menu.add_checkbutton(label="Male",command = male1)
    m30.menu.add_checkbutton(label="Female",command = female1)
    m30.place(x = 340,y = 100)

    m40 = Menubutton(
        window1,
        text = "Owner of House",
        width = 14,
        anchor = "center",
        font =("Oswald",12,'bold'),
        bg = '#99FF99'
    )
    m40.place(x = 545,y=100)

    m50 = Menubutton(
        window1,
        text = "Relation to Owner",
        width = 23,
        anchor = "center",
        font =("Oswald",12,'bold'),
        bg = '#99FF99'
    )
    m50.place(x = 680,y=100)

    m60 = Menubutton(
        window1,
        text = "Age",
        width = 12,
        anchor = "center",
        font =("Oswald",12,'bold'),
        bg = '#99FF99'
    )
    m60.menu = Menu(m60,tearoff =0)
    m60["menu"]=m60.menu
    m60.menu.add_radiobutton(label="14-18",command = age10)
    m60.place(x=875,y=100)
    
    m70 = Menubutton(
        window1,
        text = "Date of Birth",
        width = 15,
        anchor = "center",
        font =("Oswald",12,'bold'),
        bg = '#99FF99'
    )
    m70.place(x = 980,y=100)

   
    m80 = Menubutton(
        window1,
        text = "Occupation",
        width = 18,
        anchor = "center",
        font =("Oswald",12,'bold'),
        bg = '#99FF99'
    )
    m80.menu = Menu(m80,tearoff =0)
    m80["menu"]=m80.menu
  # m8.menu.add_radiobutton(label="",command = student,value = 2,variable = sui)
    m80.menu.add_radiobutton(label="Student",command = student1)
    m80.place(x = 1120,y = 100)

    m90 = Menubutton(
        window1,
        text = "Salary",
        width = 16,
        anchor = "center",
        font =("Oswald",12,'bold'),
        bg = '#99FF99'
    )
    m90.place(x = 1280,y = 100)


    addfa = tk.Button(
	    window1,
	    text = "Add Family",
    	command = af,
        font =("Tahoma",12,'bold'),
        bg='#00AB66'
     )
    addfa.place(x = 170,y = 750,anchor = "center")

    edifa = tk.Button(
	    window1,
	    text = "Edit Family",
	    command = editFamily1,
        font =("Tahoma",12,'bold'),
        bg='#00AB66'
        )
    edifa.place(x = 470,y=750,anchor = "center")

    serfa = tk.Button(
	    window1,
	    text = "Search Name",
	    command = searchName2,
        font =("Tahoma",12,'bold'),
        bg='#00AB66'
	    )
    serfa.place(x = 770,y=750,anchor = "center")

    refa = tk.Button(
	    window1,
	    text = "Refresh",
	    command = refresh1,
        font =("Tahoma",12,'bold'),
        bg='#00AB66'
	    )
    refa.place(x = 1070,y=750,anchor = "center")

    defa = tk.Button(
	    window1,
	    text = "Delete",
	    command = delete,
        font =("Tahoma",12,'bold'),
        bg='#00AB66'
	    )
    defa.place(x = 1370,y=750,anchor = "center")

    window1.mainloop()


def death():
    global dea
    dea = tk.Toplevel()
    dea.title("Palli")
    dea.state('zoomed')
   
    global tv3
    tv3 = ttk.Treeview(dea,columns =('S No','Name','Date of Death','Place of Death','Reason of Death'),show='headings',height = 25)
    style3 = ttk.Style()
    vsb3 = ttk.Scrollbar(dea, orient="vertical", command=tv3.yview)
    vsb3.place(x=1290 ,y=100,height = 530)
    tv3.configure(yscrollcommand=vsb3.set)
    style3.configure("Treeview.Heading",font = ('Oswald',14))
    style3.configure("Treeview.Column",font = ('Georgia',10))

    tv3.column('#0', width=0, stretch="NO")
    tv3.column('S No', anchor="center", width=50)
    tv3.column('Name', anchor="center", width=250)
    tv3.column('Date of Death', anchor="center", width=150)
    tv3.column('Place of Death', anchor="center", width=300)
    tv3.column('Reason of Death', anchor="center", width=300)

    tv3.heading('#0', text='', anchor="center")
    tv3.heading('S No', text='S No', anchor="center")
    tv3.heading('Name', text='Name', anchor="center")
    tv3.heading('Date of Death', text='Date of Death', anchor="center")
    tv3.heading('Place of Death', text='Place of Death', anchor="center")
    tv3.heading('Reason of Death', text='Reason of Death', anchor="center")
    
    cc = curse.execute("SELECT * FROM death_details")
    c = 0 
    for i in cc:
        print(i)
        tv3.insert(parent='', index=c, iid=c, text='', values= (i[0],i[1],i[2],i[3],i[4]))
        c = c + 1

    tv3.place(x = 250,y = 100)

    ddd = tk.Button(
	    dea,
	    text = "Add Entry",
    	command = adddeath,
        font =("Tahoma",12,'bold'),
        bg='#00AB66'
	    )
    ddd.place(x = 170,y = 750,anchor = "center")

    edd = tk.Button(
	    dea,
	    text = "Edit Entry",
	    command = editdeath,
        font =("Tahoma",12,'bold'),
        bg='#00AB66'
	    )
    edd.place(x = 470,y = 750,anchor = "center")

    sed = tk.Button(
	    dea,
	    text = "Search Name",
	    command = searchdeath,
        font =("Tahoma",12,'bold'),
        bg='#00AB66'
	    )
    sed.place(x = 770,y = 750,anchor = "center")

    red = tk.Button(
	    dea,
	    text = "Refresh",
	    command = refresh2,
        font =("Tahoma",12,'bold'),
        bg='#00AB66'
	    )
    red.place(x = 1070,y = 750,anchor = "center")

    reda = tk.Button(
	    dea,
	    text = "Delete",
	    command = delete3,
        font =("Tahoma",12,'bold'),
        bg='#00AB66'
	    )
    reda.place(x = 1370,y = 750,anchor = "center")

hou = tk.Button(
    home,
    text = "Open Houses",
    command = openHouse,
    font =("Tahoma",12,'bold'),
    bg='#00AB66'
    )
hou.place(x = 450,y=800,anchor = "center")

fou = tk.Button(
    home,
    text = "Open Family",
    command = openFamily,
    font =("Tahoma",12,'bold'),
    bg='#00AB66'
    )
fou.place(x = 750,y = 800,anchor = "center")

fod = tk.Button(
    home,
    text = "Death Roll",
    command = death,
    font =("Tahoma",12,'bold'),
    bg='#00AB66'
    )
fod.place(x = 1050,y = 800,anchor = "center")


#DEFINING FUNCTION
def nothing(w):
    pass

def addHouse():
    mahal = tk.Toplevel()
    mahal.title("Palli")
    mahal.geometry('350x332')

    fonta =tkf.Font(family = "Oswald",size = 14)

    ownername = tk.Text(
        mahal,
        height = 1,
        width = 30
    )
    ownername.grid(row = 0,column = 1)
    lbl1 = tk.Label(
        mahal,
        text="Owner Name",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbl1.grid(row = 0,column = 0)

    panchayatnumber = tk.Text(
        mahal,
        height = 1,
        width = 30
    )
    panchayatnumber.grid(row = 1,column = 1)
    lbl2 = tk.Label(
        mahal,
        text="Panchayat No.",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbl2.grid(row = 1,column = 0)

    address = tk.Text(
        mahal,
        height = 3,
        width = 30
    )
    address.grid(row = 2,column = 1)
    lbl3 = tk.Label(
        mahal,
        text="Address",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbl3.grid(row = 2,column = 0)

    phonenumber = tk.Text(
        mahal,
        height = 1,
        width = 30
    )
    phonenumber.grid(row = 3,column = 1)
    lbl4 = tk.Label(
        mahal,
        text="Phone No.",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbl4.grid(row = 3,column = 0)

    whatsappnumber = tk.Text(
        mahal,
        height = 1,
        width = 30
    )
    whatsappnumber.grid(row = 4,column = 1)
    lbl5 = tk.Label(
        mahal,
        text="WhatsApp No.",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbl5.grid(row = 4,column = 0)

    gender = tk.Text(
        mahal,
        height = 1,
        width = 30
    )
    gender.grid(row = 5,column = 1)
    lbl6 = tk.Label(
        mahal,
        text="Gender",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbl6.grid(row = 5,column = 0)

    age = tk.Text(
        mahal,
        height = 1,
        width = 30
    )
    age.grid(row = 6,column = 1)
    lbl7 = tk.Label(
        mahal,
        text="Age",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbl7.grid(row = 6,column = 0)

    dateOfBirth = tk.Text(
        mahal,
        height = 1,
        width = 30
    )
    dateOfBirth.grid(row = 7,column = 1)
    lbl8 = tk.Label(
        mahal,
        text="Date of Birth",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbl8.grid(row = 7,column = 0)

    occupation = tk.Text(
        mahal,
        height = 1,
        width = 30
    )
    occupation.grid(row = 8,column = 1)
    lbl9 = tk.Label(
        mahal,
        text="Profession",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbl9.grid(row = 8,column = 0)
    
    salary = tk.Text(
        mahal,
        height = 1,
        width = 30
    )
    salary.grid(row = 9,column = 1)
    lbl10 = tk.Label(
        mahal,
        text="Salary",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbl10.grid(row = 9,column = 0)
    paym = tk.Text(
        mahal,
        height = 1,
        width = 30
    )
    paym.grid(row = 10,column = 1)
    lbl1e = tk.Label(
        mahal,
        text="Payment Due",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbl1e.grid(row = 10,column = 0)
    

    aount = 0
    bount = 0
    
    ccc = curse.execute('SELECT COUNT(*) AS RowCnt FROM house_details')
    for dou in ccc:
        sount = int(dou[0])
        print(sount)

    if sount > 0:
        cc = curse.execute("SELECT * FROM house_details ORDER BY [House Number] DESC LIMIT 1")

        for hou in cc:
            aount = hou[0]
            aiount = int(aount)+ 1
            print(aiount)
    else:
        aiount = 1

    ccc = curse.execute('SELECT COUNT(*) AS RowCnt FROM family_details')
    for dou in ccc:
        sount = int(dou[0])
        print(sount)

    if sount > 0:
        cc = curse.execute("SELECT * FROM family_details ORDER BY CAST(S_No AS INT) DESC LIMIT 1")

        for hou in cc:
            bount = hou[0]
            biount = int(bount)+ 1
            print(biount)
    else:
        biount = 1


    
    def enter():
        ownername1=ownername.get("1.0",'end-1c')
        dateOfBirth1=dateOfBirth.get("1.0",'end-1c')
        panchayatnumber1=panchayatnumber.get("1.0",'end-1c')
        salary1=salary.get("1.0",'end-1c')
        occupation1=occupation.get("1.0",'end-1c')
        age1=age.get("1.0",'end-1c')
        whatsappnumber1=whatsappnumber.get("1.0",'end-1c')
        phonenumber1=phonenumber.get("1.0",'end-1c')
        gender1=gender.get("1.0",'end-1c')
        address1= address.get("1.0",'end-1c')
        self1="Self"
        paym1 = paym.get("1.0",'end-1c')
        print(aount,ownername1,address1,panchayatnumber1,phonenumber1,whatsappnumber1)
        curse.execute("INSERT INTO house_details VALUES (?,?,?,?,?,?,?)",(aiount,ownername1,address1,panchayatnumber1,phonenumber1,whatsappnumber1,paym1))
        curse.commit()
        curse.execute("INSERT INTO family_details VALUES (?,?,?,?,?,?,?,?,?)",(biount,ownername1,gender1,ownername1,self1,age1,dateOfBirth1,occupation1,salary1))
        curse.commit()
        mahal.destroy()
        tv.delete(*tv.get_children())
        cc = curse.execute("SELECT * FROM house_details")
        d = 0
        for ad in cc:
            tv.insert(parent='', index=d, iid=d, text='', values= (ad[0],ad[1],ad[2],ad[3],ad[4],ad[5],ad[6]))
            d = d + 1

    aDd = tk.Button(mahal,text = 'ADD HOUSE',command = enter,font =("Tahoma",12,'bold'),bg='#00AB66')
    aDd.grid(row = 11,column = 1)
    
    mahal.mainloop()

def paid():
    global smo
    smo = tk.Label(
        window,
        text = "Select the member you wish to update payment of",
        font =("Oswald",20,'bold')
    )
    smo.place(x=500 ,y = 25)
    tv.bind("<ButtonRelease-1>",select10)

def adddeath():
    maha = tk.Toplevel()
    maha.title("Palli")
    maha.geometry('350x306')


    name = tk.Text(
        maha,
        height = 1,
        width = 30
    )
    name.grid(row = 0,column = 1)
    lbn1 = tk.Label(
        maha,
        text="Name",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbn1.grid(row = 0,column = 0)

    dodo = tk.Text(
        maha,
        height = 1,
        width = 30
    )
    dodo.grid(row = 1,column = 1)
    lbn2 = tk.Label(
        maha,
        text="Date of Death",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbn2.grid(row = 1,column = 0)

    ploda = tk.Text(
        maha,
        height = 3,
        width = 30
    )
    ploda.grid(row = 2,column = 1)
    lbn3 = tk.Label(
        maha,
        text="Place of Death",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbn3.grid(row = 2,column = 0)

    roda = tk.Text(
        maha,
        height = 1,
        width = 30
    )
    roda.grid(row = 3,column = 1)
    lbn4 = tk.Label(
        maha,
        text="Reason of Death",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbn4.grid(row = 3,column = 0)

    aount = 0
    bount = 0

    ccc = curse.execute('SELECT COUNT(*) AS RowCnt FROM death_details')
    for dou in ccc:
        sount = int(dou[0])
        print(sount)

    if sount > 0:
        cc = curse.execute("SELECT * FROM death_details ORDER BY [S No] DESC LIMIT 1")

        for hou in cc:
            aount = hou[0]
            aiount = int(aount)+ 1
            print(aiount)
    else:
        aiount = 1
    def enter():
        name1=name.get("1.0",'end-1c')
        dodo1=dodo.get("1.0",'end-1c')
        ploda1=ploda.get("1.0",'end-1c')
        roda1=roda.get("1.0",'end-1c')
        curse.execute("INSERT INTO death_details VALUES (?,?,?,?,?)",(aiount,name1,dodo1,ploda1,roda1))
        curse.commit()
        maha.destroy()
        tv3.delete(*tv3.get_children())
        cc = curse.execute("SELECT * FROM death_details")
        d = 0
        for ad in cc:
            tv3.insert(parent='', index=d, iid=d, text='', values= (ad[0],ad[1],ad[2],ad[3],ad[4]))
            d = d + 1

    aDdd = tk.Button(maha,text = 'ADD ENTRY',command = enter,font =("Tahoma",12,'bold'),bg='#00AB66')
    aDdd.grid(row = 10,column = 1)
    
    maha.mainloop()


def edithou():
    global querh
    querh = tk.Label(
        window,
        text = "Select the house you wish to edit",
        font =("Oswald",20,'bold')
    )
    querh.place(x=540 ,y = 25)
    tv.bind("<ButtonRelease-1>",select3)

def editHouse():
    mosque = tk.Toplevel()
    mosque.title("Palli")
    mosque.geometry('350x206')

    tv.bind("<ButtonRelease-1>",select)

    ownername0 = tk.Text(
        mosque,
        height = 1,
        width = 30
    )
    ownername0.grid(row = 1,column = 1)
    lbl01 = tk.Label(
        mosque,
        text="Owner Name",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbl01.grid(row = 1,column = 0)

    panchayatnumber0 = tk.Text(
        mosque,
        height = 1,
        width = 30
    )
    panchayatnumber0.grid(row = 2,column = 1)
    lbl02 = tk.Label(
        mosque,
        text="Panchayat No.",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbl02.grid(row = 2,column = 0)

    address0 = tk.Text(
        mosque,
        height = 1,
        width = 30
    )
    address0.grid(row = 3,column = 1)
    lbl03 = tk.Label(
        mosque,
        text="Address",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbl03.grid(row = 3,column = 0)
    
    phonenumber0 = tk.Text(
        mosque,
        height = 1,
        width = 30
    )
    phonenumber0.grid(row = 4,column = 1)
    lbl04 = tk.Label(
        mosque,
        text="Phone No.",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbl04.grid(row = 4,column = 0)

    whatsappnumber0 = tk.Text(
        mosque,
        height = 1,   
        width = 30
    )
    whatsappnumber0.grid(row = 5,column = 1)
    lbl05 = tk.Label(
        mosque,
        text="WhatsApp No.",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbl05.grid(row = 5,column = 0)
    
    def enter1():
        ownername1=ownername0.get("1.0",'end-1c')
        panchayatnumber1=panchayatnumber0.get("1.0",'end-1c')
        whatsappnumber1=whatsappnumber0.get("1.0",'end-1c')
        phonenumber1=phonenumber0.get("1.0",'end-1c')
        address1=address0.get("1.0",'end-1c')

        curse.execute("UPDATE house_details SET [Owner Name]=(?),Address=(?),[Panchayat Number]=(?),[Phone Number]=(?),[Whatsapp Number]=(?)  WHERE [House Number] = (?);",(ownername1,address1,panchayatnumber1,phonenumber1,whatsappnumber1,joooo))
        curse.commit()
        curse.execute("UPDATE family_details SET [Owner of House]=(?) WHERE [Owner of House] = (?);",(ownername1,aaaa))
        curse.commit()
        curse.execute("UPDATE family_details SET Name=(?) WHERE [Owner of House] = (?) AND [Relation to Owner] = 'Self';",(ownername1,aaaa))
        curse.commit()
        mosque.destroy()
        tv.delete(*tv.get_children())
        cc = curse.execute("SELECT * FROM house_details")
        d = 0
        for ade in cc:
            tv.insert(parent='', index=d, iid=d, text='', values= (ade[0],ade[1],ade[2],ade[3],ade[4],ade[5],ade[6]))
            d = d + 1

    aDde = tk.Button(mosque,text = 'Edit House',command = enter1,font =("Tahoma",12,'bold'),bg='#00AB66')
    aDde.grid(row = 6,column = 1)

    mosque.mainloop()    

def editdeath():
    global dquer
    dquer = tk.Label(
        dea,
        text = "Select the entry you wish to edit",
        font =("Oswald",20,'bold')
        )
    dquer.place(x=600,y=25)
    tv3.bind("<ButtonRelease-1>",select8)

def editdeathh():
    maha1 = tk.Toplevel()
    maha1.title("Palli")
    maha1.geometry('350x306')

    tv3.bind("<ButtonRelease-1>",nothing)

    named = tk.Text(
        maha1,
        height = 1,
        width = 30
    )
    named.grid(row = 0,column = 1)
    lbn11 = tk.Label(
        maha1,
        text="Name",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbn11.grid(row = 0,column = 0)

    dodod = tk.Text(
        maha1,
        height = 1,
        width = 30
    )
    dodod.grid(row = 1,column = 1)
    lbn21 = tk.Label(
        maha1,
        text="Date of Death",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbn21.grid(row = 1,column = 0)

    plodad = tk.Text(
        maha1,
        height = 3,
        width = 30
    )
    plodad.grid(row = 2,column = 1)
    lbn31 = tk.Label(
        maha1,
        text="Place of Death",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbn31.grid(row = 2,column = 0)

    rodad = tk.Text(
        maha1,
        height = 1,
        width = 30
    )
    rodad.grid(row = 3,column = 1)
    lbn41 = tk.Label(
        maha1,
        text="Reason of Death",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbn41.grid(row = 3,column = 0)

   
    def enter():
        named1=named.get("1.0",'end-1c')
        dodod1=dodod.get("1.0",'end-1c')
        plodad1=plodad.get("1.0",'end-1c')
        rodad1=rodad.get("1.0",'end-1c')
        curse.execute("UPDATE death_details SET Name=(?),[Date of Death]=(?),[Place of Death]=(?),[Reason of Death]=(?) WHERE [S No] = (?);",(named1,dodod1,plodad1,rodad1,aaaaaa))
        curse.commit()
        maha1.destroy()
        tv3.delete(*tv3.get_children())
        cc = curse.execute("SELECT * FROM death_details")
        d = 0
        for ad in cc:
            tv3.insert(parent='', index=d, iid=d, text='', values= (ad[0],ad[1],ad[2],ad[3],ad[4]))
            d = d + 1

    aDde = tk.Button(maha1,text = 'EDIT ENTRY',command = enter,font =("Tahoma",12,'bold'),bg='#00AB66')
    aDde.grid(row = 10,column = 1)
    
    maha1.mainloop()

def editFamily():
    global quer
    quer = tk.Label(
        fam,
        text = "Select the member you wish to edit",
        font =("Oswald",20,'bold')
    )
    quer.place(x=550 ,y = 25)
    tv1.bind("<ButtonRelease-1>",select1)

def editfamilyy():
    queq = tk.Toplevel()
    queq.title("Palli")
    queq.geometry("450x306")

    namequeq = tk.Text(
        queq,
        height = 1,
        width = 45
    )
    namequeq.grid(row = 0,column = 1)
    lblnqq = tk.Label(
        queq,
        text="Name of Member",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lblnqq.grid(row = 0,column = 0)

    gendqueq = tk.Text(
        queq,
        height = 1,
        width = 45

    )
    gendqueq.grid(row = 1,column = 1)
    lblgqq = tk.Label(
        queq,
        text="Gender",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lblgqq.grid(row = 1,column = 0)

    relaqueq = tk.Text(
        queq,
        height = 1,
        width = 45
    )
    relaqueq.grid(row = 2,column = 1)
    lblrqq = tk.Label(
        queq,
        text="Relation to Owner",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lblrqq.grid(row = 2,column = 0)

    agequeq = tk.Text(
        queq,
        height = 1,
        width = 45
    )
    agequeq.grid(row = 3,column = 1)
    lblaqq = tk.Label(
        queq,
        text="Age",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lblaqq.grid(row = 3,column = 0)

    datequeq = tk.Text(
        queq,
        height = 1,
        width = 45
    )
    datequeq.grid(row = 4,column = 1)
    lbldqq = tk.Label(
        queq,
        text="Date of Birth",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbldqq.grid(row = 4,column = 0)

    occuqueq = tk.Text(
        queq,
        height = 1,
        width = 45
    )
    occuqueq.grid(row = 5,column = 1)
    lbloqq = tk.Label(
        queq,
        text="Profession",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbloqq.grid(row = 5,column = 0)

    salaqueq = tk.Text(
        queq,
        height = 1,
        width = 45
    )
    salaqueq.grid(row = 6,column = 1)
    lblsqq = tk.Label(
        queq,
        text="Salary",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lblsqq.grid(row = 6,column = 0)

    tv1.bind("<ButtonRelease-1>",nothing)
    
    def enqq():
        namequeq1=namequeq.get("1.0",'end-1c')
        gendqueq1=gendqueq.get("1.0",'end-1c')
        relaqueq1=relaqueq.get("1.0",'end-1c')
        agequeq1=agequeq.get("1.0",'end-1c')
        datequeq1=datequeq.get("1.0",'end-1c')
        occuqueq1=occuqueq.get("1.0",'end-1c')
        salaqueq1=salaqueq.get("1.0",'end-1c')

        curse.execute("UPDATE family_details SET Name=(?), Gender =(?), [Relation to Owner]=(?), Age = (?), [Date of Birth] =(?), Occupation =(?), Salary=(?)  WHERE [Owner of House] = (?) AND Name = (?);",(namequeq1,gendqueq1,relaqueq1,agequeq1,datequeq1,occuqueq1,salaqueq1,joos,aa))
        curse.commit()
        
        queq.destroy()
        tv1.delete(*tv1.get_children())
        d = 0
        cc = curse.execute("SELECT * FROM family_details WHERE [Owner of House] = %s ORDER BY CAST(S_No AS INT)"%a)
        for cuqq in cc:
            tv1.insert(parent='', index=d, iid=d, text='', values= (cuqq[0],cuqq[1],cuqq[2],cuqq[3],cuqq[4],cuqq[5],cuqq[6],cuqq[7],cuqq[8]))
            d = d + 1

        


    aqdq = tk.Button(queq,text = 'EDIT MEMBER',command = enqq,font =("Tahoma",12,'bold'),bg='#00AB66')
    aqdq.grid(row = 7,column = 1)

    queq.mainloop()
    
def editFamily1():
    global smol
    smol = tk.Label(
        window1,
        text = "Select the member you wish to edit",
        font =("Oswald",20,'bold')
    )
    smol.place(x=500 ,y = 25)
    tv2.bind("<ButtonRelease-1>",select2)

def editfamilyy1():
    queqf = tk.Toplevel()
    queqf.title("Palli")
    queqf.geometry("450x306")

    namequeqf = tk.Text(
        queqf,
        height = 1,
        width = 45
    )
    namequeqf.grid(row = 0,column = 1)
    lblnqqf = tk.Label(
        queqf,
        text="Name of Member  ",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lblnqqf.grid(row = 0,column = 0)

    gendqueqf = tk.Text(
        queqf,
        height = 1,
        width = 45

    )
    gendqueqf.grid(row = 1,column = 1)
    lblgqqf = tk.Label(
        queqf,
        text="Gender  ",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lblgqqf.grid(row = 1,column = 0)

    relaqueqf = tk.Text(
        queqf,
        height = 1,
        width = 45
    )
    relaqueqf.grid(row = 2,column = 1)
    lblrqqf = tk.Label(
        queqf,
        text="Relation to Owner",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lblrqqf.grid(row = 2,column = 0)

    agequeqf = tk.Text(
        queqf,
        height = 1,
        width = 45
    )
    agequeqf.grid(row = 3,column = 1)
    lblaqqf = tk.Label(
        queqf,
        text="Age  ",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lblaqqf.grid(row = 3,column = 0)

    datequeqf = tk.Text(
        queqf,
        height = 1,
        width = 45
    )
    datequeqf.grid(row = 4,column = 1)
    lbldqqf = tk.Label(
        queqf,
        text="Date of Birth  ",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbldqqf.grid(row = 4,column = 0)

    occuqueqf = tk.Text(
        queqf,
        height = 1,
        width = 45
    )
    occuqueqf.grid(row = 5,column = 1)
    lbloqqf = tk.Label(
        queqf,
        text="Profession  ",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbloqqf.grid(row = 5,column = 0)

    salaqueqf = tk.Text(
        queqf,
        height = 1,
        width = 45
    )
    salaqueqf.grid(row = 6,column = 1)
    lblsqqf = tk.Label(
        queqf,
        text="Salary  ",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lblsqqf.grid(row = 6,column = 0)

    tv2.bind("<ButtonRelease-1>",nothing)

    def enqqf():
        namequeqf1=namequeqf.get("1.0",'end-1c')
        gendqueqf1=gendqueqf.get("1.0",'end-1c')
        relaqueqf1=relaqueqf.get("1.0",'end-1c')
        agequeqf1=agequeqf.get("1.0",'end-1c')
        datequeqf1=datequeqf.get("1.0",'end-1c')
        occuqueqf1=occuqueqf.get("1.0",'end-1c')
        salaqueqf1=salaqueqf.get("1.0",'end-1c')

        curse.execute("UPDATE family_details SET Name=(?), Gender =(?), [Relation to Owner]=(?), Age = (?), [Date of Birth] =(?), Occupation =(?), Salary=(?)  WHERE [Owner of House] = (?) AND Name = (?);",(namequeqf1,gendqueqf1,relaqueqf1,agequeqf1,datequeqf1,occuqueqf1,salaqueqf1,jooo,aaa))
        curse.commit()
        
        queqf.destroy()
        tv2.delete(*tv2.get_children())
        d = 0
        cc = curse.execute("SELECT * FROM family_details ORDER BY CAST(S_No AS INT)")
        for cuqqf in cc:
            tv2.insert(parent='', index=d, iid=d, text='', values= (cuqqf[0],cuqqf[1],cuqqf[2],cuqqf[3],cuqqf[4],cuqqf[5],cuqqf[6],cuqqf[7],cuqqf[8]))
            d = d + 1
    aqdqf = tk.Button(queqf,text = 'EDIT MEMBER',command = enqqf,font =("Tahoma",12,'bold'),bg='#00AB66')
    aqdqf.grid(row = 7,column = 1)

    queqf.mainloop()

def searchName():
    searchn = tk.Toplevel()
    searchn.title("Palli")
    searchn.geometry("550x100")

    searchhouse = tk.Text(
        searchn,
        width = 45,
        height = 1
    )
    searchhouse.grid(row = 0,column = 1)
    lbls = tk.Label(
        searchn,
        text="Search Name Here",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbls.grid(row = 0,column = 0)

    def search():
        se ="\'"+searchhouse.get("1.0",'end-1c')  +"\'"
        searchn.destroy()
        tv.delete(*tv.get_children())
        cc = curse.execute("SELECT * FROM house_details WHERE [Owner Name] = %s"%se)
        d = 0
        for ss in cc:
            tv.insert(parent='', index=d, iid=d, text='', values= (ss[0],ss[1],ss[2],ss[3],ss[4],ss[5],ss[6]))
            d = d + 1

    buts = tk.Button(searchn,text = 'SEARCH',command = search,font =("Tahoma",12,'bold'),bg='#00AB66')
    buts.grid(row = 3,column = 1)

    searchn.mainloop()

def searchName2():
    searchf1 = tk.Toplevel()
    searchf1.title("Palli")
    searchf1.geometry("550x100")

    searchhouse11= tk.Text(
        searchf1,
        width = 45,
        height = 1
    )
    searchhouse11.grid(row = 0,column= 1)
    lblf1 = tk.Label(
        searchf1,
        text="Search Name Here",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lblf1.grid(row = 0,column= 0)

    def search11():
        sf1 ="\'"+searchhouse11.get("1.0",'end-1c')  +"\'"
        searchf1.destroy()
        tv2.delete(*tv2.get_children())
        cc = curse.execute("SELECT * FROM family_details WHERE [Name] = %s ORDER BY CAST(S_No AS INT)"%sf1)
        d = 0
        for sf10 in cc:
            tv2.insert(parent='', index=d, iid=d, text='', values= (sf10[0],sf10[1],sf10[2],sf10[3],sf10[4],sf10[5],sf10[6],sf10[7],sf10[8]))
            d = d + 1

    butf1 = tk.Button(searchf1,text = 'SEARCH',command = search11,font =("Tahoma",12,'bold'),bg='#00AB66')
    butf1.grid(row = 1,column = 1)


    searchf1.mainloop()

def searchName1():
    searchf = tk.Toplevel()
    searchf.title("Palli")
    searchf.geometry("550x100")

    searchhouse1= tk.Text(
        searchf,
        width = 45,
        height = 1
    )
    searchhouse1.grid(row = 0,column= 1)
    lblf = tk.Label(
        searchf,
        text="Search Name Here",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lblf.grid(row = 0,column= 0)

    def search1():
        sf ="\'"+searchhouse1.get("1.0",'end-1c')  +"\'"
        searchf.destroy()
        tv1.delete(*tv1.get_children())
        cc = curse.execute("SELECT * FROM family_details WHERE [Name] = %s ORDER BY CAST(S_No AS INT)"%sf)
        d = 0
        for sf in cc:
            tv1.insert(parent='', index=d, iid=d, text='', values= (sf[0],sf[1],sf[2],sf[3],sf[4],sf[5],sf[6],sf[7],sf[8]))
            d = d + 1

    butf = tk.Button(searchf,text = 'SEARCH',command = search1,font =("Tahoma",12,'bold'),bg='#00AB66')
    butf.grid(row = 1,column = 1)
    searchf.mainloop()

def searchdeath():
    searcdf = tk.Toplevel()
    searcdf.title("Palli")
    searcdf.geometry("550x100")

    searchhoused= tk.Text(
        searcdf,
        width = 45,
        height = 1
    )
    searchhoused.grid(row = 0,column= 1)
    lbldd = tk.Label(
        searcdf,
        text="Search Name Here",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbldd.grid(row = 0,column= 0)

    def search1d():
        sf ="\'"+searchhoused.get("1.0",'end-1c')  +"\'"
        searcdf.destroy()
        tv3.delete(*tv3.get_children())
        cc = curse.execute("SELECT * FROM death_details WHERE [Name] = %s"%sf)
        d = 0
        for sf in cc:
            tv3.insert(parent='', index=d, iid=d, text='', values= (sf[0],sf[1],sf[2],sf[3],sf[4]))
            d = d + 1

    butdf = tk.Button(searcdf,text = 'SEARCH',command = search1d,font =("Tahoma",12,'bold'),bg='#00AB66')
    butdf.grid(row = 1,column = 1)


    searcdf.mainloop()

def addFamily():
    que = tk.Toplevel()
    que.title("Palli")
    que.geometry('450x306')

    nameque = tk.Text(
        que,
        height = 1,
        width = 45
    )
    nameque.grid(row = 0,column = 1)
    lblnq = tk.Label(
        que,
        text="Name of Member  ",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lblnq.grid(row = 0,column = 0)

    gendque = tk.Text(
        que,
        height = 1,
        width = 45

    )
    gendque.grid(row = 1,column = 1)
    lblgq = tk.Label(
        que,
        text="Gender  ",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lblgq.grid(row = 1,column = 0)

    relaque = tk.Text(
        que,
        height = 1,
        width = 45
    )
    relaque.grid(row = 2,column = 1)
    lblrq = tk.Label(
        que,
        text="Relation to Owner",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lblrq.grid(row = 2,column = 0)

    ageque = tk.Text(
        que,
        height = 1,
        width = 45
    )
    ageque.grid(row = 3,column = 1)
    lblaq = tk.Label(
        que,
        text="Age  ",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lblaq.grid(row = 3,column = 0)

    dateque = tk.Text(
        que,
        height = 1,
        width = 45
    )
    dateque.grid(row = 4,column = 1)
    lbldq = tk.Label(
        que,
        text="Date of Birth  ",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbldq.grid(row = 4,column = 0)

    occuque = tk.Text(
        que,
        height = 1,
        width = 45
    )
    occuque.grid(row = 5,column = 1)
    lbloq = tk.Label(
        que,
        text="Profession  ",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbloq.grid(row = 5,column = 0)

    salaque = tk.Text(
        que,
        height = 1,
        width = 45
    )
    salaque.grid(row = 6,column = 1)
    lblsq = tk.Label(
        que,
        text="Salary  ",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lblsq.grid(row = 6,column = 0)

    def enq():
        nameque1=nameque.get("1.0",'end-1c')
        gendque1=gendque.get("1.0",'end-1c')
        relaque1=relaque.get("1.0",'end-1c')
        ageque1=ageque.get("1.0",'end-1c')
        dateque1=dateque.get("1.0",'end-1c')
        occuque1=occuque.get("1.0",'end-1c')
        salaque1=salaque.get("1.0",'end-1c')

        ccc = curse.execute('SELECT COUNT(*) AS RowCnt FROM family_details')
        for dou in ccc:
            sount = int(dou[0])
            print(sount)

        if sount > 0:
            cc = curse.execute("SELECT * FROM family_details ORDER BY CAST(S_No AS INT) DESC LIMIT 1")

            for hou in cc:
                aount = hou[0]
                aiount = int(aount)+ 1
                print(aiount)
        else:
            aiount = 1

        print(nameque1,gendque1,relaque1,ageque1,dateque1,occuque1,salaque1)
        curse.execute("INSERT INTO family_details VALUES (?,?,?,?,?,?,?,?,?)",(aiount,nameque1,gendque1,joos,relaque1,ageque1,dateque1,occuque1,salaque1))
        curse.commit()
        que.destroy()
        tv1.delete(*tv1.get_children())
        d = 0
        cc = curse.execute("SELECT * FROM family_details WHERE [Owner of House] = %s ORDER BY CAST(S_No AS INT)"%a)
        for cuq in cc:
            tv1.insert(parent='', index=d, iid=d, text='', values= (cuq[0],cuq[1],cuq[2],cuq[3],cuq[4],cuq[5],cuq[6],cuq[7],cuq[8]))
            d = d + 1



    aqd = tk.Button(que,text = 'ADD MEMBER',command = enq,font =("Tahoma",12,'bold'),bg='#00AB66')
    aqd.grid(row = 7,column = 1)

    que.mainloop()



def copy(event):
    sel = tv.selection()
    window.clipboard_clear()
    for k in sel:
        val = [tv.item(k,'text')]
        val.extend(tv.item(k,'values'))
        window.clipboard_append("\t".join(val)+"\n")

def select(w):  
    cure = tv.focus()
    global a,joos
    try:
        joos = tv.item(cure)["values"][1]
        a ="\'" + tv.item(cure)["values"][1]+"\'"
        neww()
    except:
        messagebox.showerror('Invalid Value','Please select a valid value.')
    

def select1(w):
    curee = tv1.focus()
    global aa
    try:
        aa =tv1.item(curee)["values"][1]
        quer.destroy()
        print(aa)
        editfamilyy()
    except:
        messagebox.showerror('Invalid Value','Please select a valid value.')

def select2(w):
    cureee = tv2.focus()
    global aaa,jooo
    try:
        jooo = tv2.item(cureee)["values"][3]
        aaa =tv2.item(cureee)["values"][1]
        smol.destroy()
        print(aaa)
        editfamilyy1()
    except:
        messagebox.showerror('Invalid Value','Please select a valid value.')

def select3(w):
    cureeee = tv.focus()
    global aaaa,joooo
    try:
        joooo = tv.item(cureeee)["values"][0]
        aaaa =tv.item(cureeee)["values"][1]
        print(joooo,aaaa)
        querh.destroy()
        editHouse()
    except:
        messagebox.showerror('Invalid Value','Please select a valid value.')

def select4(w):
    cureeeee = tv2.focus()
    global aaaaa
    try:
        aaaaa=tv2.item(cureeeee)["values"][3]
        queb.destroy()
        AddFamily()
    except:
        messagebox.showerror('Invalid Value','Please select a valid value.')


def select5(w):
    cureeeeee = tv2.focus()
    try:
        delhno=tv2.item(cureeeeee)["values"][0]
        curse.execute('DELETE FROM family_details WHERE S_No = (?);',(delhno,))
        curse.commit()
        qued.destroy()
        cc = curse.execute("SELECT * FROM family_details ORDER BY CAST(S_No AS INT)")
        tv2.delete(*tv2.get_children())
        tv2.bind("<ButtonRelease-1>",nothing)
        d = 0
        for cu1 in cc:
            tv2.insert(parent='', index=d, iid=d, text='', values= (cu1[0],cu1[1],cu1[2],cu1[3],cu1[4],cu1[5],cu1[6],cu1[7],cu1[8]))
            d = d + 1
    except:
        messagebox.showerror('Invalid Value','Please select a valid value.')

def select6(w):
    cureeeeeee = tv.focus()
    try:
        delhno1=tv.item(cureeeeeee)["values"][0]
        cc = curse.execute('SELECT * FROM house_details WHERE [House Number] = (?);',(delhno1,))
        for mo in cc:
            delno1 = mo[1]
        curse.execute('DELETE FROM house_details WHERE [House Number] = (?);',(delhno1,))
        curse.commit()
        curse.execute('DELETE FROM family_details WHERE [Name] = (?);',(delno1,))
        curse.commit()
        queda.destroy()
        cc = curse.execute("SELECT * FROM house_details")
        tv.delete(*tv.get_children())
        tv.bind("<ButtonRelease-1>",select)
        d = 0
        for cu1 in cc:
            tv.insert(parent='', index=d, iid=d, text='', values= (cu1[0],cu1[1],cu1[2],cu1[3],cu1[4],cu1[5],cu1[6]))
            d = d + 1
    except:
        messagebox.showerror('Invalid Value','Please select a valid value.')

def select7(w):
    cureeeeeeee = tv1.focus()
    try:
        delhnoi=tv1.item(cureeeeeeee)["values"][0]
        curse.execute('DELETE FROM family_details WHERE S_No = (?);',(delhnoi,))
        curse.commit()
        quedad.destroy()
        cc = curse.execute("SELECT * FROM family_details WHERE [Owner of House] = %s ORDER BY CAST(S_No AS INT)"%a)
        tv1.bind("<ButtonRelease-1>",nothing)
        tv1.delete(*tv1.get_children())
        d = 0
        for cu in cc:
            tv1.insert(parent='', index=d, iid=d, text='', values= (cu[0],cu[1],cu[2],cu[3],cu[4],cu[5],cu[6],cu[7],cu[8]))
            d = d + 1
    except:
        messagebox.showerror('Invalid Value','Please select a valid value.')

def select8(w):
    cureeeeeeeee = tv3.focus()
    try:
        global aaaaaa
        aaaaaa=tv3.item(cureeeeeeeee)["values"][0]
        dquer.destroy()
        editdeathh()
    except:
        messagebox.showerror('Invalid Value','Please select a valid value.')

def select9(w):
        cureeeeeeeeee = tv3.focus()
    
        delhnoi=tv3.item(cureeeeeeeeee)["values"][0]
        curse.execute('DELETE FROM death_details WHERE [S No] = (?);',(delhnoi,))
        curse.commit()
        quedd.destroy()
        cc = curse.execute("SELECT * FROM death_details")
        tv3.bind("<ButtonRelease-1>",nothing)
        tv3.delete(*tv3.get_children())
        d = 0
        for cu in cc:
            tv3.insert(parent='', index=d, iid=d, text='', values= (cu[0],cu[1],cu[2],cu[3],cu[4]))
            d = d + 1

def select10(w):
    cureeeeeeeeeee = tv.focus()
    global aaaaaaa
    try:
        aaaaaa = tv.item(cureeeeeeeeeee)["values"][0]
        cc = curse.execute("SELECT * FROM house_details WHERE [House Number] = (?)",(aaaaaa,))
        for la in cc:
            paidis = float(la[6])
        pearchn = tk.Toplevel()
        pearchn.title("Palli")
        pearchn.geometry("550x100")

        pearchhouse = tk.Text(
            pearchn,
            width = 45,
            height = 1
        )
        pearchhouse.grid(row = 0,column = 1)    
        lbps = tk.Label(
            pearchn,
            text="Balance Paid",
            foreground="black",
            font =("Oswald",12,'bold')
        )
        lbps.grid(row = 0,column = 0)

        def pearch():
            se =float(pearchhouse.get("1.0",'end-1c'))
            pearchn.destroy()
            s = paidis - se
            print(s)
            curse.execute("UPDATE house_details SET [Payment Status] = (?) WHERE [House Number] = (?)",(s,aaaaaa) )
            curse.commit()
            tv.delete(*tv.get_children())
            cc = curse.execute("SELECT * FROM house_details")
            d = 0
            smo.destroy()
            for ss in cc:
                tv.insert(parent='', index=d, iid=d, text='', values= (ss[0],ss[1],ss[2],ss[3],ss[4],ss[5],ss[6]))
                d = d + 1

        bups = tk.Button(pearchn,text = 'UPDATE',command = pearch,font =("Tahoma",12,'bold'),bg='#00AB66')
        bups.grid(row = 3,column = 1)

        pearchn.mainloop()
    except:
        messagebox.showerror('Invalid Value','Please select a valid value.')
    

def select11(w):
        cureeeeeeeeeeee = tv1.focus()
    
        delhnoi=tv1.item(cureeeeeeeeeeee)["values"][0]
        curse.execute('DELETE FROM family_details WHERE [S_No] = (?);',(delhnoi,))
        curse.commit()
        quedad.destroy()
        cc = curse.execute("SELECT * FROM family_details WHERE [Owner of House] = %s ORDER BY CAST(S_No AS INT)"%a)
        tv1.delete(*tv1.get_children())
        d = 0
        for cu in cc:
            tv1.insert(parent='', index=d, iid=d, text='', values= (cu[0],cu[1],cu[2],cu[3],cu[4],cu[5],cu[6],cu[7],cu[8]))
            d = d + 1









def male():
    cc=curse.execute("SELECT * FROM family_details WHERE Gender='Male' ORDER BY CAST(S_No AS INT)")
    tv1.delete(*tv1.get_children())
    d = 0
    for ma in cc:
        print(ma)
        tv1.insert(parent='', index=d, iid=d, text='', values= (ma[0],ma[1],ma[2],ma[3],ma[4],ma[5],ma[6],ma[7],ma[8]))
        d = d + 1
    cc=curse.execute("SELECT * FROM family_details WHERE Gender='male' ORDER BY CAST(S_No AS INT)")
    for ma in cc:
        print(ma)
        tv1.insert(parent='', index=d, iid=d, text='', values= (ma[0],ma[1],ma[2],ma[3],ma[4],ma[5],ma[6],ma[7],ma[8]))
        d = d + 1


def female():
    cc = curse.execute("SELECT * FROM family_details WHERE Gender='Female' ORDER BY CAST(S_No AS INT)")
    tv1.delete(*tv1.get_children())
    d = 0
    for fe in cc:
        tv1.insert(parent='', index=d, iid=d, text='', values= (fe[0],fe[1],fe[2],fe[3],fe[4],fe[5],fe[6],fe[7],fe[8]))
        d = d + 1
    cc=curse.execute("SELECT * FROM family_details WHERE Gender='female' ORDER BY CAST(S_No AS INT)")
    for ma in cc:
        print(ma)
        tv1.insert(parent='', index=d, iid=d, text='', values= (ma[0],ma[1],ma[2],ma[3],ma[4],ma[5],ma[6],ma[7],ma[8]))
        d = d + 1

def student():
    cc=curse.execute("SELECT * FROM family_details WHERE Occupation ='Student'")
    tv1.delete(*tv1.get_children())
    d = 0
    for stu in cc:
        tv1.insert(parent='', index=d, iid=d, text='', values= (stu[0],stu[1],stu[2],stu[3],stu[4],stu[5],stu[6],stu[7],stu[8]))
        d = d + 1

def age():
    ageing = 0
    cc = curse.execute('SELECT * FROM family_details WHERE Age >= 14 and Age <= 18')
    tv1.delete(*tv1.get_children())

    d = 0
    for ma in cc:
        tv1.insert(parent='', index=d, iid=d, text='', values= (ma[0],ma[1],ma[2],ma[3],ma[4],ma[5],ma[6],ma[7],ma[8]))
        d = d +1

def age10():
    ageing = 0
    cc = curse.execute('SELECT * FROM family_details WHERE Age >= 14 and Age <= 18')
    tv2.delete(*tv2.get_children())

    d = 0
    for ma in cc:
        tv2.insert(parent='', index=d, iid=d, text='', values= (ma[0],ma[1],ma[2],ma[3],ma[4],ma[5],ma[6],ma[7],ma[8]))
        d = d +1

def refresh():
    cc = curse.execute("SELECT * FROM family_details WHERE [Owner of House] = %s ORDER BY CAST(S_No AS INT)"%a)
    tv1.delete(*tv1.get_children())
    d = 0
    for cu in cc:
        tv1.insert(parent='', index=d, iid=d, text='', values= (cu[0],cu[1],cu[2],cu[3],cu[4],cu[5],cu[6],cu[7],cu[8]))
        d = d + 1

def male1():
    cc = curse.execute("SELECT * FROM family_details WHERE Gender='Male' ORDER BY CAST(S_No AS INT)")
    tv2.delete(*tv2.get_children())
    d = 0
    for ma1 in cc:
        tv2.insert(parent='', index=d, iid=d, text='', values= (ma1[0],ma1[1],ma1[2],ma1[3],ma1[4],ma1[5],ma1[6],ma1[7],ma1[8]))
        d = d + 1
    cc = curse.execute("SELECT * FROM family_details WHERE Gender='male' ORDER BY CAST(S_No AS INT)")
    d = 0
    for ma1 in cc:
        tv2.insert(parent='', index=d, iid=d, text='', values= (ma1[0],ma1[1],ma1[2],ma1[3],ma1[4],ma1[5],ma1[6],ma1[7],ma1[8]))
        d = d + 1


def female1():
    cc = curse.execute("SELECT * FROM family_details WHERE Gender='Female'")
    tv2.delete(*tv2.get_children())
    d = 0
    for fe1 in cc:
        tv2.insert(parent='', index=d, iid=d, text='', values= (fe1[0],fe1[1],fe1[2],fe1[3],fe1[4],fe1[5],fe1[6],fe1[7],fe1[8]))
        d = d + 1
    cc = curse.execute("SELECT * FROM family_details WHERE Gender='female'")
    d = 0
    for fe1 in cc:
        tv2.insert(parent='', index=d, iid=d, text='', values= (fe1[0],fe1[1],fe1[2],fe1[3],fe1[4],fe1[5],fe1[6],fe1[7],fe1[8]))
        d = d + 1

def student1():
    cc = curse.execute("SELECT * FROM family_details WHERE Occupation ='Student'")
    tv2.delete(*tv2.get_children())
    d = 0
    for stu1 in cc:
        tv2.insert(parent='', index=d, iid=d, text='', values= (stu1[0],stu1[1],stu1[2],stu1[3],stu1[4],stu1[5],stu1[6],stu1[7],stu1[8]))
        d = d + 1

def refresh1():
    cc = curse.execute("SELECT * FROM family_details ORDER BY CAST(S_No AS INT)")
    tv2.delete(*tv2.get_children())
    d = 0
    for cu1 in cc:
        tv2.insert(parent='', index=d, iid=d, text='', values= (cu1[0],cu1[1],cu1[2],cu1[3],cu1[4],cu1[5],cu1[6],cu1[7],cu1[8]))
        d = d + 1

def refresh3():
    cc = curse.execute("SELECT * FROM house_details")
    tv.delete(*tv.get_children())
    d = 0
    for cu1 in cc:
        tv.insert(parent='', index=d, iid=d, text='', values= (cu1[0],cu1[1],cu1[2],cu1[3],cu1[4],cu1[5],cu1[6]))
        d = d + 1

def refresh2():
    cc = curse.execute("SELECT * FROM death_details")
    tv3.delete(*tv3.get_children())
    d = 0
    for cu1 in cc:
        tv3.insert(parent='', index=d, iid=d, text='', values= (cu1[0],cu1[1],cu1[2],cu1[3],cu1[4]))
        d = d + 1

def delete():
    global qued
    qued = tk.Label(
        window1,
        text = "Select the member you wish to delete",
        font =("Oswald",20,'bold')
    )
    qued.place(x=500 ,y = 25)
    tv2.bind("<ButtonRelease-1>",select5)

def delete1():
    global queda
    queda = tk.Label(
        window,
        text = "Select the house you wish to delete",
        font =("Oswald",20,'bold')
    )
    queda.place(x=540 ,y = 25)
    tv.bind("<ButtonRelease-1>",select6)

def delete2():
    global quedad
    quedad = tk.Label(
        fam,
        text = "Select the member you wish to delete",
        font =("Oswald",20,'bold')
    )
    quedad.place(x=550 ,y = 25)
    tv1.bind("<ButtonRelease-1>",select11)

def delete3():
    global quedd
    quedd = tk.Label(
        dea,
        text = "Select the entry you wish to delete",
        font =("Oswald",20,'bold')
    )
    quedd.place(x=600 ,y = 25)
    tv3.bind("<ButtonRelease-1>",select9)


def neww():
    global fam
    fam = tk.Toplevel()
    fam.title("Palli")
    fam.state('zoomed')

    global tv1
    tv1 = ttk.Treeview(fam,columns =('SNo','Name','Gender','Owner of House','Relation to Owner','Age','Date of Birth','Occupation','Salary'),show='headings',height = 25)
    vsb = ttk.Scrollbar(fam, orient="vertical", command=tv1.yview)
    vsb.place(x=1419 ,y=130,height = 500)
    tv1.configure(yscrollcommand=vsb.set)
    #styl1 = ttk.Style()
    #styl1.configure("Treeview.Heading",font = ('Oswald',14))

    tv1.column('#0', width=0, stretch="NO")
    tv1.column('SNo', anchor="center", width=100)
    tv1.column('Name', anchor="center", width=200)
    tv1.column('Gender', anchor="center", width=150)
    tv1.column('Owner of House', anchor="center", width=200)
    tv1.column('Relation to Owner', anchor="center", width=150)
    tv1.column('Age', anchor="center", width=100)
    tv1.column('Date of Birth', anchor="center", width=150)
    tv1.column('Occupation', anchor="center", width=150)
    tv1.column('Salary', anchor="center", width=150)

    tv1.heading('#0', text='', anchor="center")
    tv1.heading('SNo', text='SNo', anchor="center")
    tv1.heading('Name', text='Name', anchor="center")
    tv1.heading('Gender', text='Gender', anchor="center")
    tv1.heading('Owner of House', text='Owner of House', anchor="center")
    tv1.heading('Relation to Owner', text='Relation to Owner', anchor="center")
    tv1.heading('Age', text='Age', anchor="center")
    tv1.heading('Date of Birth', text='Date of Birth', anchor="center")
    tv1.heading('Occupation', text='Occupation', anchor="center")
    tv1.heading('Salary', text='Salary', anchor="center")

    cc = curse.execute("SELECT * FROM family_details WHERE [Owner of House] = %s ORDER BY CAST(S_No AS INT)"%a)
    d = 0 
    for j in cc:
        print(j)
        tv1.insert(parent='', index=d, iid=d, text='', values= (j[0],j[1],j[2],j[3],j[4],j[5],j[6],j[7],j[8]))
        d = d + 1
    tv1.place(x=85,y=100)

    m1 = Menubutton(
        fam,
        text = "SNo",
        width = 13,
        anchor = "center",
        font =("Oswald",12,'bold'),
        bg = '#99FF99'  
    )
    m1.place(x=85,y=100)

    m2 = Menubutton(
        fam,
        text = "Name",
        width = 24,
        anchor = "center",
        font =("Oswald",12,'bold'),
        bg = '#99FF99'
    )
    m2.place(x=180,y=100)

    m3 = Menubutton(
        fam,
        text = "Gender",
        width = 22,
        anchor = "center",
        font =("Oswald",12,'bold'),
        bg = '#99FF99'
    )
    m3.menu = Menu(m3,tearoff =0)
    m3["menu"]=m3.menu
    m3.menu.add_checkbutton(label="Male",command = male)
    m3.menu.add_checkbutton(label="Female",command = female)
    m3.place(x=340,y=100)

    m4 = Menubutton(
        fam,
        text = "Owner of House",
        width = 14,
        anchor = "center",
        font =("Oswald",12,'bold'),
        bg = '#99FF99'
    )
    m4.place(x=545,y=100)

    m5 = Menubutton(
        fam,
        text = "Relation to Owner",
        width = 27,
        anchor = "center",
        font =("Oswald",12,'bold'),
        bg = '#99FF99'
    )
    m5.place(x=680,y=100)

    m6 = Menubutton(
        fam,
        text = "Age",
        width = 12,
        anchor = "center",
        font =("Oswald",12,'bold'),
        bg = '#99FF99'
    )
    m6.menu = Menu(m6,tearoff =0)
    m6["menu"]=m6.menu
    m6.menu.add_radiobutton(label="14-18",command = age)
    m6.place(x=875,y=100)
    
    m7 = Menubutton(
        fam,
        text = "Date of Birth",
        width = 15,
        anchor = "center",
        font =("Oswald",12,'bold'),
        bg = '#99FF99'
    )
    m7.place(x=980,y=100)


    m8 = Menubutton(
        fam,
        text = "Occupation",
        width = 18,
        anchor = "center",
        font =("Oswald",12,'bold'),
        bg = '#99FF99'
    )
    m8.menu = Menu(m8,tearoff =0)
    m8["menu"]=m8.menu
  # m8.menu.add_radiobutton(label="",command = student,value = 2,variable = sui)
    m8.menu.add_radiobutton(label="Student",command = student)
    m8.place(x=1120,y=100)

    m9 = Menubutton(
        fam,
        text = "Salary",
        width = 16,
        anchor = "center",
        font =("Oswald",12,'bold'),
        bg = '#99FF99'
    )
    m9.place(x = 1280,y=100)


    addf = tk.Button(
	    fam,
	    text = "Add Family Members",
    	command = addFamily,font =("Tahoma",12,'bold'),bg='#00AB66'
	    )
    addf.place(x = 170,y = 750,anchor = "center")

    edif = tk.Button(
	    fam,
	    text = "Edit Family",
	    command = editFamily,font =("Tahoma",12,'bold'),bg='#00AB66'
	    )
    edif.place(x = 470,y = 750,anchor = "center")

    serf = tk.Button(
	    fam,
	    text = "Search Name",
	    command = searchName1,font =("Tahoma",12,'bold'),bg='#00AB66'
	    )
    serf.place(x = 770,y = 750,anchor = "center")

    ref = tk.Button(
	    fam,
	    text = "Refresh",
	    command = refresh,font =("Tahoma",12,'bold'),bg='#00AB66'
	    )
    ref.place(x = 1070,y = 750,anchor = "center")

    defad = tk.Button(
	    fam,
	    text = "Delete",
	    command = delete2,
        font =("Tahoma",12,'bold'),
        bg='#00AB66'
	    )
    defad.place(x = 1370,y = 750,anchor = "center")

    fam.mainloop()

def af():
    global queb
    queb = tk.Label(
        window1,
        text = "Select family you wish to add member(s) to",
        font =("Oswald",20,'bold')
    )
    queb.place(x=500 ,y = 25)
    tv2.bind("<ButtonRelease-1>",select4)

def AddFamily():
    browhat = tk.Toplevel()
    browhat.title('Palli')
    browhat.geometry('550x100')
    fnumber = tk.Text(
        browhat,
        height = 1,
        width = 30
    )
    fnumber.grid(row = 0,column = 1)
    lbl001 = tk.Label(
        browhat,
        text="No of family Members To Add: ",
        foreground="black",
        font =("Oswald",12,'bold')
    )
    lbl001.grid(row = 0,column = 0)

    tv2.bind("<ButtonRelease-1>",nothing)

    def enq(fno):
            fn = fno - 1
        
            queb = tk.Toplevel()
            queb.title("Palli")
            queb.geometry("450x306")
            namequeb = tk.Text(
                queb,
                height = 1,
                width = 45
                )
            namequeb.grid(row = 0,column = 1)
            lblnqb = tk.Label(
                queb,
                text="Name of Member",
                foreground="black",
                font =("Oswald",12,'bold')
                )
            lblnqb.grid(row = 0,column = 0)

            gendqueb = tk.Text(
                queb,
                height = 1,
                width = 45

                )
            gendqueb.grid(row = 1,column = 1)
            lblgqb = tk.Label(
                queb,
                text="Gender",
                foreground="black",
                font =("Oswald",12,'bold')
                )
            lblgqb.grid(row = 1,column = 0)

            relaqueb = tk.Text(
                queb,
                height = 1,
                width = 45
                )
            relaqueb.grid(row = 2,column = 1)
            lblrqb = tk.Label(
                queb,
                text="Relation to Owner",
                foreground="black",
                font =("Oswald",12,'bold')
                )   
            lblrqb.grid(row = 2,column = 0)

            agequeb = tk.Text(
                queb,
                height = 1,
                width = 45
                )
            agequeb.grid(row = 3,column = 1)
            lblaqb = tk.Label(
                queb,
                text="Age",
                foreground="black",
                font =("Oswald",12,'bold')
                )
            lblaqb.grid(row = 3,column = 0)

            datequeb = tk.Text(
                queb,
                height = 1,
                width = 45
                )
            datequeb.grid(row = 4,column = 1)
            lbldqb = tk.Label(
                queb,
                text="Date of Birth",
                foreground="black",
                font =("Oswald",12,'bold')
            )
            lbldqb.grid(row = 4,column = 0)

            occuqueb = tk.Text(
                queb,
                height = 1,
                width = 45
                )
            occuqueb.grid(row = 5,column = 1)
            lbloqb = tk.Label(
                queb,
                text="Profession",
                foreground="black",
                font =("Oswald",12,'bold')
            )
            lbloqb.grid(row = 5,column = 0)

            salaqueb = tk.Text(
                queb,
                height = 1,
                width = 45
                )
            salaqueb.grid(row = 6,column = 1)
            lblsqb = tk.Label(
                queb,
                text="Salary",
                foreground="black",
                font =("Oswald",12,'bold')
            )
            lblsqb.grid(row = 6,column = 0)

            def enber():
                namequeb1=namequeb.get("1.0",'end-1c')
                gendqueb1=gendqueb.get("1.0",'end-1c')
                relaqueb1=relaqueb.get("1.0",'end-1c')
                agequeb1=agequeb.get("1.0",'end-1c')
                datequeb1=datequeb.get("1.0",'end-1c')
                occuqueb1=occuqueb.get("1.0",'end-1c')
                salaqueb1=salaqueb.get("1.0",'end-1c')


                ccc = curse.execute('SELECT COUNT(*) AS RowCnt FROM family_details')
                for dou in ccc:
                    sount = int(dou[0])
                    print(sount)

                if sount > 0:
                    cc = curse.execute("SELECT * FROM family_details ORDER BY CAST(S_No AS INT) DESC LIMIT 1")

                    for hou in cc:
                        aount = hou[0]
                        aiount = int(aount)+ 1
                        print(aiount)
                else:
                    aiount = 1

                curse.execute("INSERT INTO family_details VALUES (?,?,?,?,?,?,?,?,?)",(aiount,namequeb1,gendqueb1,aaaaa,relaqueb1,agequeb1,datequeb1,occuqueb1,salaqueb1))
                curse.commit()
                queb.destroy()
                tv2.delete(*tv2.get_children())
                d = 0
                cc = curse.execute("SELECT * FROM family_details ORDER BY CAST(S_No AS INT)")
                for cub in cc:
                    tv2.insert(parent='', index=d, iid=d, text='', values= (cub[0],cub[1],cub[2],cub[3],cub[4],cub[5],cub[6],cub[7],cub[8]))
                    d = d + 1
                if fn > 0:
                    enq(fn)
            abd = tk.Button(queb,text = 'ADD MEMBER',command = enber,font =("Tahoma",12,'bold'),bg='#00AB66')
            abd.grid(row = 10,column = 1)
            
            
    
    def enb():
        global fno
        fno = int(fnumber.get('1.0','end-1c'))
        browhat.destroy()
        enq(fno)

    butb = tk.Button(browhat,text = 'ENTER',command = enb,font =("Tahoma",12,'bold'),bg='#00AB66')
    butb.grid(row = 1,column = 1)

    browhat.mainloop()





        
           
 
home.mainloop()
#FRONT END

#BACK END FOR WINDOW 1





