import random
import string
import hashlib
import bcrypt
import secrets
from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from passlib.hash import pbkdf2_sha256

### 生成密码 ###

# 生成随机密码
def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    return password

# 示例
password = generate_password()
print(f"生成的随机密码为：{password}")


### 哈希密码 ###

# MD5
def hash_md5(password):
    password_hash = hashlib.md5(password.encode()).hexdigest()
    return password_hash

# SHA-1
def hash_sha1(password):
    password_hash = hashlib.sha1(password.encode()).hexdigest()
    return password_hash

# SHA-256
def hash_sha256(password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    return password_hash

# SHA-512
def hash_sha512(password):
    password_hash = hashlib.sha512(password.encode()).hexdigest()
    return password_hash

# Bcrypt
def hash_bcrypt(password):
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return password_hash.decode()

# PBKDF2-SHA256
def hash_pbkdf2_sha256(password):
    password_hash = pbkdf2_sha256.hash(password)
    return password_hash

# 验证密码
def verify_password(stored_password, provided_password):
    if stored_password.startswith("$2b$"):
        return bcrypt.checkpw(provided_password.encode(), stored_password.encode())
    else:
        return pbkdf2_sha256.verify(provided_password, stored_password)

# 示例
password = "password123"
hashed_password = hash_bcrypt(password)
print(f"哈希后的密码为：{hashed_password}")
print(f"验证密码：{verify_password(hashed_password, password)}")


### 对称加密 ###

# 生成加密密钥
def generate_symmetric_key():
    key = Fernet.generate_key()
    return key

# 加密
def encrypt(plaintext, key):
    cipher_suite = Fernet(key)
    ciphertext = cipher_suite.encrypt(plaintext.encode())
    return ciphertext

# 解密
def decrypt(ciphertext, key):
    cipher_suite = Fernet(key)
    plaintext = cipher_suite.decrypt(ciphertext).decode()
    return plaintext

# 示例
key = generate_symmetric_key()
plaintext = "Hello, world!"
ciphertext = encrypt(plaintext, key)
decrypted_plaintext = decrypt(ciphertext, key)
print(f"加密后的文本为：{ciphertext}")
print(f"解密后的文本为：{decrypted_plaintext}")

# AES 对称加解密示例代码
def encrypt_aes(plaintext, key):
    cipher = AES.new(key, AES.MODE_CTR)
    nonce = cipher.nonce
    ciphertext = cipher.encrypt(plaintext)
    return nonce + ciphertext


def decrypt_aes(ciphertext, key):
    nonce = ciphertext[:16]
    ciphertext = ciphertext[16:]
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext


### 非对称加密 ###

import base64
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes



# RSA 公钥加密示例代码
def encrypt_rsa(plaintext, public_key):
    recipient_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    ciphertext = cipher_rsa.encrypt(plaintext)
    return ciphertext


# RSA 私钥解密示例代码
def decrypt_rsa(ciphertext, private_key):
    private_key = RSA.import_key(private_key)
    cipher_rsa = PKCS1_OAEP.new(private_key)
    plaintext = cipher_rsa.decrypt(ciphertext)
    return plaintext


# 生成 RSA 密钥对示例代码
def generate_rsa_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key


# Base64 编解码示例代码
def base64_encode(data):
    return base64.b64encode(data).decode('utf-8')


def base64_decode(data):
    return base64.b64decode(data.encode('utf-8'))


if __name__ == '__main__':
    # AES 加解密示例
    key = get_random_bytes(16)
    plaintext = b"Hello, world!"
    ciphertext = encrypt_aes(plaintext, key)
    decrypted_plaintext = decrypt_aes(ciphertext, key)
    assert plaintext == decrypted_plaintext

    # RSA 加解密示例
    private_key, public_key = generate_rsa_key_pair()
    plaintext = b"Hello, RSA!"
    ciphertext = encrypt_rsa(plaintext, public_key)
    decrypted_plaintext = decrypt_rsa(ciphertext, private_key)
    assert plaintext == decrypted_plaintext

    # Base64 编解码示例
    data = b"Hello, Base64!"
    encoded_data = base64_encode(data)
    decoded_data = base64_decode(encoded_data)
    assert data == decoded_data
