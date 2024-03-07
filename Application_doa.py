import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='bank')

cursor = cnx.cursor()


query = ("SELECT Name , Balance From Users")


cursor.execute(query)

for (Name , Balance) in cursor:
    print(Name , Balance)


cnx.close()
cnx.close