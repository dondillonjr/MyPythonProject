import mysql.connector

######## Connection to mySQL Database
Host = "ec2-18-216-119-62.us-east-2.compute.amazonaws.com"
User = "root"
Password="myPassword"
Database="validate_users"

mydb = mysql.connector.connect(host=Host, user=User, password=Password, database=Database)

QUERY1 = "Select * from legal_users"
QUERY2 = "Select username, password, email from legal_users"
QUERY3 = "select * from legal_users"

def query_all(query):
    mycursor = mydb.cursor()

    mycursor.execute(query)

    myresult = mycursor.fetchall()

    print(f"\n{'#'*50}\nConnecting to Host {Host} \n{'#'*50}")

    for x in myresult:
        print(x)

    mycursor.close();

def query_one(query):
    mycursor = mydb.cursor()

    mycursor.execute(query)
    ############# FETCH ONLY ONE ROW ############
    myresult = mycursor.fetchone()

    print(f"\n{'#'*50}\nConnecting to Host {Host} \n{'#'*50}")
    print(myresult)

############### MAIN ######
query_all(QUERY1)
query_all(QUERY2)
query_one(QUERY3)

