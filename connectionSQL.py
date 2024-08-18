import mysql.connector
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="9769",
    database="s4mpr",
    port="3306"
)

cursor = connection.cursor()