from m5stack import *
from m5ui import *
from uiflow import *
from my_utils import my_init

my_init(3, lcd.FONT_DefaultSmall, 0, 0)

time = rtc.now()
date_label = M5TextBox(
    38, 20, "%04d-%02d-%02d" % (time[0], time[1], time[2]), lcd.FONT_Default
)
time_label = M5TextBox(
    36, 40, "%02d:%02d:%02d" % (time[3], time[4], time[5]), lcd.FONT_DejaVu18
)

while True:
    wait_ms(10)
    time = rtc.now()
    date_label.setText("%04d-%02d-%02d" % (time[0], time[1], time[2]))
    time_label.setText("%02d:%02d:%02d" % (time[3], time[4], time[5]))
