from tkinter import *
def click(event):
    global scvalue
    text=event.widget.cget("text")
    # // to get text from widget
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        scvalue.update()
    else:
        scvalue.set(scvalue.get() + text)
        # add sc value with the text value
        screen.update()
    
root =Tk()
root.geometry("400x400")
root.title("Calculator")
scvalue = StringVar()
scvalue.set("")
screen=Entry(root,textvariable=scvalue,font="lucida 20 bold"
             )
screen.pack(fill=X,ipadx=8,pady=15,padx=10)
f1=Frame(root,bg="grey")
b1=Button(f1,text="9",padx=15,pady=5)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
# f1.pack()
# f1=Frame(root,bg="grey")
b1=Button(f1,text="8",padx=15,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",click)
# f1.pack()
# f1=Frame(root,bg="grey")
b1=Button(f1,text="7",padx=15,pady=5)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
f1.pack()
# new frame

f1=Frame(root,bg="grey")
b1=Button(f1,text="6",padx=15,pady=5)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
# f1.pack()
# f1=Frame(root,bg="grey")
b1=Button(f1,text="5",padx=15,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",click)
# f1.pack()
# f1=Frame(root,bg="grey")
b1=Button(f1,text="4",padx=15,pady=5)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
f1.pack()

# new frame for 1--2--3
f1=Frame(root,bg="grey")
b1=Button(f1,text="1",padx=15,pady=5)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
# f1.pack()
# f1=Frame(root,bg="grey")
b1=Button(f1,text="2",padx=15,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",click)
# f1.pack()
# f1=Frame(root,bg="grey")
b1=Button(f1,text="3",padx=15,pady=5)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
f1.pack()

# new frame for 0--*---
f1=Frame(root,bg="grey")
b1=Button(f1,text="0",padx=15,pady=5)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
# f1.pack()
# f1=Frame(root,bg="grey")
b1=Button(f1,text="*",padx=15,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",click)
# f1.pack()
# f1=Frame(root,bg="grey")
b1=Button(f1,text="-",padx=15,pady=5)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
f1.pack()
# new frame for % = /
f1=Frame(root,bg="grey")
b1=Button(f1,text="C",padx=15,pady=5)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
# f1.pack()
# f1=Frame(root,bg="grey")
b1=Button(f1,text="/",padx=15,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",click)
# f1.pack()
# f1=Frame(root,bg="grey")
b1=Button(f1,text="%",padx=15,pady=5)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
f1.pack()

# new frame for +  square and &
f1=Frame(root,bg="grey")
b1=Button(f1,text="+",padx=15,pady=15)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
# f1.pack()
# f1=Frame(root,bg="grey")
b1=Button(f1,text="**",padx=15,pady=15)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",click)
# f1.pack()
# f1=Frame(root,bg="grey")
b1=Button(f1,text="=",padx=15,pady=15)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
f1.pack()



root.mainloop()

# ---------SUCCESSFULLY EXCUTED-------#