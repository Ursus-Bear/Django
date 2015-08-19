__author__ = 'clark'
__author__ = 'clark_liu'
import struct
# from cn100_common import SerialProcess
from matplotlib import pyplot
import os
import ctypes

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
    # lpBuf = SerialProcess.SerialPort().getAllData(lpBuf)
    return  lpBuf


path = os.getcwd()
# print(path)
libLoadEcg = ctypes.cdll.LoadLibrary(path + '/libcn100_compress.so')

__int16 = ctypes.c_int16* 11920 * 12

i = __int16()
# print(i[0][0], "ii")
# Buf = [i for j in range(12)]
pBuf = ctypes.pointer(i)
pBuf.contents = i
# lpBuf = [[0*11920] for i in range(12)]
print(libLoadEcg.ReadReviewFile(path+'/20150817144325921133720128602889.309', pBuf.contents))
# for i in range(11920):
#     print(pBuf.contents[0][i],"xx")
pyplot.figure(figsize=(8,2))
x = range(len(pBuf.contents[3]))
# print('x',x)
x = x[0:1750]
y3 = []
for i in x:
    y3.append(-pBuf.contents[3][i])
    # print(pBuf.contents[0][i])
pyplot.plot(x,y3, linewidth=1.0, label='avR')

# y4 = []
# for i in x:
#     y4.append(-pBuf.contents[4][i])
# pyplot.plot(x,y4, linewidth=1.0, label='avF')
#
# y5 = []
# for i in x:
#     y5.append(-pBuf.contents[5][i]-1000)
# pyplot.plot(x,y5, linewidth=1.0, label='avF')

pyplot.grid(True)
pyplot.show()

