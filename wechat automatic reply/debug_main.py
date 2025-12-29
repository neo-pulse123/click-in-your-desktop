import time
import schedule
import pyautogui
import subprocess

# 配置参数
target_name = "dsj"  # 好友昵称
message = "jinwanwodaichapai"  # 要发送的消息
wechat_path = "D:\\weixin\\Weixin.exe"  # 微信安装路径


# 打开微信
def open_wechat():
    print("正在打开微信...")
    try:
        subprocess.Popen(wechat_path)
        time.sleep(3)  # 等待微信打开
        print("微信已打开")
    except Exception as e:
        print(f"打开微信失败：{e}")


# 发送消息
def send_message():
    print("准备发送消息...")

    try:
        # 1. 打开微信
        open_wechat()
        time.sleep(2)

        # 2. 点击搜索框
        # 搜索框位置可能需要根据你的屏幕调整
        pyautogui.click(x=2061, y=75)  # 默认位置，可能需要调整
        time.sleep(1)

        # 3. 输入好友昵称
        pyautogui.write(target_name)
        pyautogui.press("enter")
        time.sleep(2)

        # 4. 点击好友
        pyautogui.click(x=2080, y=187)  # 默认位置，可能需要调整
        time.sleep(1)

        pyautogui.click(x=2378, y=775)  # 默认位置，可能需要调整
        time.sleep(1)

        # 5. 输入消息
        pyautogui.write(message)
        pyautogui.press("space")
        time.sleep(1)

        # 6. 发送消息
        pyautogui.press("enter")
        print(f"消息已发送：{message}")

    except Exception as e:
        print(f"发送失败：{e}")


# 主函数
def main():
    print("微信自动发送消息程序启动")
    print(f"配置：")
    print(f"- 好友昵称：{target_name}")
    print(f"- 发送消息：{message}")
    print(f"- 微信路径：{wechat_path}")

    # 设置每天18:00执行任务
    schedule.every().day.at("16:53").do(send_message)
    print("定时任务已设置，每天18:00发送消息")

    # 保持程序运行
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()