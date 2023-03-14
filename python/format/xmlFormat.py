#http://tools.jb51.net/code/xml_format_compress
#这是一款针对XML代码进行压缩与格式化的工具，可实现XML代码的在线压缩与格式化功能，一键格式化与压缩XML代码
import xml.dom.minidom

# 格式化XML
def format_xml(xml_str):
    try:
        # 解析xml
        dom = xml.dom.minidom.parseString(xml_str)
        # 格式化xml
        format_xml_str = dom.toprettyxml()
        return format_xml_str
    except Exception as e:
        print(f"Error: {e}")

# 压缩XML
def compress_xml(xml_str):
    try:
        # 解析xml
        dom = xml.dom.minidom.parseString(xml_str)
        # 压缩xml
        compress_xml_str = dom.toxml()
        return compress_xml_str
    except Exception as e:
        print(f"Error: {e}")