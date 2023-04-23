import json
from tkinter import *
import tkinter as tk
import datetime as dt
from Functions import *
#from tkintertable import TableCanvas, TableModel



farbstil ="#39D8ED"
schrift = "Impact"
schrift_farbe = "#175DF5"

hauptfenster = Tk()
#hauptfenster.iconbitmap("kyubi.ico")
hauptfenster.configure(bg=farbstil)
hauptfenster.title("Stepometer für Vanny")
#tframe = Frame(master=hauptfenster)




def steps():
    window1 = Tk()
    window1.configure(bg=farbstil)
    window1.title("Schritte gemacht !")
    window1.iconbitmap("kyubi.ico")

    eingabevariable = tk.IntVar()

    def speicher_knopf():
        steps_save(steps_eingabe.get())
        window1.destroy()

    steps_label = Label(window1, text=" Wieviele Schritte hast du heute gemacht ?", bg= farbstil, font=schrift, fg=schrift_farbe)
    steps_eingabe = Entry(window1, bd=5, width=40, bg = "white", textvariable=eingabevariable)
    steps_berechnen = Button(window1, text = "Speichern", command=lambda:speicher_knopf(),bg= farbstil)

    steps_label.grid(row =0 , column=0, padx=10, pady= 10)
    steps_eingabe.grid(row = 1, column=0,  padx=10, pady= 10)
    steps_berechnen.grid(row= 2, column= 0, padx=10, pady= 10)

def drive():
    window2 = Tk()
    window2.configure(bg=farbstil)
    window2.title("Fahrrad gefahren !")
    window2.iconbitmap("kyubi.ico")

    eingabevariable = tk.IntVar()
    
    def speicher_knopf():
    
        drive_save(drive_eingabe.get())
        window2.destroy()

    drive_label = Label(window2, text=" Wieviele Minuten bist du heute gefahren ?", bg= farbstil, font=schrift, fg=schrift_farbe)
    drive_eingabe = Entry(window2, bd=5, width=40, bg = "white", textvariable=eingabevariable)
    drive_berechnen = Button(window2, text = "Speichern", command=lambda:speicher_knopf(),bg= farbstil)

    drive_label.grid(row =0 , column=0, padx=10, pady= 10)
    drive_eingabe.grid(row = 1, column=0,  padx=10, pady= 10)
    drive_berechnen.grid(row= 2, column= 0, padx=10, pady= 10)


  
def left():
    window3 = Tk()
    window3.configure(bg=farbstil)
    window3.title(" Wieviel noch fahren ?")
    window3.iconbitmap("kyubi.ico")

    eingabevariable = tk.IntVar() 

    def speicher_knopf():

        ergebnis = str(round(((calc_drive_time(left_eingabe.get()))/100)*60,2))
        left_ausgabe = Label(window3, text=ergebnis+ " min", bg= farbstil, font=schrift, fg=schrift_farbe)
        left_ausgabe.grid(row=3, column = 0, padx=10, pady=10)

    left_label = Label(window3, text="Wieviele Schritte fehlen dir noch?", bg= farbstil, font=schrift, fg=schrift_farbe)
    left_eingabe = Entry(window3, bd=5, width=40, bg = "white", textvariable=eingabevariable)
    left_berechnen = Button(window3, text = "Speichern", command=lambda:speicher_knopf(),bg= farbstil)
    
    left_label.grid(row =0 , column=0, padx=10, pady= 10)
    left_eingabe.grid(row = 1, column=0,  padx=10, pady= 10)
    left_berechnen.grid(row= 2, column= 0, padx=10, pady= 10)
 

def chart():
    window4 = Tk()
    window4.configure(bg=farbstil)
    window4.title("7 Tage-Auflistung ")
    window4.iconbitmap("kyubi.ico")

    ausgabe = Label(window4, text=show_7days_chart(), bg= farbstil, font=schrift, fg=schrift_farbe, justify=RIGHT) 
    #exit_knopf = Button(window4, text = "Beenden", command=quit, bg=farbstil)
    ausgabe.grid(row=0, column=0, padx=10,pady=10)  
    #exit_knopf.grid(row=1,column=0, padx=10,pady=10)


label = Label(hauptfenster,text="Wie habe ich mich heute bewegt ?", bg=farbstil, font=schrift, fg=schrift_farbe)
gehen = PhotoImage(file="gehen.png", width=100 ,height= 100)
fahren = PhotoImage(file="drive.png", width=100 ,height= 100)
calc= PhotoImage(file="data.png", width=100 ,height= 100)



button_steps = Button(hauptfenster, image=gehen, command=steps, bg = farbstil)
button_drive = Button(hauptfenster, image=fahren, command=drive, bg = farbstil)
button_calc = Button(hauptfenster, image=calc, command=left, bg= farbstil)
button_data = Button(hauptfenster, text="Aktuelle 7 Tage anzeigen", command=chart, bg= farbstil)

label.grid(row = 0,  column = 2, padx= 10, pady=10)
button_steps.grid(row= 1, column=0, padx= 10, pady=10)
button_drive.grid(row= 1, column=2,padx= 10, pady=10)
button_calc.grid(row= 1, column=3,padx= 10, pady=10)
button_data.grid(row = 2, column=2, padx= 10, pady=10,)




mainloop()