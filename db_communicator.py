import mysql.connector

mydb = None

def authenticate(username, password):
  global mydb
  try:
    mydb = mysql.connector.connect(
      host="localhost",
      user=username,
      password=password
    )
    return "Success"
  except:
    return "Failure"
  
def insert(djs, showname, results):
  if mydb == None:
    return "Failed to connect"
  else:
    try:
      mycursor = mydb.cursor()
      mycursor.execute("use testdb")
      query = "insert into transcripts values (%s, %s, NULL, %s);"
      values = (djs, results, showname)
      mycursor.execute(query, values)
      mydb.commit()
      return "Success"
    except:
      return "Failed query"
    
def search(input):
    try:
      res = authenticate("root", "Vds1414umd16?")
      if res == "Success":
        mycursor = mydb.cursor()
        mycursor.execute("use testdb;")
        query = "select * from transcripts where speakers like %s or txt like %s or showname like %s;"
        values = ("%" + input + "%", "%" + input + "%", "%" + input + "%")
        mycursor.execute(query, values)
        result = mycursor.fetchall()
        return result
      else:
        return "Failed to connect"
    except:
      return "Failed query"

def ignore():
  mycursor = mydb.cursor()

  mycursor.execute("use testdb")
  mycursor.execute('insert into transcripts values ()')

  result = mycursor.fetchall()

  for i in result:
      print(i)