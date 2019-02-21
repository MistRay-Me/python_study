import pymysql


def area(a, b):
    return a + b


def test_database():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "testone")

    # 使用cursor() 方法创建一个游标对象
    cursor = db.cursor()

    # 使用execute() 方法执行sql查询
    cursor.execute("select version()")

    # 使用 fetchone() 方法获取单条数据
    data = cursor.fetchone()
    print("Database version : %s" % data)

    cursor.execute("select * from t_test_index")
    test_index = cursor.fetchone()

    ids = test_index[0]
    print(ids)
    create_time = test_index[1]
    print(create_time)
    create_user = test_index[2]
    print(create_user)
    update_time = test_index[3]
    print(update_time)
    update_user = test_index[4]
    print(update_user)
    order_id = test_index[5]
    print(order_id)
    trans_type = test_index[6]
    print(trans_type)
    status = test_index[7]
    print(status)
    trans_time = test_index[8]
    print(trans_time)
    print(test_index)
    result = area(order_id, status)
    print(result)
    db.close()


test_database()
