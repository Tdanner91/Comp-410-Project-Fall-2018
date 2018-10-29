import sqlite3


conn = sqlite3.connect('Resultsdummybase.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS results(result_name TEXT, in_use NUMERIC)')

def dynamic_data_entry():
    resultName = 'result'
    resultNum = 0
    resultInUse = 0

    for i in range(100):
        resultNameAndNum = resultName + str(i)
        c.execute("INSERT INTO results (result_name, in_use) VALUES (?, ?)",
        (resultNameAndNum, resultInUse))
        conn.commit()
    
    c.close()
    conn.close()

create_table()
dynamic_data_entry()