import json
from tkinter import *
import datetime as dt
from Functions import *

farbstil ="#6BB8F0"
schrift = "Impact"
schrift_farbe = "white"

hauptfenster = Tk()
hauptfenster.iconbitmap("kyubi.ico")
hauptfenster.configure(bg=farbstil)
hauptfenster.title("Stepometer für Vanny")



def steps():
    window1 = Tk()
    window1.configure(bg=farbstil)
    window1.title("Schritte gemacht !")
    window1.iconbitmap("kyubi.ico")

    steps_label = Label(window1, text=" Wieviele Schritte habe ich gemacht ?", bg= farbstil, font=schrift, fg=schrift_farbe)
    steps_eingabe = Entry(window1, bd=5, width=40, bg = "white")
    steps_berechnen = Button(window1, text = "Speichern", command=steps_save(steps_eingabe.get()), bg= farbstil)

    steps_label.grid(row =0 , column=0, padx=10, pady= 10)
    steps_eingabe.grid(row = 1, column=0,  padx=10, pady= 10)
    steps_berechnen.grid(row= 2, column= 0, padx=10, pady= 10)
   

#def button_drive():
#    window1 = tk.Toplevel(self)
#        window1.title("Fenster 1")

#def button_calc():
#    window1 = tk.Toplevel(self)
#        window1.title("Fenster 1")


#def button_data():
#    window1 = tk.Toplevel(self)
#        window1.title("Fenster 1")




label = Label(hauptfenster,text="Wie habe ich mich heute bewegt ?", bg=farbstil, font=schrift, fg=schrift_farbe)
gehen = PhotoImage(file="gehen.png", width=100 ,height= 100)
drive = PhotoImage(file="drive.png", width=100 ,height= 100)
calc= PhotoImage(file="data.png", width=100 ,height= 100)

button_steps = Button(hauptfenster, image=gehen, command=steps, bg = farbstil)
button_drive = Button(hauptfenster, image=drive, command=quit, bg = farbstil)
button_calc = Button(hauptfenster, image=calc, command=quit, bg= farbstil)
button_data = Button(hauptfenster, text="Aktuelle 7 Tage anzeigen", command=quit, bg= farbstil)

label.grid(row = 0,  column = 2, padx= 10, pady=10)
button_steps.grid(row= 1, column=0, padx= 10, pady=10)
button_drive.grid(row= 1, column=2,padx= 10, pady=10)
button_calc.grid(row= 1, column=3,padx= 10, pady=10)
button_data.grid(row = 2, column=2, padx= 10, pady=10,)


def steps():
    window1 = Toplevel
    window1.title("Schritte gemacht !")

#def button_drive():
#    window1 = tk.Toplevel(self)
#        window1.title("Fenster 1")

#def button_calc():
#    window1 = tk.Toplevel(self)
#        window1.title("Fenster 1")


#def button_data():
#    window1 = tk.Toplevel(self)
#        window1.title("Fenster 1")


    


mainloop()