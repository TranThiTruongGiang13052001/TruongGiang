import pyodbc 
# def read(conn):
#     print("read")
#     cursor = conn.cursor()
#     cursor.execute("select * from Branch")
#     for row in cursor:
#         print(f'row = {row}')

conn = pyodbc.connect(
    'Driver={ODBC Driver 17 for SQL Server;'
    'Server=PC;'
    'Database =Bank;'
    'Trusted_Connection = yes;'

)
print(pyodbc.drivers())
# read(conn)
# conn.close()