import marshal
import mysql.connector



conn = mysql.connector.connect(

    host="archisi-db.cqozp8kc5eik.eu-west-3.rds.amazonaws.com",
    user="adminSI",
    port=3306,
    password="mypasswordarchis!",
    database="Schema1"

)

cursor = conn.cursor()



    
#data = marshal.load(open("binaryDataChamp/dataLigue1", "rb"))
data = marshal.load(open("binaryDataChamp/dataLiga", "rb"))
#data = marshal.load(open("binaryDataChamp/dataBundes", "rb"))
#data = marshal.load(open("binaryDataChamp/dataSerieA", "rb"))

for i in data:
    for j in i[0]:
        print (i[0][j])
    print('//////////')



