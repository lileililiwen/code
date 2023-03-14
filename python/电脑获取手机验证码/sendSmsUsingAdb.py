import subprocess

def send_sms(phone_number, message, sim_id=0):
    command = "adb shell pm grant your.package.name android.permission.SEND_SMS"
    result = subprocess.run(command, shell=True, capture_output=True)
    if result.returncode != 0:
        print("Failed to grant permission: {}".format(result.stderr.decode().strip()))
    else:
        print("Permission granted successfully.")

    # 通过 adb shell am start 命令发送短信。其中，-a android.intent.action.SENDTO 参数指定要发送短信的操作，-d sms:{phone_number} 参数指定要发送短信的手机号码，--es sms_body '{message}' 参数指定要发送的短信内容，--ez exit_on_sent true 参数指定发送完短信后退出发送界面。
    # 在 adb shell am start 命令中，可以添加 -e simId 参数来指定要使用的 SIM 卡 ID，例如 -e simId 0 表示使用 SIM 卡 1 发送短信，-e simId 1 表示使用 SIM 卡 2 发送短信。
    # dat 参数用于指定要启动的 Activity 对应的 URI，
    command = "adb shell am start -a android.intent.action.SENDTO -d sms:{}  --es sms_body '{}' --ez exit_on_sent true -e simId {}".format(phone_number, message, sim_id)
    print(command)
    result = subprocess.run(command, shell=True, capture_output=True)
    if result.returncode != 0:
        print("Failed to send SMS: {}".format(result.stderr.decode().strip()))
    else:
        print("SMS sent successfully.")

# 使用 SIM 卡 1 发送短信
# send_sms("1234567890", "Hello, World!", sim_id=0)

#db shell am force-stop <package_name> 强制关闭一个应用
# 使用 SIM 卡 2 发送短信
send_sms("18607192405", "测试，这是一个测试,hello python!", sim_id=1)