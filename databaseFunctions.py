import sqlite3

def connectToDatabase(dbName):
    dbName = 'db/' + dbName
    conn = sqlite3.connect(dbName)
    return conn.cursor()



def retrieveDataPoints(dbName):
    c = connectToDatabase(dbName + '.db')

    tableName = dbName[:-9].lower()
    selectionCriteria = getSelectionCriteria(tableName)

    data = []

    for row in c.execute('SELECT ' + selectionCriteria + ' FROM ' + tableName):
        data.append(row)

    return [x[0] for x in data]

def getSelectionCriteria(tableName):

    if tableName == 'dut':
        return 'device_name'
    elif tableName == 'test':
        return 'test_name'
    elif tableName == 'results':
        return 'result_name'
