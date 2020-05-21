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

"""
class test(object):
    
    #data = marshal.load(open("dataLigue1", "rb"))
    #data = marshal.load(open("dataLiga", "rb"))
    #data = marshal.load(open("dataBundes", "rb"))
    data = marshal.load(open("dataSerieA", "rb"))

    for i in data:
        for j in i[0]:
            print (i[0][j])
        print('//////////')



    """