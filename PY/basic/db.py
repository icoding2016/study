"""

Python SQL:
  mysql
  psycopg2
  ...
Python Non-SQL
  

# SQL:
The basic process for db operation
- Create connection
- Create cursor
- Create Query string
- Execute the query
- Commit to the query
- Close the cursor
- Close the connection
e.g.
    mydb = MySQLdb.connect(host=host, user=user, passwd=passwd, db=database, charset="utf8")
    cursor = mydb.cursor()
    query = "INSERT INTO tablename (text_for_field1, text_for_field2, text_for_field3, text_for_field4) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (field1, field2, field3, field4))
    mydb.commit()
    cursor.close()
    mydb.close()



"""

import psycopg2 



def try_postgresql():
    psycopg2.connect
