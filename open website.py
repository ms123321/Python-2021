import os
import time
from time import sleep


os.system("start \"\" https://boards.4chan.org/pol/thread/356952592")
time.sleep(10)
os.system("taskkill /im chrome.exe /f")
os.system("powershell.exe -command Stop-Process -Name 'chrome'")


