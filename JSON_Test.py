import json
import pandas as pd


montag = {"Datum":"2023-04-16","Gehen":0,"Fahren":0,"Gesamt":0}
dienstag = {"Datum":"2023-04-16","Gehen":0,"Fahren":0,"Gesamt":0}
Mittwoch = {"Datum":"2023-04-16","Gehen":0,"Fahren":0,"Gesamt":0}
donnerstag = {"Datum":"2023-04-16","Gehen":0,"Fahren":0,"Gesamt":0}
freitag = {"Datum":"2023-04-16","Gehen":0,"Fahren":0,"Gesamt":0}
samstag = {"Datum":"2023-04-16","Gehen":0,"Fahren":0,"Gesamt":0}
sonntag = {"Datum":"2023-04-16","Gehen":0,"Fahren":0,"Gesamt":0}

history = {
    "Montag":montag,
    "Dienstag":dienstag,
    "Mittwoch":Mittwoch,
    "Donnerstag":donnerstag,
    "Freitag":freitag,
    "Samstag":samstag,
    "Sonntag":sonntag}


history["Montag"]["Fahren"]= 100
history["Dienstag"]["Gehen"]=111
history["Dienstag"]["Fahren"]=222
history["Dienstag"]["Gesamt"]=history["Dienstag"]["Gehen"]+history["Dienstag"]["Fahren"]
zähler = 0

for tage in history:
    zähler += history[tage]["Gesamt"]

with open ("history.json","w") as file:
    json.dump(history, file)

testhistory = {}

with open ("history.json","r") as file:
    testhistory=json.load(file)

print(testhistory)
    
df = pd.DataFrame(data=testhistory,)

print(df)