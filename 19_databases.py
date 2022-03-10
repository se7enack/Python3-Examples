import sqlite3

dbcon = sqlite3.connect("cars.db")

c = dbcon.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS cars (
    new text,
    make test,
    model text,
    year INTEGER
)""")

c.execute("INSERT INTO cars VALUES ('True', 'Tesla', 'Model 3', 2021) ")
c.execute("SELECT * FROM cars")
all = c.fetchall()

dbcon.commit()
dbcon.close()

for each in all:
    if each[0] == "True":
        x = "brand new"
    else:
        x = "used" 
    print("Enjoy your", x, each[1], each[2], str(each[3]) + "!")

