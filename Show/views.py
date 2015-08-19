from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponse

import ctypes
import os
from matplotlib import pyplot


# Create your views here.
@login_required
def show(request):
    if request.method == 'POST':
        return render('xx')
    else:
        auth.logout(request)
        path = os.getcwd()
        path += '/Show'
        # print(path)
        libLoadEcg = ctypes.cdll.LoadLibrary(path + '/libcn100_compress.so')

        __int16 = ctypes.c_int16* 11920 * 12

        i = __int16()
        # print(i[0][0], "ii")
        # Buf = [i for j in range(12)]
        pBuf = ctypes.pointer(i)
        pBuf.contents = i
        # lpBuf = [[0*11920] for i in range(12)]
        print(libLoadEcg.ReadReviewFile(path+'/20150519112355024161291461318950.003', pBuf.contents))
        # for i in range(11920):
        #     print(pBuf.contents[0][i],"xx")
        pyplot.figure()
        x = range(len(pBuf.contents[0]))
        print('x',len(pBuf.contents[0]))
        y = []
        for i in x:
            y.append(pBuf.contents[0][i])
            # print(pBuf.contents[0][i])
        pyplot.plot(x,y, linewidth=1.0)
        pyplot.grid(True)
        # pyplot.show()
        return render_to_response('Show.html')
        # return reponse