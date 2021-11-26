from m5stack import *
from m5ui import *
from uiflow import *
from my_utils import Logger, my_init
from random import randint

my_init(rotation=1)

log = Logger(ezdata_token="3lpzokiWbY4LzE61mraLIF5fsMV5Ja4m")


def btn_a_press():
    num = randint(1, 30)
    t = str(num + len(str(num))) + chr(randint(65, 90)) * num
    log.log(t)


btnA.wasPressed(btn_a_press)


def btn_b_press():
    log.clear()


btnB.wasPressed(btn_b_press)
