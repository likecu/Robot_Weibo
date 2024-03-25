import pymysql


def insert(user_id, user_name, user_comment, robot_result, comment_id):
    # 数据库连接配置
    config = {
        'user': 'root',  # 你的数据库用户名
        'password': 'qwe12345',  # 你的数据库密码
        'host': '192.168.123.11',  # 你的数据库地址，本地一般为 'localhost'
        'database': 'weibo',  # 你的数据库名称
    }

    # 创建数据库连接
    connection = pymysql.connect(**config)

    # 创建一个游标对象
    cursor = connection.cursor()

    # 定义要插入的数据
    data = {
        'user_id': user_id,
        'user_name': user_name,
        'user_comment': user_comment,
        'robot_result': robot_result,
        'comment_id': comment_id
    }

    # SQL 插入语句
    insert_query = """
    INSERT INTO weibo.robot (user_id, user_name, user_comment, robot_result, comment_id)
    VALUES (%(user_id)s, %(user_name)s, %(user_comment)s, %(robot_result)s, %(comment_id)s)
    """

    # 执行插入操作
    cursor.execute(insert_query, data)

    # 提交事务
    connection.commit()

    # 关闭游标和连接
    cursor.close()
    connection.close()
