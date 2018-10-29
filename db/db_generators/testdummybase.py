import sqlite3

conn = sqlite3.connect('Testdummybase.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS test(test_name TEXT, in_use NUMERIC)')

def dynamic_data_entry():
    testName = 'test'
    testNum = 0
    testInUse = 0

    for i in range(100):
        testNameAndNum = testName + str(i)
        c.execute("INSERT INTO test (test_name, in_use) VALUES (?, ?)",
        (testNameAndNum, testInUse))
        conn.commit()
    
    c.close()
    conn.close()

create_table()
dynamic_data_entry()