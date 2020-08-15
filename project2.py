from tkinter import *
import random
import time


scr=Tk()
scr.geometry("1600x800+0+0")
scr.title("Resaurant Management System")

text_Input=StringVar()
operator=""

Tops=Frame(scr,width=1600,bg="green",relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(scr,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(scr,width=300,height=700,bg="green",relief=SUNKEN)
f2.pack(side=RIGHT)
#--------------------------time
localtime=time.asctime(time.localtime(time.time()))
#---------------------info

lblInfo=Label(Tops,font=("default",50),text="Restaurant Management System",fg="blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo=Label(Tops,font=("default",20),text=localtime,fg="blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)
#----------------------calculator
def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")
def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""


def Ref():
    x=random.randint(100,500)
    randomRef=str(x)
    rand.set(randomRef)

def qExit():
    scr.destroy()

def Reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Momos.set("")
    Pancake.set("")
    Drinks.set("")
    Noodles.set("")
    Cakes.set("")
    Chips.set("")
    Sweets.set("")

    
txtDisplay=Entry(f2,font=("arial",20),textvariable=text_Input,bd=30,insertwidth=4,bg="steel blue",justify='right')
txtDisplay.grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("default",20),text="7",
            bg="powderblue",command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("default",20),text="8",
            bg="powderblue",command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("default",20),text="9",
            bg="powderblue",command=lambda:btnClick(9)).grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("default",20),text="+",
            bg="powderblue",command=lambda:btnClick("+")).grid(row=2,column=3)

#------------------------------------

btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("default",20),text="4",
            bg="powderblue",command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("default",20),text="5",
            bg="powderblue",command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("default",20),text="6",
            bg="powderblue",command=lambda:btnClick(6)).grid(row=3,column=2)

Subraction=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("default",20),text="-",
            bg="powderblue",command=lambda:btnClick("-")).grid(row=3,column=3)
#--------------------------------------------------


btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("default",20),text="1",
            bg="powderblue",command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("default",20),text="2",
            bg="powderblue",command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("default",20),text="3",
            bg="powderblue",command=lambda:btnClick(3)).grid(row=4,column=2)

Multiply=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("default",20),text="*",
            bg="powderblue",command=lambda:btnClick("*")).grid(row=4,column=3)

#------------------------------------------------------

btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("default",20),text="0",
            bg="powderblue",command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("default",20),text="C",
            bg="powderblue",command=btnClearDisplay).grid(row=5,column=1)
btnEquals=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("default",20),text="=",
            bg="powderblue",command=btnEqualsInput).grid(row=5,column=2)

Division=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("default",20),text="/",
            bg="powderblue",command=lambda:btnClick("/")).grid(row=5,column=3)

#----------------------------------restaurant -------------
rand=StringVar()
Fries=StringVar()
Burger=StringVar()
Momos=StringVar()
Pancake=StringVar()
Drinks=StringVar()
Noodles=StringVar()
Cakes=StringVar()
Chips=StringVar()
Sweets=StringVar()

lblRefrence=Label(f1,font=("default",16),text="Refrence",bd=16,anchor='w')
lblRefrence.grid(row=0,column=0)
txtRefrence=Entry(f1,font=("default",16),textvariable=rand,bd=10,insertwidth=4,
                  bg="powder blue",justify='right')
txtRefrence.grid(row=0,column=1)

lblFries=Label(f1,font=("default",16),text="Fries",bd=16,anchor='w')
lblFries.grid(row=1,column=0)
txtFries=Entry(f1,font=("default",16),textvariable=Fries,bd=10,insertwidth=4,
                  bg="powder blue",justify='right')
txtFries.grid(row=1,column=1)

lblBurger=Label(f1,font=("default",16),text="Burger",bd=16,anchor='w')
lblBurger.grid(row=2,column=0)
txtBurger=Entry(f1,font=("default",16),textvariable=Burger,bd=10,insertwidth=4,
                  bg="powder blue",justify='right')
txtBurger.grid(row=2,column=1)

lblMomos=Label(f1,font=("default",16),text="Momos",bd=16,anchor='w')
lblMomos.grid(row=3,column=0)
txtMomos=Entry(f1,font=("default",16),textvariable=Momos,bd=10,insertwidth=4,
                  bg="powder blue",justify='right')
txtMomos.grid(row=3,column=1)

lblPancake=Label(f1,font=("default",16),text="Pancake",bd=16,anchor='w')
lblPancake.grid(row=4,column=0)
txtPancake=Entry(f1,font=("default",16),textvariable=Pancake,bd=10,insertwidth=4,
                  bg="powder blue",justify='right')
txtPancake.grid(row=4,column=1)


#------------------------------2--------


lblDrinks=Label(f1,font=("default",16),text="Drinks",bd=16,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks=Entry(f1,font=("default",16),textvariable=Drinks,bd=10,insertwidth=4,
                  bg="powder blue",justify='left')
txtDrinks.grid(row=0,column=3)


lblNoodles=Label(f1,font=("default",16),text="Noodles",bd=16,anchor='w')
lblNoodles.grid(row=1,column=2)
txtNoodles=Entry(f1,font=("default",16),textvariable=Noodles,bd=10,insertwidth=4,
                  bg="powder blue",justify='right')
txtNoodles.grid(row=1,column=3)

lblCakes=Label(f1,font=("default",16),text="Cakes",bd=16,anchor='w')
lblCakes.grid(row=2,column=2)
txtCakes=Entry(f1,font=("default",16),textvariable=Cakes,bd=10,insertwidth=4,
                  bg="powder blue",justify='right')
txtCakes.grid(row=2,column=3)

lblChips=Label(f1,font=("default",16),text="Chips",bd=16,anchor='w')
lblChips.grid(row=3,column=2)
txtChips=Entry(f1,font=("default",16),textvariable=Chips,bd=10,insertwidth=4,
                  bg="powder blue",justify='right')
txtChips.grid(row=3,column=3)

lblSweets=Label(f1,font=("default",16),text="Sweets",bd=16,anchor='w')
lblSweets.grid(row=4,column=2)
txtSweets=Entry(f1,font=("default",16),textvariable=Sweets,bd=10,insertwidth=4,
                  bg="powder blue",justify='right')
txtSweets.grid(row=4,column=3)

#----------------------------------------------------------
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=("default",16),width=10,
                text="Total",bg="powder blue",command=Ref).grid(row=7,column=1)
btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=("default",16),width=10,
                text="Reset",bg="powder blue",command=Reset).grid(row=7,column=2)
btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=("default",16),width=10,
                text="Exit",bg="powder blue",command=qExit).grid(row=7,column=3)

