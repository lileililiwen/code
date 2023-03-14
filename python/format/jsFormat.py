#http://tools.jb51.net/code/jscompress
# JavaScript代码工具为大家提供针对JavaScript代码的压缩、格式化、eval加密/解密以及针对处理结果的复制与清空功能。此外，针对JavaScript格式化代码功能，还提供了格式化代码结果的缩进方式、大小等选项，供用户选择使用。提供给需要的朋友使用
import jsbeautifier

# 格式化代码
formatted_code = jsbeautifier.beautify("var x=1;var y=2;")

# 压缩代码
compressed_code = jsbeautifier.beautify("var x = 1; var y = 2;", opts={"indent_size": 0, "space_in_empty_paren": True})

print(formatted_code)
print(compressed_code)



import javascript_obfuscator

# 加载JavaScript代码
with open('test.js', 'r') as f:
    code = f.read()

# 混淆代码
obfuscated_code = javascript_obfuscator.obfuscate(code)

print(obfuscated_code)