# from django.contrib import admin

# Register your models here.
import ctypes
import os

path = os.getcwd()
libLoadEcg = ctypes.cdll.LoadLibrary(path + '/libcn100_compress.so')

__int16 = ctypes.c_int16 * 11920 * 12

i = __int16()
print(i[0][0], "ii")
# Buf = [i for j in range(12)]
pBuf = ctypes.pointer(i)
pBuf.contents = i
# lpBuf = [[0*11920] for i in range(12)]
print(libLoadEcg.ReadReviewFile(path+'/20150519112355024161291461318950.003', pBuf.contents))
for i in range(11920):
    print(pBuf.contents[0][i],"xx")