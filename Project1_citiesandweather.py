Import sqlite3 as lite
import pandas as pd
cities = (('Las Vegas', 'VN'),('Atlanta', 'GA'),('New York City', 'NY'),
          ('Boston', 'MA'),('Chicago', 'IL'),('San Francisco', 'CA'),('Los Angeles','CA'))
weather =(('New York City', '2013', 'July', 'January', '62'),
          ('Boston', '2013', 'July', 'January', '59'),('Chicago', '2013', 'July', 'January', '59'))
con = lite.connect('getting_started.db')
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE cities (name text, state text);")
    cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold month text, average_high integer);"
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?", weather)
    cur.execute("SELECT name, state, year, warm_month, cold_month FROM cities INNER JOIN weather ON name = city")
    rows = cur.fetchall()
    dfc = pd. DataFrame(rows)
    cur.execute("SELECT city FROM weather WHERE warm_month = 'July'")
    hot_city = cur.fetchall()
    strhot = str(hot_city)
    print(strhot)
    

