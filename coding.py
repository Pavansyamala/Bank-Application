import mysql.connector as c 

connection = c.connect(
    host = 'localhost',
    user = 'abc',
    password = 'password'
)

cursor = connection.cursor()

#cursor.execute("SHOW DATABASES")
# cursor.execute("CREATE DATABASE IF NOT EXISTS db")
# cursor.execute("CREATE TABLE IF NOT EXISTS db.Customer_Details(name VARCHAR(255) , phonenumber VARCHAR(10) , password VARCHAR(255))")
# cursor.execute('''INSERT INTO db.Customer_Details(name , phonenumber , password) 
#          VALUES ("Kasa Pavan" , "9347649447" , "Syamala@123")
#         ''')
# cursor.execute('SELECT password FROM db.Customer_Details WHERE name = "Kasa Pavan"')
cursor.execute("SELECT * FROM db.Customer_Details")
for i in cursor :
    print(i[0])