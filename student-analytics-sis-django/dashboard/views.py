from django.http import JsonResponse
from django.shortcuts import render,redirect,reverse
from django.contrib.auth.decorators import login_required
from .forms import CorrForm


def index_view(request):
    return render(request, 'index.html', {})

@login_required
def home_view(request):

	if request.method=="POST": 	#Obtaining selected value of corelation options
		correl_type=int(request.POST['correl_type'])
		
		if correl_type==1:
			return redirect('dashboard:corr_view3') #Use namespace : to resolve URL name!!
	
	context={}
	return render(request, 'dashboard/home.html', context)

def corr_view3(request):
    my_form = CorrForm()
    return render(request,'dashboard/corr_view3.html',{'form': my_form})

def corr_view3_getEnrollYear(request):
    if request.method=="POST":
        
        return JsonResponse({'key1':'value1','key1':'value1', 'key1':'value1'})
	