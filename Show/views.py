from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import auth

# Create your views here.
@login_required
def show(request):
    if request.method == 'POST':
        return render('xx')
    else:
        auth.logout(request)
        return render_to_response('Show.html')