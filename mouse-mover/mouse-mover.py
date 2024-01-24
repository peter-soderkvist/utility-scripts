#!python3
import pyautogui, time, random, sys


if __name__ == '__main__':
    screen_width, screen_height = pyautogui.size()
    while True:
        try:
            x = random.randint(0, screen_width)
            y = random.randint(0, screen_height)
            move_duration = random.randint(1, 3)
            sleep_duration = random.randint(0, 5)
            pyautogui.moveTo(x, y, move_duration)
            time.sleep(sleep_duration)
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)
