2 lines (26 sloc)  652 Bytes

import sqlite3

def create():
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
       userid INT PRIMARY KEY,
       fname TEXT,
       lname TEXT,
       gender TEXT);
    """)
    conn.commit()
    conn.commit()

def sqlrequest(request):
    cur.execute(request)
    conn.commit()

def clear():
    cur.execute("DROP TABLE IF EXISTS users;")

def sqlwrite():
    cur.execute("SELECT * FROM users;")
    all_results = cur.fetchall()
    print(all_results)

conn = sqlite3.connect('orders.db')
cur = conn.cursor()
clear()

while True:
    txt = input("Введите запрос ")
    sqlrequest(txt)
    sqlwrite()