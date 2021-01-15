from django.shortcuts import render
from .searchIllness import SearchIllness

# Create your views here.

def mainView(request):
    context = {}
    #input = str(request.readline())

    if request.method == 'POST':
        context = SearchIllness.search(request)
    print(context)
    return render(request, "home.html", context)