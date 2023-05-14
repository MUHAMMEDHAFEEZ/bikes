
from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage ,Label ,messagebox
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\guiproject\adhamcycle\build\assets_user\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
qty=0
qty1=0
qty2=0
qty3=0
qty4=0
qty5=0
qty6=0
qty7=0

def itemplus():
    global qty
    qty+=1
    my_label.config(text = qty)

def item1plus():
    global qty1
    qty1+=1
    my_label1.config(text = qty1)

def item2plus():
    global qty2
    qty2+=1
    my_label2.config(text = qty2)

def item3plus():
    global qty3
    qty3+=1
    my_label3.config(text = qty3)

def item4plus():
    global qty4
    qty4+=1
    my_label7.config(text = qty4)

def item5plus():
    global qty5
    qty5+=1
    my_label6.config(text = qty5)

def item6plus():
    global qty6
    qty6+=1
    my_label5.config(text = qty6)

def item7plus():
    global qty7
    qty7+=1
    my_label4.config(text = qty7)
    

def itemmins():
    global qty
    if(qty>0):
         qty-=1
    my_label.config(text = qty)

def item1mins():
    global qty1
    if(qty1>0):
         qty1-=1
    my_label1.config(text = qty1)

def item2mins():
    global qty2
    if(qty2>0):
         qty2-=1
    my_label2.config(text = qty2)

def item3mins():
    global qty3
    if(qty3>0):
         qty3-=1
    my_label3.config(text = qty3)

def item4mins():
    global qty4
    if(qty4>0):
        qty4-=1
    my_label7.config(text = qty4)

def item5mins():
    global qty5
    if(qty5>0):
        qty5-=1
    my_label6.config(text = qty5)

def item6mins():
    global qty6
    if(qty6>0):
        qty6-=1
    my_label5.config(text = qty6)

def item7mins():
    global qty7
    if(qty7>0):
        qty7-=1
    my_label4.config(text = qty7)

#new_invice()
def new_invoice():
    tree.delete(*tree.get_children())
    
    invoice_list.clear()

def generate_invoice():
    doc = DocxTemplate("invoice_template.docx")
    name = "adham"
    phone = "666-666"
    subtotal = sum(item[3] for item in invoice_list) 
    salestax = 0.1
    total = subtotal*(1-salestax)
    
    doc.render({"name":name, 
            "phone":phone,
            "invoice_list": invoice_list,
            "subtotal":subtotal,
            "salestax":str(salestax*100)+"%",
            "total":total})
    
    doc_name = "new_invoice" + name + datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".docx"
    doc.save(doc_name)
    
    messagebox.showinfo("Invoice Complete", "Invoice Complete")
    
    new_invoice()    
    
window = Tk()

window.geometry("1280x832")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 832,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
columns = ('qty', 'desc', 'price', 'total')
tree = ttk.Treeview(window, columns=columns, show="headings")
tree.heading('qty', text='Qty')
tree.heading('desc', text='Description')
tree.heading('price', text='Unit Price')
tree.heading('total', text="Total")
tree.place(x=206,
    y=552,
    width=871,
    height=255)

invoice_list = []

