#生成二维码，参考http://tools.jb51.net/transcoding/jb51qrcode
import qrcode
from PIL import Image

def generate_qrcode(content_type, content, bg_color, img_color, outer_frame_color, inner_frame_color):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    if content_type == 'text':
        qr.add_data(content)
    elif content_type == 'tel':
        qr.add_data('tel:' + content)
    elif content_type == 'sms':
        tel, message = content.split(',')
        qr.add_data('smsto:' + tel + ':' + message)
    elif content_type == 'vcard':
        name, tel, company, url, job_title, email, address = content.split(',')
        vcard = f'BEGIN:VCARD\nVERSION:3.0\nN:{name};;;\nFN:{name}\nORG:{company}\nURL:{url}\nTITLE:{job_title}\nTEL;TYPE=WORK,VOICE:{tel}\nEMAIL:{email}\nADR;TYPE=WORK:;;{address};;;;\nEND:VCARD'
        qr.add_data(vcard)
    elif content_type == 'url':
        qr.add_data(content)
    elif content_type == 'wifi':
        ssid, password, encryption = content.split(',')
        wifi = f'WIFI:S:{ssid};T:{encryption};P:{password};;'
        qr.add_data(wifi)
    else:
        raise ValueError('Unsupported content type')
    qr.make(fit=True)
    img = qr.make_image(fill_color=img_color, back_color=bg_color).convert('RGBA')
    outer_frame = Image.new('RGBA', (img.size[0] + 20, img.size[1] + 20), outer_frame_color)
    inner_frame = Image.new('RGBA', (img.size[0] + 16, img.size[1] + 16), inner_frame_color)
    outer_frame.paste(inner_frame, (2, 2))
    outer_frame.paste(img, (10, 10), img)
    return outer_frame


bg_color = '#FFFFFF'
img_color = '#000000'
outer_frame_color = '#000000'
inner_frame_color = '#FFFFFF'

# 生成文本内容的二维码
content_type = 'text'
content = 'Hello, world!'
img = generate_qrcode(content_type, content, bg_color, img_color, outer_frame_color, inner_frame_color)
img.show()

# 生成电话号码的二维码
content_type = 'tel'
content = '1234567890'
img = generate_qrcode(content_type, content, bg_color, img_color, outer_frame_color, inner_frame_color)
img.show()

# 生成短信的二维码
content_type = 'sms'
content = '1234567890,Hello world!'
img = generate_qrcode(content_type, content, bg_color, img_color, outer_frame_color, inner_frame_color)
img.show()

#生成电子名片的二维码
content_type = 'vcard'
content = 'John Doe,1234567890,Acme Inc.,https://www.acme.com,Software Engineer,john.doe@acme.com,123 Main St Anytown USA'
img = generate_qrcode(content_type, content, bg_color, img_color, outer_frame_color, inner_frame_color)
img.show()

#生成网址的二维码
content_type = 'url'
content = 'https://www.example.com'
img = generate_qrcode(content_type, content, bg_color, img_color, outer_frame_color, inner_frame_color)
img.show()

#生成wifi网络的二维码
content_type = 'wifi'
content = 'MyNetwork,MyPassword,WPA'
img = generate_qrcode(content_type, content, bg_color, img_color, outer_frame_color, inner_frame_color)
img.show()