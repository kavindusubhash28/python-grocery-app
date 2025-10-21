import mysql.connector

__cnx = None

def get_sql_connection():
    global __cnx  # Corrected global declaration
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='0728',
                                         host='127.0.0.1',
                                         database='gs')
    return __cnx