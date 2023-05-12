# 准备json文件，里边内容为：{"name": "tom", "age": "28"}

import json
import pymysql
import emoji

# 连接数据库
conn = pymysql.connect(
    host='localhost',
    # 端口号
    port=3306,
    # 用户名
    user='root',
    # 密码
    passwd='123123123',
    # 数据库名称
    # db='weibo',
    # 字符编码格式
    charset='utf8')

cur = conn.cursor()

# # 插入的表名
table = 'weibo.tweet_userprofile'

#
# json在我本地的路径
jsonPath = '/Users/yunpeng/Desktop/content/WeiboSpider/output/tweet_spider_20230513000022.jsonl'

# 打开json文件
with open(jsonPath, 'r', encoding='utf_8_sig') as f:
    # 读取json文件
    for line in f.readlines():
        # 读取json文件格式为python的dict字典类型
        dic = json.loads(line)
        # 剔除键值为空的list
        for item in dic:
            # 如果数组为空，则复制为null
            if isinstance(dic[item], list):
                if len(dic[item]) == 0:
                    dic[item] = 'null'
            # 如果键值为dict, 则转化为字符串
            if isinstance(dic[item], dict):
                dic[item] = str(dic[item])
            # 去除 label_desc的特殊字符
            if isinstance(dic[item], list):
                dic[item] = ''.join(dic[item]).replace('，', ' & ')

        # 拼接key值为：name,age
        keys = ','.join(dic.keys())

        # 将value值存为列表类型：['tom', '28'] <class 'list'>
        valuesList = [dici for dici in dic.values()]

        # 剔除emoji表情
        for i in range(len(valuesList)):
            if isinstance(valuesList[i], str):
                valuesList[i] = emoji.demojize(valuesList[i])

        # 将value值存为元组类型：('tom', '28')
        valuesTuple = tuple(valuesList)

        # 拼接values为：%s, %s
        values = ', '.join(['%s'] * len(dic))

        # 插入sql语句
        insertSql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
        print(insertSql, valuesTuple)
        #
        # 执行建表
        # 放在sql文件内执行
        # cur.execute(createTableSql)

        # 插入到sql
        cur.execute(insertSql, valuesTuple)
        # 提交commit
        conn.commit()

    # 关闭数据库连接
    conn.close()
