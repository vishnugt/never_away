'''
Install the dependencies using
	pip install -r requirements.txt

or install it manuall
	pip install idle-time
	pip install pyautogui
	pip install progressbar
'''

from idle_time import IdleMonitor
import time
import pyautogui
import progressbar

ALLOWED_IDLE_TIME = 180 #In seconds

def main():
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
		bar.update(min(idleTime + 1, ALLOWED_IDLE_TIME))
		if(idleTime > ALLOWED_IDLE_TIME):
			pyautogui.press('win')
			time.sleep(0.15) #necessary else two keypresses sometimes getting registered as one
			pyautogui.press('win')
			bar.finish()
			print("You were afk for {} seconds, sending some keystrokes".format(idleTime))
			return

if __name__ == "__main__":
	main()