import pymysql

connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '199711',
    database = 'student',
    port = 3306
)

cursor = connection.cursor()

cursor.execute('select 1')

result = cursor.fetchone()
print(result)

connection.close()