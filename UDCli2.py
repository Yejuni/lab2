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

from socket import *
import os
import sys

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('203.250.133.88',10109))

print('연결에 성공했습니다.')
filename = input('전송할 파일 이름을 입력하세요: ')
clientSock.sendall(filename.encode('utf-8'))

data = clientSock.recv(1024)
data_transferred = 0

if not data:
    print('파일 %s 가 서버에 존재하지 않음' %filename)
    sys.exit()

nowdir = os.getcwd()
with open(nowdir+"\\"+filename, 'wb') as f: #현재dir에 filename으로 파일을 받는다
    try:
        while data: #데이터가 있을 때까지
            f.write(data) #1024바이트 쓴다
            data_transferred += len(data)
            data = clientSock.recv(1024) #1024바이트를 받아 온다
    except Exception as ex:
        print(ex)
print('파일 %s 받기 완료. 전송량 %d' %(filename, data_transferred))