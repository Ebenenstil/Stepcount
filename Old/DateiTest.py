import datetime as dt



datei = {"Daten":{
    "Datum":"2023-04-16",
    "Gehen":0,
    "Fahren":0,
    "Schritte":0}
    }


heute = str(dt.date.today())
print(heute)


fahren ="100"
gehen = "100"
schritte =fahren + gehen


print(datei.keys())
print(datei.values())
print("-------")
print(datei["Daten"])