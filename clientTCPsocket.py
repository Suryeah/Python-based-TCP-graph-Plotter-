import socket 
from collections import deque
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.ion()

fig = plt.figure()
ay = fig.add_subplot(111)

host = '192.168.1.161'
port = 80

s = socket.socket()
s.connect((host,port))

while True:
    data = s.recv(1024)
    print (data)
    secPlot = ay.plot(data)
    fig.canvas.draw()
s.close()