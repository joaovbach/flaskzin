import sqlite3

banco = sqlite3.connect("banco.db")
cur = banco.cursor()

cur.execute("CREATE TABLE teste(a, b, c)")
#cur.execute("INSERT INTO accounts VALUES ('joao','123','false')")
banco.commit()
#print(cur.execute("SELECT * FROM accounts").fetchall())
