import random
import socket
import sys
import time
import threading

def send(t, receiver):
    msg = '"{}":{}'.format(PID, t)
    print('<Send {} to {}>'.format(msg, receiver))
    sock.sendto(msg.encode(), ('127.0.0.1', 5000 + int(receiver[1])))

def listen():
    global msgs
    global broadcasted

    while True:
        msg, addr = sock.recvfrom(1024)
        print('<Receive {} from {}>'.format(msg.decode(), addr))

        msgs.update(eval('{' + msg.decode() + '}'))

        if not broadcasted:
            t = time.time_ns()
            msgs.update({PID: t})

            for receiver in IDS:
                send(t, receiver)

            broadcasted = True

        if len(msgs) == 5:
            leader = max(msgs, key = msgs.get)
            print('*{} is the leader*'.format(leader))
            
            msgs = {}
            broadcasted = False

if len(sys.argv) != 2:
    exit(0)

PID = sys.argv[1]
IDS = ['P1', 'P2', 'P3', 'P4', 'P5']
IDS.remove(PID)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 5000 + int(PID[1])))

threading.Thread(target = listen).start()

msgs = dict()
broadcasted = False

while True:
    input()
    t = time.time_ns()
    msgs = {PID: t}

    broadcasted = False

    random.shuffle(IDS)
    for receiver in IDS:
        send(t, receiver)

    broadcasted = True