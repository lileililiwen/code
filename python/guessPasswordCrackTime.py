import time

def estimate_crack_time(password):
    """Estimate the time required to crack a password"""
    # Define password complexity score
    score = 0
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in '!@#$%^&*()_+~`|}{[]\\:;?><,./-=' for c in password):
        score += 1
    if len(password) >= 12:
        score += 1
    # Calculate crack time
    seconds_per_guess = 0.00001  # Assume 10 microsecond per guess
    guesses_required = 10 ** (score * 2)  # Assume 100 guesses per second
    crack_time_seconds = guesses_required * seconds_per_guess
    return crack_time_seconds

# User input password
password = input("Enter a password: ")
# Estimate crack time
crack_time_seconds = estimate_crack_time(password)
# Convert to human-readable time
if crack_time_seconds < 60:
    crack_time = f"{crack_time_seconds:.2f} seconds"
elif crack_time_seconds < 3600:
    crack_time = f"{crack_time_seconds/60:.2f} minutes"
elif crack_time_seconds < 86400:
    crack_time = f"{crack_time_seconds/3600:.2f} hours"
else:
    crack_time = f"{crack_time_seconds/86400:.2f} days"
# Output result
print(f"Estimated crack time for password '{password}': {crack_time}")
#这个代码使用一个简单的密码复杂度评分系统来评估密码的强度，然后根据猜测次数和每秒猜测次数来计算密码破解所需的时间。最后，将结果转换为人类可读的时间格式并输出。
#需要注意的是，这个代码只是一个估算，实际破解时间可能会有很大的差异，具体取决于攻击者使用的破解软件、计算资源和密码的实际复杂度。





