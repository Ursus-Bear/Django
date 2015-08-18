__author__ = 'clark'
__author__ = 'clark_liu'
import struct
from cn100_common import SerialProcess
from matplotlib import pyplot

def LoadEcg():
    lpBuf = [[] for i in range(12)]
    ecg = open('Ecg500.dat', 'rb')
    is_break = False
    my_filter = 0
    while True:
        my_filter += 1
        for index in range(12):
            if index == 2 or index == 3\
                    or index == 4 or index == 5:
                continue
            one = ecg.read(2)
            if not one:
                is_break = True
                break
            value, = struct.unpack('<h', one)
            # print(value)
            if my_filter == 7:
                # print(my_filter)
                lpBuf[index].append(-value/25.0)
                # if index == 0 or index == 1:
                #     print(-value)
                # else:
                #     print(0)

        if my_filter == 7:
            my_filter = 0
        if is_break:
            break
    ecg.close()
    lpBuf = SerialProcess.SerialPort().getAllData(lpBuf)
    return  lpBuf


lpBuf = LoadEcg()
pyplot.figure()
x = range(len(lpBuf[0]))
pyplot.plot(x,lpBuf[0], linewidth=1.0)
pyplot.grid(True)
pyplot.show()
