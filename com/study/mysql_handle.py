import pymysql


def area(a, b):
    return a + b


def test_database():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "123456", "mysql")

    # 使用cursor() 方法创建一个游标对象
    cursor = db.cursor()

    # 使用execute() 方法执行sql查询
    cursor.execute("select version()")

    # 使用 fetchone() 方法获取单条数据
    data = cursor.fetchone()
    print("Database version : %s" % data)

    # cursor.execute("select * from t_repayment_event limit 1")
    db.close()


test_database()
