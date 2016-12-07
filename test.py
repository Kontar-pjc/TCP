import time
import ctypes
import threading


def lock_mouse():
    """lock the mouse"""
    try:
        start_time = time.time()
        end_time = int(start_time) + 10
        while time.time() < end_time:
            ctypes.windll.user32.SetCursorPos(0, 0)
            time.sleep(0.03)
    except Exception as e:
        print e
        return False
    finally:
        return True

if __name__ == '__main__':
    lock_mouse_thread = threading.Thread(target=lock_mouse(), args=())
