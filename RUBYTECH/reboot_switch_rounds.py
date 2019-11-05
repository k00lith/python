import telnetlib
import time




dev_ip = ['10.0.0.1']
#dev_ip = ['10.0.0.1', '10.0.0.2', '10.0.0.3']

for ip in dev_ip:
    with telnetlib.Telnet(ip) as t:
        t.read_until(b'Login', timeout=3)
        t.write(b'admin\n')
        t.read_until(b'Password', timeout=3)
        t.write(b'admin\n')
        t.read_until(b'#', timeout=3)
        t.write(b'reboot\n')
        time.sleep(5)
        t.close()
