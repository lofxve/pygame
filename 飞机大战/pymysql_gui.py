# 导入pymysql模块
import pymysql
# 账号登录
def select_mysql(zhanghao):
   # 连接database
   conn = pymysql.connect(host="localhost", user="root",password="root1",database="test",charset="utf8")
   # 得到一个可以执行SQL语句的光标对象
   cursor = conn.cursor()
   sql = "SELECT * from users WHERE zhanghao="+repr(zhanghao)+";"
   # 执行SQL语句
   cursor.execute(sql)
   # 获取单条查询数据
   ret = cursor.fetchone()
   cursor.close()
   conn.close()
   # 打印下查询结果
   return ret

# 账号注册
def insert_mysql(zhanghao,keyword):
   # 连接database
   conn = pymysql.connect(host="localhost", user="root", password="root1", database="test", charset="utf8")
   # 得到一个可以执行SQL语句的光标对象
   cursor = conn.cursor()
   sql = 'insert into users(zhanghao,keyword) values (%s,%s);'
   # 执行SQL语句
   data = (repr(zhanghao),repr(keyword),)
   try:
      cursor.execute(sql % data)
      conn.commit()
      return True
   except:
      return False
   cursor.close()
   conn.close()
# 修改排名数据
def update_mysql(id,score,rank):
   # 连接database
   conn = pymysql.connect(host="localhost", user="root", password="root1", database="test", charset="utf8")
   # 得到一个可以执行SQL语句的光标对象
   cursor = conn.cursor()
   # 定义将要执行的SQL语句
   sql = "update users set score=%s,rank_in=%s WHERE id=%s;"
   # 执行SQL语句
   data =  [score,rank,id]
   try:
      cursor.execute(sql,data)
      conn.commit()
      return True
   except:
      return False
   cursor.close()
   conn.close()

def select_mysql_orderby():
   # 连接database
   conn = pymysql.connect(host="localhost", user="root",password="root1",database="test",charset="utf8")
   # 得到一个可以执行SQL语句的光标对象
   cursor = conn.cursor()
   sql = "SELECT * FROM users ORDER BY rank_in DESC; "
   # 执行SQL语句
   cursor.execute(sql)
   # 获取全部数据
   ret = cursor.fetchall()
   cursor.close()
   conn.close()
   # 打印下查询结果
   return ret

def select_mysql_by_id(id):
   # 连接database
   conn = pymysql.connect(host="localhost", user="root",password="root1",database="test",charset="utf8")
   # 得到一个可以执行SQL语句的光标对象
   cursor = conn.cursor()
   sql = "SELECT * from users WHERE id=" + repr(id) + ";"
   # 执行SQL语句
   cursor.execute(sql)
   # 获取全部数据
   ret = cursor.fetchone()
   cursor.close()
   conn.close()
   # 打印下查询结果
   return ret

print(select_mysql("vjhyjkv"))
# print(insert_mysql("魏振东",'111'))
# print(update_mysql(40,25,36))
# print(select_mysql_orderby())
# print(select_mysql_by_id(1))