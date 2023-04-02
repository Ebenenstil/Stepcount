from tkinter import *

# Die folgende Funktion soll ausgeführt werden, wenn
# der Benutzer den Button Klick me anklickt

def umrechnung(eingabe):
    return(float(eingabe)*125)

def prozentsatz(input):
    rechnung = (float(input) / 10000) * 100
    if rechnung > 100 :
        return ("Damit hast du dein Tagesziel um: " + str(rechnung-100)+ "% übertroffen.")
    else:
        return("Damit hast du dein Tagesziel zu: "+ str(rechnung) + " % erreicht!")

def button_action():
    entry_text = eingabefeld.get()
    schritte = umrechnung(eingabefeld.get())

    if (entry_text == ""):
        ausgabefeld.config(text="Bitte gib ein wieviele Minuten du gefahren bist!")
    else:
        entry_text = "Du hast umgerechnet ganze: " + str(schritte)+ " Schritte mit dem Fahrrad erreicht!\n " +prozentsatz(schritte)
        ausgabefeld.config(text=entry_text)

farbstil = "white"
fenster = Tk()
fenster.iconbitmap("bike.ico")
fenster.configure(bg=farbstil)
fenster.title("Minuten auf dem Fahrrad -> Schritte")

# Anweisungs-Label
my_label = Label(fenster, text="Wie lange bist du gefahren ? ",background=farbstil)

# In diesem Label wird nach dem Klick auf den Button der Benutzer
# mit seinem eingegebenen Namen begrüsst.
ausgabefeld = Label(fenster, background=farbstil)

# Hier kann der Benutzer eine Eingabe machen
eingabefeld = Entry(fenster, bd=5, width=40, background=farbstil)

welcom_button = Button(fenster, text="Berechnen", command=button_action, background=farbstil)
exit_button = Button(fenster, text="Beenden", command=fenster.quit, background=farbstil)


# Nun fügen wir die Komponenten unserem Fenster hinzu
my_label.grid(row = 0, column = 0)
eingabefeld.grid(row = 0, column = 1)
welcom_button.grid(row = 2, column = 0)
exit_button.grid(row = 2, column = 1, padx=10, pady=10)
ausgabefeld.grid(row = 3, column = 0, columnspan = 2)


#print("Wieviel Minuten bist du Fahrrad gefahren?")

#schritte = umrechnung(input())

#print("Du hast umgerechnet ganze: " + str(schritte)+ " Schritte mit dem Fahrrad erreicht!")
#print(prozentsatz(schritte))

mainloop()