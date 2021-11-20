"""
Source Code: https://github.com/micropython/micropython/blob/master/ports/esp8266/modules/ntptime.py
License URL: https://github.com/micropython/micropython/blob/master/LICENSE
Fixed Version: https://qiita.com/inasawa/items/a1830266c1eceb714884
"""

try:
    import usocket as socket
except:
    import socket
try:
    import ustruct as struct
except:
    import struct

# (date(2000, 1, 1) - date(1900, 1, 1)).days * 24*60*60
NTP_DELTA = 3155673600

# The NTP host can be configured at runtime by doing: ntptime.host = 'myhost.org'
host = "pool.ntp.org"


def time():
    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1b
    addr = socket.getaddrinfo(host, 123)[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(1)
    res = s.sendto(NTP_QUERY, addr)
    msg = s.recv(48)
    s.close()
    val = struct.unpack("!I", msg[40:44])[0]
    return val - NTP_DELTA


# There's currently no timezone support in MicroPython, so
# utime.localtime() will return UTC time (as if it was .gmtime())
#
# offset: timezone offset (sec)
#         settime(9*60*60) for JST
def settime(offset=0):
    t = time() + offset
    import machine
    import utime
    tm = utime.localtime(t)
    tm = tm[0:3] + (0, ) + tm[3:6] + (0, )
    machine.RTC().datetime(tm)


def sync_jp_localtime_with_ntp():
    import utime
    from m5stack import rtc
    host = "pool.ntp.org"
    offset = 9 * 3600
    settime(offset)
    t = utime.localtime()
    rtc.setTime(t[0], t[1], t[2], t[3], t[4], t[5])
