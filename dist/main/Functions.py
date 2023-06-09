import json
import datetime as dt
import pandas as pd

now = dt.datetime.now()
global wochentag
wochentag = now.strftime("%A")
if wochentag == "Monday":
    wochentag = "Montag"
elif wochentag == "Tuesday":
    wochentag = "Dienstag"
elif wochentag == "Wednesday":
    wochentag = "Mittwoch"
elif wochentag == "Thursday":
    wochentag = "Donnerstag"
elif wochentag == "Friday":
    wochentag = "Freitag"
elif wochentag == "Saturday":
    wochentag = "Samstag"
elif wochentag == "Sunday":
    wochentag = "Sonntag"



global datei 
datei = "history.json"


def steps_save(steps):
    datentank = {}
    if steps == "":
        steps = 0
        
    datum = str(dt.date.today())
    try:
        with open(datei, "r") as f:
            datenbank = json.load(f)
    except:
        datenbank ={}   

    if datenbank[wochentag]["Datum"] == datum:
        datenbank[wochentag]["Gehen"] += int(steps)
        datenbank[wochentag]["Gesamt"] = datenbank[wochentag]["Gehen"] + datenbank[wochentag]["Fahren"]
    else:
        datenbank[wochentag]["Datum"] = datum
        datenbank[wochentag]["Gehen"] = int(steps) 
        datenbank[wochentag]["Gesamt"] = datenbank[wochentag]["Gehen"] + datenbank[wochentag]["Fahren"]  

    with open(datei,"w") as b:
        json.dump(datenbank,b)


def drive_save(drive):

    datentank = {}
    datum = str(dt.date.today())
    schritte = int(drive)*125
    print(schritte)
    try:
        with open(datei, "r") as f:
            datenbank = json.load(f)
    except:
        datenbank ={}   

    if datenbank[wochentag]["Datum"] == datum:
        datenbank[wochentag]["Fahren"] += int(schritte)

        datenbank[wochentag]["Gesamt"] = datenbank[wochentag]["Gehen"] + datenbank[wochentag]["Fahren"]
    else:
        datenbank[wochentag]["Datum"] = datum
        datenbank[wochentag]["Fahren"] = int(schritte)
        datenbank[wochentag]["Gesamt"] = datenbank[wochentag]["Gehen"] + datenbank[wochentag]["Fahren"]  

        
    with open(datei,"w") as b:
        json.dump(datenbank,b)

def calc_drive_time(steps):
    return int(steps)/125

def show_data():
    heute = str(dt.date.today())
    datenbank={}
    with open(datei, "r") as f:
        datenbank = json.load(f)
    
    return (datenbank[wochentag]["Gesamt"])
   
   
    
def show_7days_dict():
    datenbank ={}
    with open(datei,"r") as f:
        datenbank = json.load(f)

    return datenbank

def show_7days_chart():
    datenbank ={}
    with open(datei,"r") as f:
        datenbank = json.load(f)

    df = pd.DataFrame.from_dict(datenbank, orient='index')
    return df
  
def show_7days_print():
    datenbank={}

    with open(datei,"r") as f:
        datenbank = json.load(f)

    return(datenbank)

