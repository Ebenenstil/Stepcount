import json
import datetime as dt
import pandas as pd

def steps_save(steps):
    datentank = {}
    datum = str(dt.date.today())
    try:
        with open("data01.json", "r") as f:
            datenbank = json.load(f)
    except:
        datenbank ={}   

    if datum in datenbank:
        steps += datenbank.get(datum)
        datenbank[datum] = steps  
    else:
        datenbank.update({datum: steps})
        


    with open("data01.json","w") as b:
        json.dump(datenbank,b)

def drive_save(drive):
    datentank = {}
    datum = str(dt.date.today())
    schritte = drive*125
    try:
        with open("data01.json", "r") as f:
            datenbank = json.load(f)
    except:
        datenbank ={}   

    if datum in datenbank:
        schritte += datenbank.get(datum)
        datenbank[datum] = schritte
    else:
        datenbank.update({datum: schritte})
        


    with open("data01.json","w") as b:
        json.dump(datenbank,b)

def calc_drive_time(steps):
    return steps/125

def show_data():
    heute = str(dt.date.today())
    datenbank={}

    with open("data01.json","r") as f:
        datenbank = json.load(f)
    return datenbank[heute]

def show_7days_chart():
    with open("alles.json","r") as f:
        json.load(datenbank,f)
    df = pd.DataFrame(datenbank)

def show_7days_print():
    datenbank={}

    with open("data01.json","r") as f:
        datenbank = json.load(f)

    print(datenbank)

#data = {'Name': ['a', 'b', 'c'], 'Age': [10, 11, 12]}