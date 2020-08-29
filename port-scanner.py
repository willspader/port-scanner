import socket, threading


PORTS_PER_THREAD = 200


def isPortOpen(start, end, output, domain):
    try:
        for port in range(start, end + 1):
            print(f'Scanning port {port} ...\n')
            tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            tcpSocket.settimeout(2)
            output[port] = tcpSocket.connect_ex((domain, port))
            tcpSocket.close()
    except:
        pass


def threadScanning(domain):
    threads = [] # store all threads
    output = {} # store the return of the method isPortOpen

    start = 1
    for i in range(50):
        thread = threading.Thread(target=isPortOpen, args=(start, start + PORTS_PER_THREAD, output, domain))
        threads.append(thread)
        thread.start()

        start += PORTS_PER_THREAD

    for i in range(50):
        threads[i].join()

    print('===========')
    for i in range(1, 10000):
        if output[i] == 0:
            print(f'port {i} is open')


if __name__ == '__main__':
    threadScanning("www.python.org")
