from tkinter import *

window_1= Tk()
window_1.title("Hello from tkinter")
window_1.geometry('800x600')

def ButtonPressTracker():
    ButtonPressTracker.counter += 1
    print("mohannad ", ButtonPressTracker.counter)
ButtonPressTracker.counter =0

label_1=Label(window_1, text="Match Status", fg="red" , font =('verdana',30))
label_1.pack(side=TOP)

b1= Button(window_1 , text ="Exit",font =('verdana',20), bd='10', background='grey', fg="white" , command =window_1.destroy)
b1.pack(side=BOTTOM)

photo_1 = PhotoImage(file='Egy.png')
photo_1 = photo_1.subsample(2,2)
l_1=Label(window_1  ,image=photo_1)
l_1.place(x=70,y=70)

photo_2 = PhotoImage(file='belg.png')
photo_2 = photo_2.subsample(6,6)
l_2=Label(window_1  ,image=photo_2)
l_2.place(x=480,y=70)

l1 = Label(window_1 , text = "Egypt",font =('verdana',15))
l1.place(x=140,y=250)
c1=Canvas(window_1,width=100, height=100)
c1.create_rectangle(50, 20, 150, 80, fill="White")
c1.place(x=100,y=308)

l2 = Label(window_1 , text = "Belgium",font =('verdana',15))
l2.place(x=540,y=250)
c2=Canvas(window_1,width=100, height=100)
c2.create_rectangle(50, 20, 150, 80, fill="White") 
c2.place(x=520,y=308)

window_1.mainloop()

