from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index_view(request):
    return render(request, 'index.html', {})

@login_required
def home_view(request):

    context={}
    return render(request, 'home.html', context)
