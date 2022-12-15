import datetime as dt
import time

now1 = dt.datetime.now()
time.sleep(3)
now2 = dt.datetime.now()
dd = now2 - now1
print(dd)