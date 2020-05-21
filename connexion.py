## pip install mysql-connector
import mysql.connector
 
conn = mysql.connector.connect(host="archisi-db.cqozp8kc5eik.eu-west-3.rds.amazonaws.com",
                               user="adminSI", password="mypasswordarchis!", 
                               database="Schema1")
cursor = conn.cursor()
cursor.execute("SHOW TABLES")

for row in cursor:
   print(row)
 
# Opérations à réaliser sur la base ...
 
conn.close()