def add_item():
    global qty
    if(qty>0):
         desc = "BICYCLE SIZE 20 FOR CHILDREN FROM 8 TO 12 YEARS OLD - RED"
         price = 7999.00
         line_total= qty*price
         invoice_item = [qty, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
    
    
         invoice_list.append(invoice_item)
def add_item1():
    global qty1
    if(qty1>0):
         desc1 = "Phoenix Bicycle, 21 Speeds, 29 Inches - Black and Red"
         price1 = 6999.00
         line_total1 = qty1*price1
         invoice_item = [qty1, desc1, price1, line_total1]
         tree.insert('',0, values=invoice_item)
    
    
         invoice_list.append(invoice_item)
def add_item2():
    global qty2
    if(qty2>0):
         desc2 = "ZOOM- Mountain Bicycle- IRON SIZE 26 Multi color"
         price2 = 2899.00
         line_total2 = qty2*price2
         invoice_item = [qty2, desc2, price2, line_total2]
         tree.insert('',0, values=invoice_item)
    
    
         invoice_list.append(invoice_item)
         
def add_item3():
    global qty3
    if(qty3>0):
         desc3 = "Mountain Bicycle-zoom classic 26 - Multi colo"
         price3 = 3699.00
         line_total3 = qty3*price3
         invoice_item3= [qty3, desc3, price3, line_total3]
         tree.insert('',0, values=invoice_item3)
    
    
         invoice_list.append(invoice_item3)
def add_item4():
    global qty4
    if(qty4>0):
         desc4 = "Phoenix Bicycle, 21 Speeds, 26 Inches - Blue and Yellow"
         price4 = 9999.00
         line_total4 = qty4*price4
         invoice_item4= [qty4, desc4, price4, line_total4]
         tree.insert('',0, values=invoice_item4)
    
    
         invoice_list.append(invoice_item4)
def add_item5():
    global qty5
    if(qty5>0):
         desc5 = "ZOOM- Mountain Bicycle- aluminum SIZE 26 Multi color"
         price5 = 1899.00
         line_total5 = qty5*price5
         invoice_item5 = [qty5, desc5, price5, line_total5]
         tree.insert('',0, values=invoice_item5)
    
    
         invoice_list.append(invoice_item5)
def add_item6():
    global qty6
    if(qty6>0):
         desc6 = "CNOPT MACTEP Mountain Bike 21 Speed Full Suspension Mountain Bike 26"
         price6 = 7899.00
         line_total6= qty6*price6
         invoice_item6 = [qty6, desc6, price6, line_total6]
         tree.insert('',0, values=invoice_item6)
    
    
         invoice_list.append(invoice_item6)
def add_item7():
    global qty7
    if(qty7>0):
         desc7 = "kross N-Spire 27.5T Inches Cycle 21S"
         price7= 6199.00
         line_total7= qty7*price7
         invoice_item7 = [qty7, desc7, price7, line_total7]
         tree.insert('',0, values=invoice_item7)
    
    
         invoice_list.append(invoice_item7)
    

my_label= Label(window,text = qty)
my_label.place(x=242,
    y=218,
    width=58,
    height=12)


my_label1= Label(window,text = "0")
my_label1.place(x=447,
    y=218,
    width=58,
    height=12)

my_label2= Label(window,text = "0")
my_label2.place(x=783,
    y=218,
    width=58,
    height=12)


my_label3= Label(window,text = "0")
my_label3.place(x=992,
    y=218,
    width=58,
    height=12)


my_label4= Label(window,text = "0")
my_label4.place(x=986,
    y=431,
    width=58,
    height=12)


my_label5= Label(window,text = "0")
my_label5.place(x=784,
    y=431,
    width=58,
    height=12)


my_label6= Label(window,text = "0")
my_label6.place(x=454,
    y=431,
    width=58,
    height=12)


my_label7= Label(window,text = "0")
my_label7.place(x=240,
    y=431,
    width=58,
    height=12)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    271.0,
    107.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item(),
    relief="flat"
)
button_1.place(
    x=212.0,
    y=232.0,
    width=118.33200073242188,
    height=20.067703247070312
)
#//new invo
button_image_newinv = PhotoImage(
    file=relative_to_assets("Group 2.png"))
button_newinv = Button(
    text="new_inv",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: new_invoice(),
    relief="flat"
)
button_newinv.place(
    x=1090,
    y=553,
    width=72,
    height=101
)

#// Generate_invoice
button_image_newinv = PhotoImage(
    file=relative_to_assets("Group 1.png"))
