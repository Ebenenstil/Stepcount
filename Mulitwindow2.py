import tkinter as tk
import json
import datetime as dt


class MainWindow(tk.Tk):
    farbstil = "white"
    def __init__(self):

        super().__init__()
        self.title("Auswahlmenü mit Inhalten")

        self.icon1 = tk.PhotoImage(file="icon1.png")
        self.menu_item1 = tk.Button(self, image=self.icon1, text="Menüpunkt 1", compound="top", command=self.open_window1)
        self.menu_item1.pack(side="left", padx=10, pady=10)
        self.eingabefeld = tk.Entry()
        self.icon2 = tk.PhotoImage(file="icon2.png")
        self.menu_item2 = tk.Button(self, image=self.icon2, text="Menüpunkt 2", compound="top", command=self.open_window2)
        self.menu_item2.pack(side="left", padx=10, pady=10)
        try:
            with open("data.json","r") as f:
                datenbank = json.load(f)
        except:
            datenbank ={}

    def umrechnung(eingabe):
        return(float(eingabe)*125)
        
    def open_window1(self):
        farbstil="white"
        window1 = tk.Toplevel(self)
        window1.title("Fenster 1")
        
        # Erstelle ein Label-Widget und platziere es in Fenster 1
        label1 = tk.Label(window1, text="Inhalt für Menüpunkt 1")
        label1.grid(row = 0, column = 0, padx=10, pady=10)
        eingabefeld = tk.Entry(window1, bd=5, width=40)
        eingabefeld.grid(row = 2, column = 0, padx=10, pady=10)
      
        ausgabefeld = tk.Label(window1, background=farbstil)

        # Ausgabefeld 2 für die Fehlende Schritte
        ausgabefeld2 = tk.Label(window1, background=farbstil)


        #Buttons für Berechnung und Beenden erstellen
        berechnen_button = tk.Button(window1, text="Berechnen",command=self.button_action(), background=farbstil)
  
        exit_button = tk.Button(window1, text="Beenden", command=window1.quit, background=farbstil)


        # Aufgabei und ausrichtung der Fenster row/column = Zeile und Spalte. padx/pady= Abstand zu anderen Elementen.
        
        eingabefeld.grid(row = 0, column = 1)
        berechnen_button.grid(row = 2, column = 0)
        exit_button.grid(row = 2, column = 1, padx=10, pady=10)
        ausgabefeld.grid(row = 3, column = 0, columnspan = 2)
        ausgabefeld2.grid(row = 4, column =0,columnspan = 2)

    def button_action(self):
        eingabe = 111
        #eingabe = self.eingabefeld.get()
        schritte = float(eingabe)*125
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
        
    def open_window2(self):
        window2 = tk.Toplevel(self)
        window2.title("Fenster 2")
        
        # Erstelle ein Label-Widget und platziere es in Fenster 2
        label2 = tk.Label(window2, text="Inhalt für Menüpunkt 2")
        label2.pack(padx=10, pady=10)

  
        

     # Füge hier die Elemente für das neue Fenster hinzu
    # Anweisungs-Label

try:
    with open("data.json","r") as f:
        datenbank = json.load(f)
except:
    datenbank ={}
   

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
