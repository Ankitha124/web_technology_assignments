from django.shortcuts import render

# Create your views here.
def resume(request):
    return render(request,'resume.html')

def css_rotation(request):
    return render(request,'css_rotation.html')

def layouts(request):
    return render(request,'layouts.html')

def transition(request):
    return render(request,'transition.html')

def swiggi(request):
    return render(request,'swiggi.html')