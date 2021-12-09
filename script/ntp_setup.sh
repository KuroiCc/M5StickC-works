sudo echo "[Time]
NTP=ntp.jst.mfeed.ad.jp ntp.nict.jp
FallbackNTP=time.google.com
#FallbackNTP=0.debian.pool.ntp.org 1.debian.pool.ntp.org 2.debian.pool.ntp.org 3.debian.pool.ntp.org
#RootDistanceMaxSec=5
#PollIntervalMinSec=32
#PollIntervalMaxSec=2048" > /etc/systemd/timesyncd.conf

timedatectl set-ntp true
systemctl daemon-reload
systemctl restart systemd-timesyncd.service

apt update
apt full-upgrade -y
apt autoremove -y
apt clean
reboot