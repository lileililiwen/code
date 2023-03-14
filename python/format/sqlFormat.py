#http://tools.jb51.net/code/sql_format_compress
# SQL在线压缩/格式化工具说明
# 1. 该工具提供了SQL格式化、压缩以及处理结果的复制、保存为sql文本、清除处理结果等功能。一键操作、简便易用。
# 2. 用户可输入如下代码进行简单测试：
# select * from `jb51_db` where `id` = '2'
# 格式化后的代码效果如下：
# SELECT *
# FROM `jb51_db`
# WHERE `id` = '2'

import sqlparse

def format_sql(sql):
    # 使用sqlparse格式化SQL
    formatted_sql = sqlparse.format(sql, reindent=True, keyword_case='upper')
    return formatted_sql

def minify_sql(sql):
    # 使用sqlparse压缩SQL
    minified_sql = sqlparse.format(sql, strip_comments=True, compress=True)
    return minified_sql

# 测试
sql = "SELECT * FROM mytable WHERE id=1;"
formatted_sql = format_sql(sql)
minified_sql = minify_sql(sql)
print(formatted_sql)
print(minified_sql)