import socket, threading

""" Check if a given port is open (TCP) """
def isPortOpen(port, output):
    tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpSocket.settimeout(2)

    try:
        output[port] = tcpSocket.connect_ex(("www.python.org", port))
    except:
        pass

""" starts the thread scanning for all ports, It creates one instance for each port. Range of ports = [1, 10000] """
def threadScanning():
    threads = [] # store all threads
    output = {} # store the return of the method isPortOpen

    for i in range(10001):
        thread = threading.Thread(target=isPortOpen, args=(i, output))
        threads.append(thread)
        thread.start()

    for i in range(10001):
        threads[i].join()

    for i in range(10001):
        if output[i] == 0:
            print(f'port {i} is open')

if __name__ == '__main__':
    threadScanning()
