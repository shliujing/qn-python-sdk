# coding:utf8

import mysql.connector

# refer: http://www.runoob.com/python3/python-mysql-connector.html

## 主要关注 curd create,update,read,delete。

# 数据库，表（excel），  99% 增删改查 数据行

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Aa111111",
    database="runoob_db"
)

mycursor = mydb.cursor()

# 创建数据库
# mycursor.execute("CREATE DATABASE runoob_db")

# 输出所有数据库列表
# mycursor.execute("SHOW DATABASES")
#
# for x in mycursor:
#     print(x)

# 创建数数据表
# mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")

# 修改表结构
# mycursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# 插入数据
# sql1 = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val1 = ("RUNOOB11111a", "https://www.runoob.com")
# mycursor.execute(sql1, val1)
# mydb.commit()  # 数据表内容有更新，必须使用到该语句
# print(mycursor.rowcount, "记录插入成功。")
#
# # 查找所有数据
mycursor.execute("SELECT * FROM sites")
myresult = mycursor.fetchall()  # fetchall() 获取所有记录
for x in myresult:
    print(x)
#
# # 只查询1条
# mycursor.execute("SELECT * FROM sites")
# myresult = mycursor.fetchone()
# print(myresult)
#
# # 条件查询
sql = "SELECT * FROM sites WHERE name ='RUNOOB'"  # 模糊查询 sql = "SELECT * FROM sites WHERE url LIKE '%oo%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
#
# 条件+占位符
sql = "SELECT * FROM sites WHERE name = %s"
na = ("RUNOOB",)
mycursor.execute(sql, na)

# 删除
sql = "DELETE FROM sites WHERE name = 'stackoverflow'"  # 或使用 %s 占位，防注入
mycursor.execute(sql)
mydb.commit()

# 更新
sql = "UPDATE sites SET name = 'ZH' WHERE name = 'Zhihu'"
mycursor.execute(sql)
mydb.commit()



# 删除表
# sql = "DROP TABLE IF EXISTS sites"  # 删除数据表 sites
# mycursor.execute(sql)
