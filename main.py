import mysql.connector

connection = mysql.connector.connect(
    user = "root",
    database = "database",
    password = "Counterayu#234"
)

cursor = connection.cursor()

name = input("Welcome to our Banking System. What is your name?")
print(f"Hey {name}, nice to see you today!")

questions = input("Are you here to Check balance, Deposit or Withdraw?")

if questions == "Check balance":
    print("Enter a Account number and Pin")
    accnum = input("Account Number: ")
    pin = input("Pin: ")
    addData = (f"SELECT balance FROM userinfo WHERE accnum = '{accnum}")
    cursor.execute(addData)
    balance = 200
    print(f"Your balance is {balance}")

if questions == "Deposit":
    print("Enter a Account number and Pin")
    accnum= input("Account Number: ")
    pin = input("Pin: ")
    amount = input("Amount to deposit: ")
    addData = (f"UPDATE userinfo SET balance = balance + {amount} WHERE accnum = '{accnum}")
    cursor.execute(addData)
    print("Balance updated!")

if questions == "Withdraw":
    print("Enter a Account number and Pin")
    accnum = input("Account Number: ")
    pin = input("Pin: ")
    amount = input("Amount to withdraw: ")
    addData = (f"SELECT balance FROM userinfo WHERE accnum = '{accnum}")
    cursor.execute(f"UPDATE userinfo SET balance = balance - {amount} WHERE accnum = '{accnum}")
    print("Withdraw complete!")


for item in cursor:
    print(item)

cursor.close()
connection.close()


