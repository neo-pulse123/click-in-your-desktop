import time
import pyautogui

def get_mouse_position():
    """
    获取鼠标当前位置的坐标
    """
    print("===== 微信坐标获取工具 =====")
    print("此工具将帮助你获取微信界面上各个元素的坐标")
    print("\n使用说明：")
    print("1. 运行本程序")
    print("2. 将鼠标移动到微信界面上的目标位置（如搜索框、好友列表等）")
    print("3. 程序将每2秒自动显示当前鼠标坐标")
    print("4. 按下 Ctrl+C 停止程序")
    print("\n开始获取坐标...")
    
    try:
        while True:
            # 获取当前鼠标坐标
            x, y = pyautogui.position()
            
            # 清除当前行并打印新坐标
            print(f"\r当前坐标：x={x:4d}, y={y:4d} | 按 Ctrl+C 停止", end="", flush=True)
            
            # 等待2秒
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\n\n程序已停止，感谢使用！")

if __name__ == "__main__":
    get_mouse_position()