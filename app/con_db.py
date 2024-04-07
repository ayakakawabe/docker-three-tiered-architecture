import mysql.connector

cnx = mysql.connector.connect(
    user='sample_user',
    password='sample_user',
    host='db',
    database='sample_db')

with cnx.cursor() as cursor:
    result = cursor.execute("SELECT * FROM sample_table")
    rows = cursor.fetchall()
    print("sample_table")
    for rows in rows:
        print(rows)