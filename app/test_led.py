from m5stack import *
from m5ui import *
from uiflow import *
from my_utils import Log, my_init

my_init(0, lcd.FONT_DefaultSmall, 0, 0)

led_status = False

log = Log()


def A_press():
    global led_status
    if led_status:
        M5Led.off()
        led_status = False
    else:
        M5Led.on()
        led_status = True

    log.log(str(led_status))


btnA.wasPressed(A_press)


def b_2press():
    log.clear()


btnB.wasDoublePress(b_2press)
