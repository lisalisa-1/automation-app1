import subprocess
import time
import threading

# 启动Appium Server并记录日志
def start_appium_server():
    print("启动Appium Server...")
    process = subprocess.Popen(
        ['appium', '--log-level', 'debug'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    
    # 读取并显示日志
    try:
        while True:
            line = process.stdout.readline()
            if not line:
                break
            print(line.strip())
    except KeyboardInterrupt:
        print("停止Appium Server...")
        process.terminate()
    finally:
        process.wait()

# 运行微信启动脚本
def run_wechat_script():
    print("等待5秒后运行微信启动脚本...")
    time.sleep(5)
    
    print("运行微信启动脚本...")
    import subprocess
    result = subprocess.run(
        ['python', 'minimal_test.py'],
        capture_output=True,
        text=True
    )
    
    print("\n微信脚本输出:")
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)

# 启动两个线程
server_thread = threading.Thread(target=start_appium_server)
script_thread = threading.Thread(target=run_wechat_script)

server_thread.start()
script_thread.start()

# 等待脚本线程完成
script_thread.join()

print("\n按Enter键停止Appium Server...")
input()