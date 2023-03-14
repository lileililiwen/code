from reportlab.pdfgen import canvas
import PyPDF2

# 创建一个PDF文件
c = canvas.Canvas('example.pdf')
c.drawString(100, 750, "Welcome to Python PDF Tutorial")
c.save()

# 读取PDF文件
pdf_file = open('example.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
num_pages = pdf_reader.numPages
page1 = pdf_reader.getPage(0)
page1_text = page1.extractText()
pdf_file.close()

# 合并两个PDF文件
pdf1_file = open('example1.pdf', 'rb')
pdf2_file = open('example2.pdf', 'rb')
pdf1_reader = PyPDF2.PdfFileReader(pdf1_file)
pdf2_reader = PyPDF2.PdfFileReader(pdf2_file)
pdf_writer = PyPDF2.PdfFileWriter()
for pageNum in range(pdf1_reader.numPages):
    page = pdf1_reader.getPage(pageNum)
    pdf_writer.addPage(page)
for pageNum in range(pdf2_reader.numPages):
    page = pdf2_reader.getPage(pageNum)
    pdf_writer.addPage(page)
pdf_output_file = open('merged_example.pdf', 'wb')
pdf_writer.write(pdf_output_file)
pdf_output_file.close()
pdf1_file.close()
pdf2_file.close()

# 拆分PDF文件
pdf_file = open('example.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
for pageNum in range(pdf_reader.numPages):
    pdf_writer = PyPDF2.PdfFileWriter()
    page = pdf_reader.getPage(pageNum)
    pdf_writer.addPage(page)
    output_filename = 'page_{}.pdf'.format(pageNum+1)
    output_file = open(output_filename, 'wb')
    pdf_writer.write(output_file)
    output_file.close()
pdf_file.close()

# 将PDF文件转换为文本
pdf_file = open('example.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
text = ''
for pageNum in range(pdf_reader.numPages):
    page = pdf_reader.getPage(pageNum)
    page_text = page.extractText()
    text += page_text
pdf_file.close()
print(text)