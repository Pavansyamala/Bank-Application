import mysql.connector as c
# import numpy as np 
class ATM :

    def __init__(self):

        mydb = c.connect(
        host = "localhost",
        user = "abc",
        password = "password")
        self.cursor = mydb.cursor()

        self.cursor.execute("CREATE DATABASE IF NOT EXISTS db")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS db.Customer_Details(name VARCHAR(255) , phonenumber VARCHAR(10) , password VARCHAR(255) , balance INT)")

        self.menu()

    def menu(self) : 
        self.user_nput = input('''
        Choose the service you want from the following : 
        1 : Registration
        2 : Bank Balance 
        3 : With drawal 
        4 : Credit Amount 
        5 : Change Password
        6 : Exit
        ''')

        if self.user_nput == '1' :
            self.register()
        elif self.user_nput == '2' :
            self.Bank_Balance()
        elif self.user_nput == '3' :
            self.Withdraw_Amount()
        elif self.user_nput == '4' :
            self.Credit_Amount()
        elif self.user_nput == '5' :
            self.Change_Password()
        else :
            print("Have a Great Day !") 
            
    
    def register(self):
        user_name = input("Enter your Name : ")
        phonenumber = input("Enter phone number for your registration : ")
        password = input("Choose Your Passord : ")
        balance = 500
        self.cursor.execute(
            'INSERT INTO db.Customer_Details(name, phonenumber, password, balance) VALUES (%s, %s, %s, %s)',
            (user_name, phonenumber, password, balance)
        )
        print('Registration Succesfull')
        self.menu() 
    
    def Change_Password(self):

        name = input("Enter your User Name")
        old_password = input("Enter Old Password : ")
        self.cursor.execute('SELECT password FROM db.Customer_Details WHERE name = %s' , (name , ))
        for i in cursor : 
            a = i[0]
        if a == self.old_password :
            self.new_password = input("Enter New Password : ")
            self.cursor("UPDATE db.Customer_Details SET password = %s WHERE name = %s" , (new_password , name))

            print(" *** Password Updated Succesfully *** ")
            self.menu() 
        else :
            print("Entered Wrong Password Sorry !!! ")  

    def Bank_Balance(self) :
        name = input("Enter your User Name")
        password = input("Enter Password : ")

        self.cursor.execute(
            'SELECT password FROM db.Customer_Details WHERE name = %s',
            (name,)
        )
        for i in self.cursor : 
            a = i[0]
        if a == password :
            self.cursor.execute('SELECT balance FROM db.Customer_Details WHERE name = %s' , (name,)) 
            for i in self.cursor :
                print("Your Account Balance is " , i[0])
        else : 
            print('Oops ! Invalid User Name or Password Try Again !!!')
        self.menu()
    
    def Credit_Amount(self) : 
        name = input("Enter your User Name")
        password = input("Enter Password : ")

        self.cursor.execute('SELECT password FROM db.Customer_Details WHERE name = %s', (name ,))
        for i in self.cursor : 
            a = i[0]
        if a == password :
            amount = int(input("Enter Credit Amount : "))
            self.cursor.execute('UPDATE db.Customer_Details SET balance = balance +  %d  WHERE name = %s' , (amount , name)) 
            print("Amount Credited Succesfully")
        else : 
            print('Oops ! Invalid User Name or Password Try Again !!!') 
        
        self.menu() 

    def Withdraw_Amount(self) :
        name = input("Enter your User Name")
        password = input("Enter Password : ")

        self.cursor.execute('SELECT password FROM db.Customer_Details WHERE name = %s ' , (name , ))
        for i in self.cursor : 
            a = i[0]
        if a == password :
            amount = int(input("Enter Credit Amount : "))
            self.cursor.execute("SELECT balance FROM db.Customer_Details WHERE name = %s" , (name , ))
            for i in self.cursor : 
                balace = i[0]
            if balance >= amount :
                self.cursor.execute('UPDATE db.Customer_Details SET balance = balance -  %d  WHERE name = %s' , (amount , name)) 
                print("Amount Debited Succesfully")
            else :
                print("No Sufficient Funds")
        else : 
            print('Oops ! Invalid User Name or Password Try Again !!!') 
        
        self.menu()  

obj = ATM() 