from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CorrForm
# Create your views here.
def index_view(request):
    return render(request, 'index.html', {})

@login_required
def home_view(request):

    context={}
    return render(request, 'dashboard/home.html', context)

def corr_view(request):
    form = CorrForm()
    return render(request,'corr.html',form)