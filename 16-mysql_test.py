#!/usr/bin/env python3

# 导入mysql驱动
import pymysql

# 建立数据库连接，并打开游标
conn = pymysql.connect(user='root', password='6121108', database='test')
cursor = conn.cursor()

# 创建user表
cursor.execute('create table if not exists user (id varchar(20) primary key, name varchar(20))')

# 插入一行记录
cursor.execute('insert into user (id, name) values (%s, %s)', ['2', 'Jason'])
cursor.rowcount

# 提交事务
conn.commit()
cursor.close()

# 运行查询
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()

print(values)

# 关闭cursor和conn
cursor.close()
conn.close()
