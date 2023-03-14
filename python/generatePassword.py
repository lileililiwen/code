import string
import random

def generate_password(length, include_symbols=False):
    """Generate a strong password of given length"""
    # Define character set
    if include_symbols:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits
    # Generate password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Generate a 12-character password without symbols
password1 = generate_password(12)
print(password1)

# Generate a 16-character password with symbols
password2 = generate_password(16, include_symbols=True)
print(password2)    