#Umrechnung von Sitzfahrrad Dauer in Schritte

def umrechnung(eingabe):
    return(float(eingabe)*125)

def prozentsatz(input):
    rechnung = (float(input) / 10000) * 100
    if rechnung > 100 :
        return ("Damit hast du dein Tagesziel um: " + str(rechnung-100)+ "% übertroffen.")
    else:
        return("Damit hast du dein Tagesziel zu: "+ str(rechnung) + " % erreicht!")

print("Wieviel Minuten bist du Fahrrad gefahren?")
benutzereingabe = input()
schritte = umrechnung(benutzereingabe)

print("Du hast umgerechnet ganze: " + str(schritte)+ " Schritte mit dem Fahrrad erreicht!")
print(prozentsatz(schritte))
