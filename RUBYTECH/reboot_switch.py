import telnetlib
import time




ip = '192.168.1.16'

with telnetlib.Telnet(ip) as t:
    t.read_until(b'Login', timeout=3)
    t.write(b'admin\n')
    t.read_until(b'Password', timeout=3)
    t.write(b'admin\n')
    t.read_until(b'#', timeout=3)
    t.write(b'reboot\n')
    time.sleep(5)
    t.close()
