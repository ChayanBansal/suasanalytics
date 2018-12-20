from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'index.html', {})


def home_view(request):

    context={}
    return render(request, 'home.html', context)
