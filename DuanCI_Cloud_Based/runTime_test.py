import threading
import time

def A():
    time.sleep(1)  # 模擬程序A執行時間
    return "程序A的回覆"

def B(result):
    print(f"程序B執行，接收到程序A的結果：{result}")
    # 這裡放置程序B的程式碼

def C():
    print("程序C執行，程序A超時")
    # 這裡放置程序C的程式碼

def run_with_timeout(func, timeout):
    result = None
    event = threading.Event()

    def target():
        nonlocal result
        result = func()
        event.set()

    thread = threading.Thread(target=target)
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        return None  # 超時
    else:
        return result  # 正常回覆

result = run_with_timeout(A, 1)

if result:
    B(result)  # 程序A正常回覆，執行程序B
else:
    C()  # 程序A超時，執行程序C