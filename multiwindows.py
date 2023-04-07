import tkinter as tk
from tkinter import *

class MainWindow(tk.Tk):
    farbstil ="White"
    def __init__(self):
        
        super().__init__()
        self.title("Auswahlmenü mit Icons")
        
        # Erstelle ein Menü-Element mit einem Icon und Text
        #self.icon1 = tk.PhotoImage(file="icon.png")
        self.menu_item1 = tk.Button(self, text="Menüpunkt 1", compound="top", command=self.open_window1)
        self.menu_item1.pack(side="left", padx=10, pady=10)
        
        # Erstelle ein weiteres Menü-Element mit einem anderen Icon und Text
        #self.icon2 = tk.PhotoImage(file="icon2.png")
        self.menu_item2 = tk.Button(self, text="Menüpunkt 2", compound="top", command=self.open_window2)
        self.menu_item2.pack(side="left", padx=10, pady=10)
        
    def open_window1(self):
        # Öffne ein neues Fenster, wenn Menüpunkt 1 ausgewählt wird
       
        
        window1 = tk.Toplevel(self)
        window1.iconbitmap("bike.ico")
        window1.configure(bg=farbstil)
        farbstil="white"
        window1.title("Fenster Fahrrad")
        
        label1 = tk.Label(window1, text="Inhalt für Menüpunkt 1")
        label1.pack(padx=10, pady=10)

        my_label = tk.Label(window1, text="Wie lange bist du gefahren ? ",background=farbstil)

        # Ausgabefeld wo die Ergebnisse der Berechnungen gezeigt werden
        ausgabefeld = Label(window1, background=farbstil)

        # Ausgabefeld 2 für die Fehlende Schritte
        ausgabefeld2 = Label(window1, background=farbstil)

        # Eingabefeld für die Berechnung
        eingabefeld = Entry(window1, bd=5, width=40, background=farbstil)

        #Buttons für Berechnung und Beenden erstellen
        berechnen_button = Button(window1, text="Berechnen", command=button_action, background=farbstil)
        exit_button = Button(window1, text="Beenden", command=window1.quit, background=farbstil)


        # Aufgabei und ausrichtung der Fenster row/column = Zeile und Spalte. padx/pady= Abstand zu anderen Elementen.
        my_label.grid(row = 0, column = 0)
        eingabefeld.grid(row = 0, column = 1)
        berechnen_button.grid(row = 2, column = 0)
        exit_button.grid(row = 2, column = 1, padx=10, pady=10)
        ausgabefeld.grid(row = 3, column = 0, columnspan = 2)
        ausgabefeld2.grid(row = 4, column =0,columnspan = 2)

        # Füge hier die Elemente für das neue Fenster hinzu
        
    def open_window2(self):
        # Öffne ein neues Fenster, wenn Menüpunkt 2 ausgewählt wird
        window2 = tk.Toplevel(self)
        window2.title("Fenster 2")
    
    def button_action():
        entry_text = eingabefeld.get()
        schritte = umrechnung(eingabefeld.get())
        gesamt = float(datenbank[str(dt.date.today())]) + schritte
        datenbank[str(dt.date.today())] = str(gesamt)


        if (entry_text == ""):
            ausgabefeld.config(text="Bitte gib ein wieviele Minuten du gefahren bist!")
        else:
            entry_text = "Du hast umgerechnet ganze: " + str(schritte)+ " Schritte mit dem Fahrrad erreicht!\n + Tageswert:{gesamt}"
            ausgabefeld.config(text=entry_text)
            f_schritte = 10000 - float(gesamt)
            fehlende_schritte = "Dir fehlen noch: " + str(f_schritte) +" oder in Fahrzeit: "+ str(f_schritte/125) +" Minuten." 
            ausgabefeld2(text=fehlende_schritte)

        with open("data.json","w") as b:
            json.dump(datenbank,b)
        

        # Füge hier die Elemente für das neue Fenster hinzu
    # Anweisungs-Label
   




if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
   
  