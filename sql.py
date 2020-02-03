import pyodbc
import datetime
import json


def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()


def read(conn):
    print("Read")
    cursor = conn.cursor()
    result = cursor.execute("select * from dbo.sara")
    items = [dict(zip([key[0] for key in cursor.description], row))
             for row in result]
    print(json.dumps({'items': items},
                     sort_keys=True,
                     indent=1,
                     default=default,))
    print(len(items))


conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-990NQR13;"
    "Database=rwf;"
    "Trusted_Connection=yes;"
)

read(conn)
