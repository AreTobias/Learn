import sqlite3

# Create a database / connect to one
conn = sqlite3.connect('bruker.db')

# Create curson
c = conn.cursor()

c.execute("""CREATE TABLE ny_bruker (

        f_navn text,
        m_navn text,
        e_navn text,
        kommune text,
        e_post text,
        avdeling text,
        stilling text,
        fodselsdato text,
        mobilnummer integer
        )""")

# Commit changes
conn.commit()

# Close connection
conn.close()