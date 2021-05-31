 # Copyright (C) 2021 KeinShin@Github. All rights reserved


from system.datas_sqlite import c, conn
from sqlite3 import OperationalError


try:
 conn.execute(f"""CREATE TABLE afk (
  sed TEXT ,
  reason TEXT
  )""")
except OperationalError:
    pass


def update_afk(boolian, reason):
    c.execute("INSERT INTO afk VALUES (?, ?)", ((boolian, reason)))
    conn.commit()

def del_afk():
    c.execute(f"""SELECT * FROM afk""")
    a=c.fetchall()
    if a[0][0] == 'True':

      c.execute(f"DELETE  from afk WHERE sed = sed AND reason = reason")
      conn.commit()
    else:
      return None


def get_afk():
    c.execute(f"""SELECT * FROM afk""")
    a=c.fetchall()
    try:

     if a[0][0] == "True":
         return True
    except IndexError:
        return None
    else:
        return None

def get_reason():
    c.execute(f"""SELECT * FROM afk""")
    a=c.fetchall()
    if a[0][1]:
        
        return a[0][1]
    else:
        return None
print(get_afk())
# update_afk("True", "Sleep")
