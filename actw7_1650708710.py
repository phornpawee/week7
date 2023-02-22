import tkinter as tk

def mainwindow() :
    root = tk.Tk()
    root.title("Week7 : My Python GUI Application")
    root.geometry('700x700+400+30')
    root.option_add('*font','garamond 16')
    root.config(bg='pink')
    root.grid_rowconfigure((0,2),weight=1)
    root.grid_rowconfigure(1,weight=5)
    root.grid_columnconfigure(0,weight=1)
    root.grid_columnconfigure(1,weight=5)
    return(root)

def layout() :
    #top side
    top.grid(row=0,column=0,columnspan=2,sticky='news')
    top.grid_columnconfigure((0,1,2),weight=1)
    top.grid_rowconfigure(0,weight=1)
    #bottom side
    bottom.grid(row=2,columnspan=2,sticky="news")
    bottom.rowconfigure(0,weight=1)
    bottom.columnconfigure((0,1),weight=1)
    #left side
    left.grid(row=1,column=0,sticky="news")
    left.columnconfigure(0,weight=1)
    left.rowconfigure((0,1,2,3,4,5),weight=1)
    #right side
    right.grid(row=1,column=1,sticky="news")
    right.rowconfigure((0,1,2),weight=1)
    right.columnconfigure((0,1),weight=1)

def topside(top) :
    tk.Button(top,text="Cake Menu",image=b1,compound='top',command=cakeclick).grid(row=0,column=0,sticky="news")
    tk.Button(top,text="Drink Menu",image=b2,compound='top',command=drinkclick).grid(row=0,column=1,sticky="news")
    tk.Button(top,text="Check out",image=b3,compound='top').grid(row=0,column=2,sticky="news")

def bottomside() :
    tk.Button(bottom,text="Reset Submit").grid(row=0,column=0,sticky="news")
    tk.Button(bottom,text="Exit Program",image=b4,compound="left",command=root.quit).grid(row=0,column=1,sticky="news")

# def leftside() :


def cakeclick() :
    pos = 0
    for i,menu in enumerate(menu1) :
        tk.Label(left,text=menu,bg="#F6F7C1").grid(row=pos,ipadx=15)
        tk.Label(left,image=cakes[i],bg="#F6F7C1").grid(row=pos+1,ipadx=15,ipady=15)
        tk.Label(right,text="( Price : " + str(price1[i]) + " ) Amount : ",bg='#FFE15D').grid(row=i,column=0,sticky="e",ipadx=20)
        tk.Spinbox(right,from_=0,to=100,width=10,justify="center").grid(row=i,column=1)
        pos += 2

def drinkclick() :
    pos = 0
    for i,menu in enumerate(menu2) :
        tk.Label(left,text=menu,bg="#F6F7C1").grid(row=pos)
        tk.Label(left,image=drinks[i],bg="#F6F7C1").grid(row=pos+1)
        tk.Label(right,text="( Price : " + str(price2[i]) + " ) Amount : ",bg='#FFE15D').grid(row=i,column=0,sticky="e",ipadx=20)
        tk.Spinbox(right,from_=0,to=100,width=10,justify="center").grid(row=i,column=1)
        pos += 2

def resetclick() :
    for i in range(len(menu1)) :
        amt1[i].set(0)
        amt2[i].set(0)

root = mainwindow()
#create top,left,right,bottom,checkout frame widgets
top = tk.Frame(root,bg='#FFB84C')
left = tk.Frame(root,bg='#F6F7C1')
right = tk.Frame(root,bg='#FFE15D')
bottom = tk.Frame(root,bg="#FFB84C")
checkoutframe = tk.Frame(root,bg='#EBC7E6')
#define images for using in this program
img1 = tk.PhotoImage(file="image/drink1.png")
img2 = tk.PhotoImage(file="image/drink2.png")
img3 = tk.PhotoImage(file="image/drink3.png")
img4 = tk.PhotoImage(file="image/cake3.png")
img5 = tk.PhotoImage(file="image/cake2.png")
img6 = tk.PhotoImage(file="image/cake4.png")
b1 = tk.PhotoImage(file="image/cake-button.png")
b2 = tk.PhotoImage(file="image/drink-button.png")
b3 = tk.PhotoImage(file="image/checkout.png")
b4 = tk.PhotoImage(file="image/exit.png")
drinks = [img1,img2,img3]
cakes = [img4,img5,img6]
menu1 = [' Strawberry Cake '," Cheese   Cake  ","Newyork Cheese Cake"]
menu2 = ['| Orange   Mixed |',' Lemonade Mixed ',"| Mojito  Miexd  Berry |"]
price1 = [145,120,130]
price2 = [120,100,90]
amt1 = [tk.IntVar() for x in menu1] #spy of cake
amt2 = [tk.IntVar() for x in menu2] #spy of drink
total = 0
discount = 0
net = 0
layout()
topside(top)
bottomside()
root.mainloop()