button_newinv = Button(
    text="Generate_invoice",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: generate_invoice(),
    relief="flat"
)
button_newinv.place(
    x=1090,
    y=666,
    width=72,
    height=101
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item4(),
    relief="flat"
)
button_2.place(
    x=210.2379150390625,
    y=445.0,
    width=119.7620849609375,
    height=20.067699432373047
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    271.0,
    175.0,
    image=image_image_2
)

canvas.create_text(
    240.0,
    184.0,
    anchor="nw",
    text="CHILDREN",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    232.0,
    199.0,
    anchor="nw",
    text="EGP7,999.00",
    fill="#000000",
    font=("Inter Bold", 12 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    271.0,
    318.0,
    image=image_image_3
)

canvas.create_text(
    208.0,
    383.0,
    anchor="nw",
    text="Phoenix Bicycle, 21 \n",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    248.0,
    398.0,
    anchor="nw",
    text="Speeds,",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    230.0,
    401.0,
    anchor="nw",
    text="\n EGP9,999.00",
    fill="#000000",
    font=("Inter", 12 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    480.0,
    113.0,
    image=image_image_4
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item1(),
    relief="flat"
)
button_3.place(
    x=417.0,
    y=232.0,
    width=118.33200073242188,
    height=20.357742309570312
)

canvas.create_text(
    417.0,
    177.0,
    anchor="nw",
    text="Phoenix Bicycle, 21 \n",
    fill="#000000",
    font=("Inter", 12 * -1)
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    484.0,
    326.0,
    image=image_image_5
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item5(),
    relief="flat"
)
button_4.place(
    x=425.0,
    y=445.0,
    width=118.33200073242188,
    height=20.067699432373047
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item6(),
    relief="flat"
)
button_5.place(
    x=755.0,
    y=445.0,
    width=118.33200073242188,
    height=20.067699432373047
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item7(),
    relief="flat"
)
button_6.place(
    x=963.0,
    y=446.0,
    width=118.33200073242188,
    height=20.067699432373047
)

canvas.create_text(
    421.0,
    374.0,
    anchor="nw",
    text="ZOOM- Mountain \n",
    fill="#000000",
    font=("Inter", 12 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    812.0,
    107.0,
    image=image_image_6
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item2(),
    relief="flat"
)
button_7.place(
    x=749.0,
    y=232.0,
    width=122.0115966796875,
    height=20.357742309570312
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item3(),
    relief="flat"
)
button_8.place(
    x=961.0,
    y=232.0,
    width=122.0115966796875,
    height=20.357742309570312
)

canvas.create_text(
    749.0,
    175.0,
    anchor="nw",
    text="ZOOM- Mountain \n",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    791.0,
    187.0,
    anchor="nw",
    text="Bicycle",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    773.0,
    201.0,
    anchor="nw",
    text="EGP2,899.00",
    fill="#000000",
    font=("Inter Bold", 12 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    814.0,
    318.0,
    image=image_image_7
)

canvas.create_text(
    751.0,
    373.0,
    anchor="nw",
    text="CNOPT MACTEP \n",
    fill="#000000",
    font=("Inter", 12 * -1)
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    1021.0,
    111.0,
    image=image_image_8
)

canvas.create_text(
    957.0,
    177.0,
    anchor="nw",
    text="Mountain Bicycle\n",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    976.0,
    188.0,
    anchor="nw",
    text="zoom classic 26",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    978.0,
    203.0,
    anchor="nw",
    text="  EGP3,699.00",
    fill="#000000",
    font=("Inter", 12 * -1)
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    1014.0,
    316.0,
    image=image_image_9
)

canvas.create_text(
    950.0,
    383.0,
    anchor="nw",
    text="kross N-Spire 27.5T ",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    910.0,
    453.0,
    anchor="nw",
    text=" ",
    fill="#000000",
    font=("Inter", 12 * -1)
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    93.0,
    263.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    1186.0,
    525.0,
    image=image_image_11
)

canvas.create_text(
    458.0,
    189.0,
    anchor="nw",
    text="Speeds",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    440.0,
    202.0,
    anchor="nw",
    text="EGP6,999.00",
    fill="#000000",
    font=("Inter Bold", 12 * -1)
)

canvas.create_text(
    430.0,
    393.0,
    anchor="nw",
    text="SIZE 26 Multi color",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    445.0,
    416.0,
    anchor="nw",
    text="EGP1,899.00",
    fill="#000000",
    font=("Inter Bold", 12 * -1)
)

canvas.create_text(
    768.0,
    393.0,
    anchor="nw",
    text="Mountain Bike 26",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    779.0,
    412.0,
    anchor="nw",
    text="EGP7,899.00",
    fill="#000000",
    font=("Inter Bold", 12 * -1)
)

canvas.create_text(
    963.0,
    398.0,
    anchor="nw",
    text="Inches Cycle 21S-",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    976.0,
    413.0,
    anchor="nw",
    text="EGP6,199.00",
    fill="#000000",
    font=("Inter Bold", 12 * -1)
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: itemmins(),
    relief="flat"
)
button_9.place(
    x=193.0,
    y=235.0,
    width=16.0,
    height=15.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:item1mins(),
    relief="flat"
)
button_10.place(
    x=395.0,
    y=235.0,
    width=16.0,
    height=15.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item2mins(),
    relief="flat"
)
button_11.place(
    x=731.0,
    y=234.0,
    width=16.0,
    height=15.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item3mins(),
    relief="flat"
)
button_12.place(
    x=945.0,
    y=234.0,
    width=16.0,
    height=15.0
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item7mins(),
    relief="flat"
)
button_13.place(
    x=945.0,
    y=448.0,
    width=16.0,
    height=15.0
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item6mins(),
    relief="flat"
)
button_14.place(
    x=736.0,
    y=447.0,
    width=16.0,
    height=15.0
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item5mins(),
    relief="flat"
)
button_15.place(
    x=406.0,
    y=448.0,
    width=16.0,
    height=15.0
)

button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item4mins(),
    relief="flat"
)
button_16.place(
    x=189.0,
    y=448.0,
    width=16.0,
    height=15.0
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: itemplus(),
    relief="flat"
)
button_17.place(
    x=334.0,
    y=234.0,
    width=16.0,
    height=16.0
)

button_image_18 = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item1plus(),
    relief="flat"
)
button_18.place(
    x=536.0,
    y=234.0,
    width=16.0,
    height=16.0
)

button_image_19 = PhotoImage(
    file=relative_to_assets("button_19.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item2plus(),
    relief="flat"
)
button_19.place(
    x=872.0,
    y=233.0,
    width=16.0,
    height=16.0
)

button_image_20 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_20 = Button(
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item3plus(),
    relief="flat"
)
button_20.place(
    x=1086.0,
    y=233.0,
    width=16.0,
    height=16.0
)

button_image_21 = PhotoImage(
    file=relative_to_assets("button_21.png"))
button_21 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item7plus(),
    relief="flat"
)
button_21.place(
    x=1086.0,
    y=447.0,
    width=16.0,
    height=16.0
)

button_image_22 = PhotoImage(
    file=relative_to_assets("button_22.png"))
button_22 = Button(
    image=button_image_22,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item6plus(),
    relief="flat"
)
button_22.place(
    x=877.0,
    y=446.0,
    width=16.0,
    height=16.0
)

button_image_23 = PhotoImage(
    file=relative_to_assets("button_23.png"))
button_23 = Button(
    image=button_image_23,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item5plus(),
    relief="flat"
)
button_23.place(
    x=547.0,
    y=447.0,
    width=16.0,
    height=16.0
)

button_image_24 = PhotoImage(
    file=relative_to_assets("button_24.png"))
button_24 = Button(
    image=button_image_24,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item4plus(),
    relief="flat"
)
button_24.place(
    x=330.0,
    y=447.0,
    width=16.0,
    height=16.0
)
window.resizable(False, False)
window.mainloop()
