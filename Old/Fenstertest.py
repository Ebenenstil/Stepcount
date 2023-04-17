from tkinter import * #Import für Fenstersteuerung
import datetime as dt #Import für Datumsfunktion
import json           #Import für Datenspeicherung : Json
import os
import sys

if os.environ.get("Display","") =="":
    print("no display found. Using :0.0")
    os.environ.__setitem__("Display", ":0.0")
    
#Funktion zum Umrechnen von Fahrzeit zu Schritten
def umrechnung(eingabe):
    return(float(eingabe)*125)

#Funktion um den Prozentsatz zu 10k zu berechnen und bewertung auszugeben
def prozentsatz(input):
    rechnung = (float(input) / 10000) * 100
    if rechnung > 100 :
        return ("Damit hast du dein Tagesziel um: " + str(rechnung-100)+ "% übertroffen.")
    else:
        return("Damit hast du dein Tagesziel zu: "+ str(rechnung) + " % erreicht!")

#Funktion für Knopf-Drücken
def button_action():
    entry_text = eingabefeld.get()
    schritte = umrechnung(eingabefeld.get())

    if (entry_text == ""):
        ausgabefeld.config(text="Bitte gib ein wieviele Minuten du gefahren bist!")
    else:
        entry_text = "Du hast umgerechnet ganze: " + str(schritte)+ " Schritte mit dem Fahrrad erreicht!\n " +prozentsatz(schritte)
        ausgabefeld.config(text=entry_text)
    gesamt = float(datenbank[str(dt.date.today())]) + schritte
    datenbank[str(dt.date.today())] = str(gesamt)

    with open("data2.json","w") as b:
        json.dump(datenbank,b)

#Dictornary Datenbank wird aus JSON Datei eingelesen oder als leeres Dict.erstellt
try:
    with open("data.json","r") as f:
        datenbank = json.load(f)
except:
    datenbank ={}

#Parameter für die Optik des Fensters wird bestimmt
farbstil = "white"
fenster = Tk()
fenster.iconbitmap("bike.ico")
fenster.configure(bg=farbstil)
fenster.title("Minuten auf dem Fahrrad -> Schritte")

# Anweisungs-Label
my_label = Label(fenster, text="Wie lange bist du gefahren ? ",background=farbstil)

# Ausgabefeld wo die Ergebnisse der Berechnungen gezeigt werden
ausgabefeld = Label(fenster, background=farbstil)

# Eingabefeld für die Berechnung
eingabefeld = Entry(fenster, bd=5, width=40, background=farbstil)

#Buttons für Berechnung und Beenden erstellen
berechnen_button = Button(fenster, text="Berechnen", command=button_action, background=farbstil)
exit_button = Button(fenster, text="Beenden", command=fenster.quit, background=farbstil)


# Aufgabei und ausrichtung der Fenster row/column = Zeile und Spalte. padx/pady= Abstand zu anderen Elementen.
my_label.grid(row = 0, column = 0)
eingabefeld.grid(row = 0, column = 1)
berechnen_button.grid(row = 2, column = 0)
exit_button.grid(row = 2, column = 1, padx=10, pady=10)
ausgabefeld.grid(row = 3, column = 0, columnspan = 2)


mainloop()