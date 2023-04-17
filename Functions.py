import json
import datetime as dt
import pandas as pd

global datei 
datei = "test.json"

def steps_save(steps):
    datentank = {}
    datum = str(dt.date.today())
    try:
        with open(datei, "r") as f:
            datenbank = json.load(f)
    except:
        datenbank ={}   

    if datum in datenbank:
        steps += datenbank.get(datum)
        datenbank[datum] = steps  
    else:
        datenbank.update({datum: steps})

    with open(datei,"w") as b:
        json.dump(datenbank,b)

def drive_save(drive):
    datentank = {}
    datum = str(dt.date.today())
    schritte = drive*125
    try:
        with open(datei, "r") as f:
            datenbank = json.load(f)
    except:
        datenbank ={}   

    if datum in datenbank:
        schritte += datenbank.get(datum)
        datenbank[datum] = schritte
    else:
        datenbank.update({datum: schritte})
        
    with open(datei,"w") as b:
        json.dump(datenbank,b)

def calc_drive_time(steps):
    return steps/125

def show_data():
    heute = str(dt.date.today())
    datenbank={}

    with open(datei,"r") as f:
        datenbank = json.load(f)
    return datenbank[heute]

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
