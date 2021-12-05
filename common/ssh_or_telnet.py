def ssh_or_telnet(gateway_ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result_ssh = sock.connect_ex((gateway_ip, 22))

    if result_ssh == 0:
        print('Доступно подключение по ssh для ip', gateway_ip)
        return True
    else:
        result_telnet = sock.connect_ex((gateway_ip, 23))
        if result_telnet ==0:
            print('Доступно подключение по telnet для ip',gateway_ip)
            return False
        else:
            print('\nssh и telnet недоступны на этом устройстве')
            sys.exit()
