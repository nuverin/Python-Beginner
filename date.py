#Time tutorial

from datetime import date, datetime, timedelta
from time import time
import unittest
#Sebuah waktu akan dimanupilasi with time delta
#ini hari apa?

def tanggal_now():
       time_now = datetime.now()
   
       new_time= time_now + timedelta(weeks=1)
       print("TIME " , str(new_time))

def mengubah():
       #use datetime
       time_now = timedelta(seconds=4, weeks= 1)
       print(time_now)
       times = datetime(2024, 1, 9, 9, 1 , 2) + \
          time_now
       print(times)
if __name__ == '__main__':
    mengubah()
