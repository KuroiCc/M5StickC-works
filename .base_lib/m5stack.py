from typing import Tuple
from button import Btn, BtnChild


# yapf: disable
def setScreenColor(color): ...  # noqa
def map_value(): ...  # noqa
def wait(): ...  # noqa
def wait_ms(): ...  # noqa


class _led():
    def on(self): ...  # noqa
    def off(self): ...  # noqa


class TFT():
    def __init__(self) -> None:
        self.FONT_Default = 0
        self.FONT_DefaultSmall = 0
        self.FONT_DejaVu18 = 0
        self.FONT_Ubuntu = 0
        self.FONT_Comic = 0
        self.FONT_Minya = 0
        self.FONT_Tooney = 0
        self.FONT_Small = 0
        self.FONT_7seg = 0
        self.LASTX = 0
        self.LASTY = 0
        self.CENTER = 0
        self.RIGHT = 0
        self.BOTTOM = 0

    def setRotation(self, rotation): ...  # noqa
    def clear(self, color): ...  # noqa
    def text(self, x, y, text, color): ...  # noqa
    def setColor(self, color, bcolor): ...  # noqa
    def print(self, text, x, y, color, rotate, transparent, fixedwidth, wrap): ...  # noqa
    def println(self, text, x, y, color): ...  # noqa
    def qrcode(self, text, x, y, width, version): ...  # noqa
    def winsize(self) -> Tuple[int, int]: ...  # noqa
    def fontSize(self) -> Tuple[int, int]: ...  # noqa
    def textWidth(text): ...  # noqa
    def font(font): ...  # noqa


class Power():
    def getBatVoltage(self): ...  # noqa
    def getChargeState(self): ...  # noqa
    def setLcdBrightness(brightness): ...  # noqa


class M5Title():
    def __init__(self, title, x, fgcolor, bgcolor) -> None: ...  # noqa
    def setTitle(self, text): ...  # noqa
    def show(self): ...  # noqa
    def hide(self): ...  # noqa
    def setFgColor(self, color): ...  # noqa
    def setBgColor(self, color): ...  # noqa


class Time():
    def now(self): ...  # noqa
    def setTime(self, year, month, date, hour, minute, second): ...  # noqa


class M5TextBox():
    def __init__(self, x, y, text, font, color, rotate=0) -> None: ...  # noqa
    def setColor(self, color): ...  # noqa
    def setPosition(self, x=10, y=10): ...  # noqa
    def setPosition(self, x=10): ...  # noqa
    def setPosition(self, y=10): ...  # noqa
    def setFont(self, font): ...  # noqa
    def setRotate(self, rotate): ...  # noqa
    def setText(self, text): ...  # noqa
    def hide(self, ): ...  # noqa
    def show(self, ): ...  # noqa
    # yapf: enable


M5Led = _led(1, 2)
lcd = TFT()

btn = Btn()
btnA = BtnChild(1)
btnB = BtnChild(1)
axp = Power()
rtc = Time()
