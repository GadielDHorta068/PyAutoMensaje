import pyautogui
import time


def send_messages(file_path, delay=1):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        pyautogui.typewrite(line.strip())
        pyautogui.press('enter')
        time.sleep(delay)


if __name__ == "__main__":
    file_path = 'mensaje.txt'
    delay = 0.1  # retraso entre los mensajes
    time.sleep(5)
    send_messages(file_path, delay)
