
import mysql.connector

insert_query1="insert into selenium values(29, 'Sdet', 'Sammy', '2022-11-24')"
update_query="update selenium set tutorial_author='Ronny' where tutorial_id=2"
delete_query="delete from selenium where tutorial_id=23"

try:
    con = mysql.connector.connect(host='localhost', port=3306, user='root', passwd='Mysql@12', database='oct282022')
    curs = con.cursor()
    curs.execute(insert_query1)
    curs.execute(update_query)
    curs.execute(delete_query)
    con.commit()
    con.close()
except:
    print('cannot connect')
