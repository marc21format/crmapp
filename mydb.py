import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'bc123yama',

	)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crmdatabase")

print("All Done!")