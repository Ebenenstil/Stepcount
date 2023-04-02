import datetime as dt
import json



datenbank =  {
    "2023-04-02" : "8523",
    "2023-04-01" : "8523",
    "2023-03-31" : "10000",
    "2023-03-30" : "2022",

}

print (datenbank)

#if str(dt.date.today()) == "2023-04-02":

#j = json.dumps(datenbank, indent=4)

#with open('test.json', 'w') as f:
#    print (f, j)
    
with open("test.json","w") as f:
    json.dump(datenbank, f)