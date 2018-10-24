import sqlite3
import random

conn = sqlite3.connect('DUTdummybase.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS dut(device_name TEXT, in_use NUMERIC)')

def dynamic_data_entry():
    deviceName = 'device'
    deviceNum = 0
    deviceInUse = 0

    for i in range(10):
        deviceNameAndNum = deviceName + str(i)
        c.execute("INSERT INTO dut (device_name, in_use) VALUES (?, ?)",
        (deviceNameAndNum, deviceInUse))
        conn.commit()
    
    c.close()
    conn.close()

create_table()
dynamic_data_entry()