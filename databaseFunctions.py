import sqlite3

def connectToDatabase(dbName):
    dbName = 'db/' + dbName
    conn = sqlite3.connect(dbName)
    return conn.cursor()



def retrieveDataPoints(dbName):
    c = connectToDatabase(dbName)
    data = []
    counter = 1
    tableName = dbName[:-12].lower()
    for row in c.execute('SELECT device_name FROM ' + tableName):
        data.append(row)

    return [x[0] for x in data]
