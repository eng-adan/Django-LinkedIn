from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def home(request):
    return HttpResponse('Hello World')

@login_required
def authorized(request):
    return render(request, 'authorized.html', {})
