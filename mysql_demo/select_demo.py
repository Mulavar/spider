import pymysql


user = 'root'
password = 'qwer1234'
db = 'spider'
charset = 'utf8mb4'

conn = pymysql.connect(user=user,
                       password=password,
                       db=db,
                       charset=charset)

with conn.cursor() as c:
    sql = 'select * from itcast;'
    c.execute(sql)
    result = c.fetchall() # fetchall()获得所有结果 fetchmany(size=None)获取一定数量的结果 fetchone()获取下一条
    for row in result:
        print('name=%s, title=%s, info=%s' % (row[1], row[2], row[3]))