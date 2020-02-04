from flask import Flask, jsonify
import pyodbc
from sqlalchemy import create_engine
import datetime
import decimal
import json
import pandas as pd

app = Flask(__name__)

def alchemyencoder(obj):
    """JSON encoder function for SQLAlchemy special classes."""
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
        return float(obj)

def example():
    print('am in')
    ser = 'LAPTOP-990NQR13'
    db = 'rwf'
    driver = 'SQL Server Native Client 11.0'
    dbc = f'mssql+pyodbc://@' + ser + '/' + db + \
        '?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'
    # f'mssql://{ser}/{db}?driver={driver}'
    # {un}:{pw}@
    engine = create_engine(dbc)
    print('in 2')
    conn = engine.connect()
    print('in 3')
    res = conn.execute("select * from dbo.sara")
    return json.dumps([dict(r) for r in res], default=alchemyencoder)

# def default(o):
#     if isinstance(o, (datetime.date, datetime.datetime)):
#         return o.isoformat()


# conn = pyodbc.connect(
#     "Driver={ODBC Driver 17 for SQL Server};"
#     "Server=LAPTOP-990NQR13;"
#     "Database=rwf;"
#     "Trusted_Connection=yes;"
# )


@app.route('/', methods=['GET'])
def get_tasks():
    # cursor = conn.cursor()
    # result = cursor.execute("select * from dbo.sara")
    # items = [dict(zip([key[0] for key in cursor.description], row))
    #          for row in result]
    # response = json.dumps({'items': items},
    #                       sort_keys=True,
    #                       indent=1,
    #                       default=default,)
    
    # return(example())
    return "HI"


if __name__ == '__main__':
    app.run(debug=True)
