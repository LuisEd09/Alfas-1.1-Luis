from django.shortcuts import render

# Create your views here.
def renderizado(request):
    return render(request, 'Index.html')
