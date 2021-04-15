'''
Install the dependencies using
	pip install -r requirements.txt

or install it manually
	pip install idle-time
	pip install pyautogui
	pip install progressbar
'''

from idle_time import IdleMonitor
from datetime import datetime
import time
import pyautogui
import progressbar

ALLOWED_IDLE_TIME = 180 #In seconds

counter = 1
startTime = datetime.now().timestamp()

def main():
	print(f"Starting with idle time out as {ALLOWED_IDLE_TIME} seconds")
	while True:
		forever()

def forever():
	monitor = IdleMonitor.get_monitor()
	prevTime = monitor.get_idle_time();
	bar = progressbar.ProgressBar(maxval=ALLOWED_IDLE_TIME, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
	bar.start()
	while True:
		time.sleep(1)
		idleTime = monitor.get_idle_time()
		if prevTime > idleTime:
			bar.start()
		prevTime = idleTime
		bar.update(min(idleTime + 1, ALLOWED_IDLE_TIME))
		if(idleTime > ALLOWED_IDLE_TIME):
			pyautogui.press('win')
			time.sleep(0.15) #necessary else two keypresses sometimes getting registered as one
			pyautogui.press('win')
			bar.finish()
			global counter
			timeWorked = (datetime.now().timestamp() - startTime - (counter * ALLOWED_IDLE_TIME))/60
			afkTime = counter * ALLOWED_IDLE_TIME / 60

			print(f"You were afk for {format(afkTime, '.3f')} minutes, and you have worked for {format(timeWorked, '.3f')} minutes or {format(timeWorked/60, '.3f')} hours")
			counter += 1
			return

if __name__ == "__main__":
	main()
