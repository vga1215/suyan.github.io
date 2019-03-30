# -*_ coding:utf-8 -*-
from sqlalchemy import *
from sqlalchemy import event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import hashlib

#定义数据库的账号、端口、密码、数据库名，使用的连接模块，这里用的是postgresql
engine = create_engine(
    'postgresql://postgres:8265884@192.168.1.202/web',echo=True #是否输出数据库操作过程，很方便调试
)

"""
mercurial (3.7.3)
pip (8.1.2)
psycopg2 (2.6.1)
setuptools (21.0.0)
SQLAlchemy (1.0.13)
wheel (0.29.0)
"""

#定义一个函数，用来获取sqlalchemy的session
def bindSQL():
    return scoped_session(sessionmaker(bind=engine))

Base = declarative_base()

class User(Base):
    __tablename__ = "shawner"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)
    email = Column(String(32), unique=True)
    password = Column(String(32))
    superuser = Column(Boolean, default=False)

metadata = Base.metadata
password_prefix = "Ad%cvcsadefr^!alpthe"
def setPassword(target, value, oldvalue, initiator):
    if value == oldvalue:
        return oldvalue
    
    return hashlib.md5("%s%s"  % (password_prefix, value)).hexdigest()
event.listen(User.password, "set", setPassword, retval=True)

def get_or_create(session,model,**kwargs):
    if "defaults" in kwargs:
        defaults = kwargs["defaults"]
        del kwargs["defaults"]
    else:
        defaults = {}

    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance, False
    else:
        kwargs.update(defaults)
        instance = model(**kwargs)
        session.add(instance)
        session.flush()
        session.refresh(instance)
        return instance, True

def initModel():
    metadata.create_all(engine)     #通过engine连接创建所有元数据
    db = bindSQL()  #获取sqlalchemy的session
    obj, created = get_or_create(
        db,
        User,    #从基类创建的User对象
        name="administrator",
        defaults={
            "email": "31525291@qq.com",
            "password": "administrator",
            "superuser":   True
        }
    )
    db.commit()
    db.remove()

if __name__ == "__main__":
    initModel() #运行python models.py就会自动创建定义的所有表
