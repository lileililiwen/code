# 导入所需模块
import imaplib
import email

# 邮件服务器地址和端口
imap_server = "imap.gmail.com"
imap_port = 993

# 邮件账户信息
email_address = "your_email@example.com"
email_password = "your_email_password"

# 连接到IMAP服务器
with imaplib.IMAP4_SSL(imap_server, imap_port) as mail:
    # 登录邮箱账户
    mail.login(email_address, email_password)

    # 选择收件箱
    mail.select("inbox")

    # 搜索收件箱中所有邮件
    _, search_data = mail.search(None, "ALL")

    # 遍历搜索结果
    for num in search_data[0].split():
        _, data = mail.fetch(num, "(RFC822)")

        # 解析邮件内容
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)

        # 获取发件人、主题和时间
        sender = email_message["From"]
        subject = email_message["Subject"]
        time = email_message["Date"]

        # 打印邮件信息
        print("From: ", sender)
        print("Subject: ", subject)
        print("Time: ", time)

        # 获取邮件正文内容
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                print(part.get_payload(decode=True).decode("utf-8"))
            elif part.get_content_type() == "text/html":
                print(part.get_payload(decode=True).decode("utf-8"))
                 # 如果是附件类型
            elif part.get_content_disposition() == "attachment":
                # 获取附件文件名
                filename = part.get_filename()
                # 如果存在文件名
                if filename:
                    # 创建文件夹，如果不存在
                    if not os.path.isdir("attachments"):
                        os.mkdir("attachments")

                    # 拼接附件完整路径
                    filepath = os.path.join("attachments", filename)

                    # 下载附件文件
                    with open(filepath, "wb") as f:
                        f.write(part.get_payload(decode=True))
                        print(f"Downloaded attachment: {filename}")

# 导入所需模块
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.header import Header
from email.utils import formataddr
import os

# 发件人邮箱地址
sender_email = "your_email@example.com"

# 发件人邮箱密码，如果启用了两步验证，请使用授权码
sender_password = "your_email_password"

# 收件人邮箱地址
recipient_email = "recipient_email@example.com"

# 构建邮件内容
msg = MIMEMultipart()

# 添加文本内容
text = "Hello, this is a test email."
text_mime = MIMEText(text, "plain", "utf-8")
msg.attach(text_mime)

# 添加图片内容
image_file_path = "path/to/image.jpg"
if os.path.exists(image_file_path):
    with open(image_file_path, "rb") as f:
        image = MIMEImage(f.read())
        image.add_header('Content-ID', '<image1>')
        msg.attach(image)

# 添加附件内容
file_path = "path/to/file.pdf"
if os.path.exists(file_path):
    with open(file_path, "rb") as f:
        file = MIMEApplication(f.read())
        file.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_path))
        msg.attach(file)

# 设置邮件标题、发件人和收件人
msg["Subject"] = Header("Test Email", "utf-8")
msg["From"] = formataddr(("Sender Name", sender_email))
msg["To"] = recipient_email

# 连接SMTP服务器，发送邮件
smtp_server = "smtp.gmail.com"
smtp_port = 587
with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()
    smtp.login(sender_email, sender_password)
    smtp.sendmail(sender_email, recipient_email, msg.as_string())                