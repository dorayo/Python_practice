#!/usr/bin/env python3

from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()

# 定义User对象
class User(Base):
    # 表的名字
    __tablename__ = 'user'

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # ‘多’的一方的book表，是通过外键关联到user表的
    user_id = Column(String(20), ForeignKey('user.id'))

# 初始化数据库连接
engine = create_engine('mysql+pymysql://root:6121108@localhost:3306/test')

# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

# 创建DBSession对象
session = DBSession()

# 创建user对象
book1 = Book(id='1', name='Hakcers', user_id='7')
book2 = Book(id='2', name='Painters', user_id='7')
book3 = Book(id='3', name='Thinker', user_id='7')
user1 = User(id='7', name='Alex')

# 添加到session
session.add(user1)
session.add(book1)
session.add(book2)
session.add(book3)

# 保存到数据库
session.commit()

# 查询
user = session.query(User).filter(User.id=='7').one()
print('type:', type(user))
print('name', user.name)
print(user.books[0].name)
print(user.books)

# 关闭session
session.close()
