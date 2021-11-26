from m5stack import lcd, rtc
from flow import ezdata
import wifiCfg


def date_format(date):
    return "%04d-%02d-%02d %02d:%02d:%02d" % date


class Logger():
    def __init__(
        self,
        ezdata_token: str = "",
        up_to_ezdata: bool = True,
        print_to_screen: bool = True,
        log_name: str = "log_" + date_format(rtc.now())
    ) -> None:
        self.loglist: List[str] = []
        self.logtime: List[list] = []

        self.up_to_ezdata = up_to_ezdata
        self.__ezdata_token = ezdata_token
        self.log_name = log_name

        self.print_to_screen = print_to_screen
        self.win_width, self.win_height = lcd.winsize()
        self.font_width, self.font_height = lcd.fontSize()
        self.print_loglist: List[str] = []

        self.log("start log.....")

    def log(self, text: str) -> None:
        self.loglist.append(text)
        self.logtime.append(rtc.now())

        if self.up_to_ezdata and self.__ezdata_token:
            self.__upload(-1)

        if self.print_to_screen:
            self.print_loglist.append(text)
            self.__print_log()

    def __upload(self, index):
        text = date_format(self.logtime[index]) + " " + self.loglist[index]
        ezdata.addToList(self.__ezdata_token, self.log_name, text)

    def clear(self) -> None:
        self.print_loglist = []
        if self.print_to_screen:
            lcd.clear()
            lcd.print("", 0, 0)

    def __print_log(self):

        lcd.clear()
        y = self.win_height - 1
        for text in self.print_loglist[::-1]:
            line_offset = lcd.textWidth(text) // self.win_width + 1
            y = y - self.font_height * line_offset

            if y <= 0:
                return

            lcd.print(text, 0, y)


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
    """
    rotation：画面の向き(0,1,2,3)、
    print_pox：printの最初の座標
    print_poy：printの最初の座標
    wifilcdShow：wifi接続画面を表示するかどうか
    """
    wifiCfg.autoConnect(lcdShow=wifilcdShow)
    sync_jp_localtime_with_ntp()

    lcd.clear()
    lcd.setRotation(rotation)
    lcd.font(font)
    lcd.print("", print_pox, print_poy)
