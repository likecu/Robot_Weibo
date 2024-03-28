import pymysql


class WeiboDatabase:
    @staticmethod
    def get_database_cursor():
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
        return connection, cursor

    @staticmethod
    def save_robot_comment(user_id, user_name, user_comment, robot_result, comment_id):
        connection, cursor = WeiboDatabase.get_database_cursor()

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

    @staticmethod
    def get_comment_count(config_name) -> int:
        connection, cur = WeiboDatabase.get_database_cursor()
        query_sql = f"SELECT count(*) FROM weibo.robot WHERE comment_id='{config_name}'"
        cur.execute(query_sql)
        rows = cur.fetchall()
        try:
            return rows[0][0]
        except IndexError:
            return 0

    @staticmethod
    def query(config_name):
        """Query the content field based on the config_name."""
        connection, cur = WeiboDatabase.get_database_cursor()
        query_sql = f"SELECT content FROM config WHERE config_name='{config_name}'"
        cur.execute(query_sql)
        rows = cur.fetchall()
        try:
            return rows[0][0]
        except IndexError:
            return 0

    @staticmethod
    def insert_exe_log(types, exe_id, message):
        connection, cursor = WeiboDatabase.get_database_cursor()

        # 定义要插入的数据
        data = {
            'type': types,
            'exe_id': exe_id,
            'message': message,
        }

        # SQL 插入语句
        insert_query = """
         INSERT INTO `exe_log` (`type`, `exe_id`, `message`)
         VALUES (%s, %s, %s)
         """

        # 执行插入操作
        cursor.execute(insert_query, (types, exe_id, message))

        # 提交事务
        connection.commit()

        # 关闭游标和连接
        cursor.close()
        connection.close()

    @staticmethod
    def get_user_id_since_date():
        connection, cursor = WeiboDatabase.get_database_cursor()
        try:
            # SQL查询语句
            sql = "SELECT id, since_date FROM user;"
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            # 遍历结果并添加到列表中
            user_list = [{"id": row[0], "since_date": row[1]} for row in results]
            return user_list
        except pymysql.MySQLError as e:
            print(f"数据库操作出错：{e}")
            return []
        finally:
            # 关闭游标和连接
            cursor.close()
            connection.close()

    @staticmethod
    def update_since_date(user_id, new_since_date):
        connection, cursor = WeiboDatabase.get_database_cursor()
        try:
            # SQL 更新语句
            update_query = """
               UPDATE user
               SET since_date = %s
               WHERE id = %s
               """
            # 执行更新操作
            cursor.execute(update_query, (new_since_date, user_id))

            # 提交事务
            connection.commit()

            # 返回影响的行数
            return cursor.rowcount
        except pymysql.MySQLError as e:
            print(f"数据库操作出错：{e}")
            return 0
        finally:
            # 关闭游标和连接
            cursor.close()
            connection.close()


# 使用示例
if __name__ == "__main__":
    users = WeiboDatabase.get_user_id_since_date()
    print(users)
