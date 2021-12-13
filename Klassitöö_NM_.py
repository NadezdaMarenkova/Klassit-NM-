from tkinter import *
from module1 import *

dictionary=main("info.txt")

window=Tk()#Akna loomine
window.title("Нумерология - Число имени") #Akna pealkiri
window.geometry("1000x400") #Akna suurus
window.iconbitmap("numerology.ico")

lbl=Label(window, text="Введите имя", font="Arial 20", fg="#321B3E", bg="#A26588", width=1000, heigh=2) #Pealkiri
lbl.pack()
ent=Entry(window,fg="#151D55", bg="#E4ABAD", width=4, font="Arial 20") # ввод текста
ent.bind("<Return>")
ent.pack()
lbl1=Label(window, text="Значение Вашего имени", font="Arial 15", fg="#151D55", bg="#F9CCE1")

btn=Button(window, text="Хочу узнать!", font="Arial 15", fg="#151D55", bg="#F9CCE1", command=lambda:first_step(ent.get().lower(),lbl1))
btn.pack()
lbl1.pack() 



window.mainloop()
