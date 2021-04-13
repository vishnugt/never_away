import progressbar
from time import sleep
i = 0;
bar = progressbar.ProgressBar(maxval=20, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
for i in range(20):
    bar.update(i + 1)
    sleep(0.2)
bar.finish()