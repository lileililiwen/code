
#json代码在线格式化/美化/压缩/编辑/转换工具
# http://tools.jb51.net/code/jsoncodeformat
import json

# 定义一个JSON字符串
json_str = '{"name":"John", "age":30, "city":"New York"}'

# 格式化JSON字符串
json_obj = json.loads(json_str)
json_formatted = json.dumps(json_obj, indent=4, sort_keys=True)
print(json_formatted)

# 压缩JSON字符串
json_compact = json.dumps(json_obj, separators=(',', ':'))
print(json_compact)