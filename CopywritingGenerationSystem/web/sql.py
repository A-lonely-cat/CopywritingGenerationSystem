import pymysql
import random

def select_random():
    # 连接到MySQL数据库
    cnx = pymysql.connect(
        host='your_host',
        user='your_username',
        password='your_password',
        database='your_database'
    )

    # 创建游标
    cursor = cnx.cursor()


    # 获取表中数据数量 (表名未修改)
    count_query = "SELECT COUNT(*) FROM your_table"
    cursor.execute(count_query)
    count = cursor.fetchone()[0]

    # 随机选择一个数据行
    random_index = random.randint(0, count - 1)

    # 查询随机选择的数据行
    random_query = "SELECT * FROM your_table LIMIT %s, 1"
    cursor.execute(random_query, random_index)
    random_data = cursor.fetchone()

    # 输出随机选择的数据
    print(random_data)


# # 执行查询 (表名未修改)
# query = "SELECT * FROM your_table"
# cursor.execute(query)

# # 获取结果
# results = cursor.fetchall()
# for row in results:
#     print(row)



    # 关闭游标和连接
    cursor.close()
    cnx.close()