import tkinter as tk

def add():
    first=int(x.get())
    second=int(y.get())
    result=first+second
    result_lable.config(text='operation result is:'+str(result))
def sub():
    first=int(x.get())
    second=int(y.get())
    result=first-second
    result_lable.config(text='operation result is:' + str(result))
def mul():
    first=int(x.get())
    second=int(y.get())
    result=first*second
    result_lable.config(text='operation result is:' + str(result))
def div():
    first=int(x.get())
    second=int(y.get())
    result=first/second
    result_lable.config(text='operation result is:' + str(result))

mainCalculator=tk.Tk()
mainCalculator.title('CALCULATOR')
heading_lable1=tk.Label(mainCalculator,text='enter the first number')
heading_lable1.pack()
x = tk.Entry(mainCalculator)
x.pack()

heading_lable2=tk.Label(mainCalculator,text='enter the second number')
heading_lable2.pack()
y = tk.Entry(mainCalculator)
y.pack()


heading_lable=tk.Label(mainCalculator,text='operation')
heading_lable.pack()
button1=tk.Button(mainCalculator,text='+',command=lambda:add())
button1.pack()
button2=tk.Button(mainCalculator,text='-',command=lambda:sub())
button2.pack()
button3=tk.Button(mainCalculator,text='*',command=lambda : mul())
button3.pack()
button4=tk.Button(mainCalculator,text='/',command=lambda : div())
button4.pack()
result_lable=tk.Label(mainCalculator,text='operation result is:')
result_lable.pack()
mainCalculator.mainloop()
