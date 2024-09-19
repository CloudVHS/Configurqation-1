# Задача 1
Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd (вам понадобится grep).
# Код
grep '.*' /etc/passwd | cut -d: -f1 | sort
# Результат
xartd0@xartd0-Strix-GL504GW-GL504GW:~$ grep '.*' /etc/passwd | cut -d: -f1 | sort
_apt
avahi
backup
bin
colord
cups-browsed
cups-pk-helper
daemon
dhcpcd
dnsmasq
ftp
fwupd-refresh
games
gdm
geoclue
gnome-initial-setup
gnome-remote-desktop
hplip
irc
kernoops
list
lp
mail
man
messagebus
news
nm-openvpn
nobody
polkitd
proxy
root
rtkit
saned
speech-dispatcher
sshd
sssd
sync
sys
syslog
systemd-network
systemd-oom
systemd-resolve
systemd-timesync
tcpdump
tss
usbmux
uucp
uuidd
whoopsie
www-data
xartd0
