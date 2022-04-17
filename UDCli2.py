"""#!/usr/bin/python3
import os
import time
new_pid = os.fork()

if new_pid == 0:
    pid = os.getpid()
    ppid = os.getppid()
    print("child process : PID= {} PPID= {}".format(pid, ppid))
else:
    pid = os.getpid()
    ppid = os.getppid()
    print("parent process : PID= {} PPID= {}".format(pid, ppid))
    time.sleep(15)
    system.exit(0)

    import signal
    import time

    def handler(signum, frame):
        print('Signal handler called with signal', signum)
        signal.signal(signal.SIGINT, handler)

     while True :
            print("Waiting...")
            time.sleep(5)
    sys.exit(0)
"""
"""#!/usr/bin/python3
import socket
import os
import errno
import signal
import socket
import sys


BACKLOG = 5
host = "0.0.0.0"
port = 10109

def collect_zombie(signum, frame):
    while True:
        try:
            pid, status = os.waitpid(-1, os.WNOHANG)
            if pid == 0:
                break
        except:
            break

def do_echo(sock):
    while True:
        message = sock.recv(1024)
        if message:
            sock.sendall(message)
        else:
            return
signal.signal(signal.SIGCHLD, collect_zombie)

conn_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
conn_sock.bind((host, port))
conn_sock.listen(BACKLOG)

print("Listening on port %d ..." %port)

while True:
    try:
        data_sock, client_address = conn_sock.accept()
        print('Got request from %s port %s...'%client_address)
    except IOError as e:
        if code == errno.EINTR:
            continue
        else:
            raise

    pid = os.fork()
    if pid == 0:
        conn_sock.close()
        do_echo(data_sock)
        os._exit(0)

    data_sock.close()
    
"""
