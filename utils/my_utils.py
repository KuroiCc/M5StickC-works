from typing import List
from m5stack import lcd, rtc
import wifiCfg


class Log():
    def __init__(self) -> None:
        winsize = lcd.winsize()
        self.win_width = winsize[0]
        self.win_height = winsize[1]

        fontsize = lcd.fontSize()
        self.font_width = fontsize[0]
        self.font_height = fontsize[1]

        self.max_len_per_line = self.win_width // int(self.font_width * 0.8)
        self.max_line = self.win_height // self.font_height - 1

        self.loglist: List[str] = []
        self.print_loglist: List[str] = []
        lcd.clear()

    def log(self, text: str) -> None:
        self.loglist.append(text)
        self.print_loglist.append(text)
        self.__print_log()

    def clear(self) -> None:
        lcd.clear()
        self.print_loglist = []
        lcd.print("", 0, 0)

    def __print_log(self):
        print_list = self.print_loglist[-self.max_line:]

        lcd.clear()
        lcd.print("", 0, 0)
        for text in print_list:
            if len(text) <= self.max_len_per_line:
                lcd.println(text)
            else:
                a = text[:self.max_len_per_line]
                lcd.println(a)


def sync_jp_localtime_with_ntp():
    """
    https://qiita.com/nagase/items/96e87b3c91a0c820e002
    """
    import ntp
    import utime

    offset = 9 * 3600
    ntp.host = "pool.ntp.org"
    ntp.settime(offset)
    t = utime.localtime()
    rtc.setTime(t[0], t[1], t[2], t[3], t[4], t[5])


def my_init(
    rotation=0, font=lcd.FONT_DefaultSmall, print_pox=0, print_poy=0, wifilcdShow=True
):
    wifiCfg.autoConnect(lcdShow=wifilcdShow)
    sync_jp_localtime_with_ntp()

    lcd.clear()
    lcd.setRotation(rotation)
    lcd.font(font)
    lcd.print("", print_pox, print_poy)
