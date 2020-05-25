from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.geometry("600x600")
root.title("Ny brukerskjema")
root.iconbitmap('C:/Users/are0906/Downloads/logo300ddv.png')

# Databases

# Create a database / connect to one
conn = sqlite3.connect('ny_bruker.db')

# Create curson
c = conn.cursor()

# Create Table
#c.execute("""CREATE TABLE ny_bruker_ (
#
#        f_navn text,
#        m_navn text,
#        e_navn text,
#        kommune text,
#        avdeling text,
#        tittel text,
#        mobilnummer integer,
#        fodselsnummer integer
#
#        )""")


# Commit changes
conn.commit()

# Close connection
conn.close()


# Create boxes
f_navn = Entry(root, width=30)
f_navn.grid(row=0, column=1, padx=20)

m_navn = Entry(root, width=30)
m_navn.grid(row=1, column=1, padx=20)

e_navn = Entry(root, width=30)
e_navn.grid(row=2, column=1, padx=20)

kommune = Entry(root, width=30)
kommune.grid(row=3, column=1, padx=20)

avdeling = Entry(root, width=30)
avdeling.grid(row=4, column=1, padx=20)

stilling = Entry(root, width=30)
stilling.grid(row=5, column=1, padx=20)

tlf_nummer = Entry(root, width=30)
tlf_nummer.grid(row=6, column=1, padx=20)

fodselsdato = Entry(root, width=30)
fodselsdato.grid(row=7, column=1, padx=20)


# Create Texbox Labe

f_navn_label = Label(root, text="Fornavn:")
f_navn_label.grid(row=0, column=0)

m_navn_label = Label(root, text="Mellomnavn:")
m_navn_label.grid(row=1, column=0)

e_navn_label = Label(root, text="Etternavn:")
e_navn_label.grid(row=2, column=0)

kommune_label = Label(root, text="Kommune:")
kommune_label.grid(row=3, column=0)

avdeling_label = Label(root, text="Avdeling/Lokasjon:")
avdeling_label.grid(row=4, column=0)

stilling_label = Label(root, text="Stilling:")
stilling_label.grid(row=5, column=0)

tlf_nummer_label = Label(root, text="Mobilnummer (Jobb/privat):")
tlf_nummer_label.grid(row=6, column=0)

fodselsdato_label = Label(root, text="Fødselsdato (mnd/dato):")
fodselsdato_label.grid(row=7, column=0)




# Knapper

def registrer():


    # Create a database / connect to one
    conn = sqlite3.connect('ny_bruker.db')

    # Create curson
    c = conn.cursor()

    #insert into table
    c.execute("INSERT INTO ny_bruker VALUES (:f_navn, :m_navn, :e_navn, :kommune, :avdeling, :stilling, :tlf_nummer, :fodselsdato)",
        {
            'f_navn': f_navn.get(),
            "m_navn": m_navn.get(),
            "e_navn": e_navn.get(),
            "kommune": kommune.get(),
            "avdeling": avdeling.get(),
            "stilling": stilling.get(),
            "tlf_nummer": tlf_nummer.get(),
            "fodselsdato": fodselsdato.get()
        }

              )

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

    f_navn.delete(0, END)
    m_navn.delete(0, END)
    e_navn.delete(0, END)
    kommune.delete(0, END)
    avdeling.delete(0, END)
    stilling.delete(0, END)
    tlf_nummer.delete(0, END)
    fodselsdato.delete(0, END)

def sjekk_info():
    # Create a database / connect to one
    conn = sqlite3.connect('ny_bruker.db')

    # Create curson
    c = conn.cursor()

    # Sjekk info i DB
    c.execute("SELECT *, oid FROM ny_bruker")
    informasjon = c.fetchall()
    print(informasjon)

    vis_informasjon = ''
    for informasjon in informasjon:
        vis_informasjon += str(informasjon) + "\n"


    informasjon_label = Label(root, text=vis_informasjon)
    informasjon_label.grid(row=11, column=0, columnspan=2)

    #epost = f"{f_navn.get()}.{e_navn.get()}@{kommune.get()}.kommune.no"

    
    #if m_navn.get() == None:
    #        epost = f"{f_navn.get()}.{e_navn.get()}@{kommune.get()}.kommune.no"
    #else:
    #        epost = f"{f_navn.get()}.{m_navn.get()}.{e_navn.get()}@{kommune.get()}.kommune.no"


    #epost_label = Label(root, text=epost)
    #epost_label.grid(row=12, column=1)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()



registrer_bruker = Button(root, text="Registrer bruker", command=registrer)
registrer_bruker.grid(row=10, column=0, columnspan=2, padx=20, pady=20, ipadx=137)

dobbelt_sjekk = Button(root, text="Sjekk info", command=sjekk_info)
dobbelt_sjekk.grid(row=9, column=0, columnspan=2, padx=20, pady=20, ipadx=137)




root.mainloop()