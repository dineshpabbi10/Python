import sqlite3
def create():
	connection = sqlite3.connect("xyz2.db")
	command = "CREATE TABLE TEST (NAME TEXT,AGE INT);"
	connection.execute(command)
	connection.commit()
	connection.close()

def insert():
	connection = sqlite3.connect("xyz2.db")
	print("""Enter the name""")
	x = input()
	print("""Enter the age""")
	y = int(input())
	# command = "INSERT INTO TEST (NAME,AGE) VALUES ({0} , {1})"
	connection.execute("INSERT INTO TEST (NAME,AGE) VALUES (? , ?)",(x,y))
	connection.commit()
	connection.close()

def view():
	connection = sqlite3.connect("xyz2.db")
	print("""Enter the name to search for data""")
	name = input()
	search = connection.cursor()
	search.execute("SELECT * FROM TEST WHERE NAME = %s"%(name))
	result = search.fetchall()
	for i in result:
		print("NAME:"+result[0]+"\n"+"Age:"+result[1])
	connection.commit()
	connection.close()

# create()
# insert()
view()