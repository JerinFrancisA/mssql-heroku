from flask import Flask, jsonify
import pyodbc
import datetime
import json

app = Flask(__name__)


def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()


conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-990NQR13;"
    "Database=rwf;"
    "Trusted_Connection=yes;"
)

@app.route('/caz', methods=['GET'])
def get_tasks():
    cursor = conn.cursor()
    result = cursor.execute("select * from dbo.sara")
    items = [dict(zip([key[0] for key in cursor.description], row))
             for row in result]
    response = json.dumps({'items': items},
                          sort_keys=True,
                          indent=1,
                          default=default,)
    return response


if __name__ == '__main__':
    app.run(debug=True)
