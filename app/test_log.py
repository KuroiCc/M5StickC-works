from m5stack import *
from m5ui import *
from uiflow import *
from my_utils import Log, my_init
from random import randint

my_init(3, lcd.FONT_DefaultSmall, 0, 0)

log = Log()

lcd.println(log.max_len_per_line)
lcd.println(log.max_line)


def btn_a_press():
    t = ""
    for i in range(randint(1, 20)):
        t += str(randint(1, 10))
    log.log(t)


btnA.wasPressed(btn_a_press)


def btn_b_press():
    lcd.clear()


btnB.wasPressed(btn_b_press)
