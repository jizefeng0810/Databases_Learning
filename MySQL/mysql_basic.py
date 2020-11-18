# 导入pymysql
import pymysql

if __name__=='__main__':
    # 连接mysql数据库的服务
    connc = pymysql.Connect(user='root',password='***',database='person',charset='utf8')
    # 创建游标对象
    cur = connc.cursor()
    # 编写sql语句
    sql = 'select * from info;'
    # 使用游标对象去执行sql
    cur.execute(sql)
    # 获取结果
    result = cur.fetchall()
    print(result)
    try:
        # 增加数据 jizefeng 25 男
        c_sql = 'insert into info values(%s,%s,%s,%s);'
        add_data = [0, 'jizefeng', 25, '男']
        cur.execute(c_sql, add_data)
        connc.commit()  # 提交操作
    except Exception as e:
        print(e)
        connc.rollback()    # 数据回滚
    finally:
        # 查询表
        sql = 'select * from info;'
        cur.execute(sql)
        result = cur.fetchall()
        print(result)

        # 关闭游标对象
        cur.close()
        # 关闭连接
        connc.close()

