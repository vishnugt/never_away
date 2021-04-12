'''
pip install idle-time
pip install pyautogui
'''

from idle_time import IdleMonitor
import time
import pyautogui


#In seconds
INTERVAL_TO_CHECK = 20
ALLOWED_IDLE_TIME = 180


def main():
	monitor = IdleMonitor.get_monitor()

	while True:
		time.sleep(INTERVAL_TO_CHECK)
		idleTime = monitor.get_idle_time()
		print(idleTime)
		if(idleTime > ALLOWED_IDLE_TIME):
			pyautogui.press('win')
			pyautogui.press('win')
			print(f"You were afk for {idleTime} seconds, but no worries")


if __name__ == "__main__":
	main()
