from django.shortcuts import render

# Create your views here.

def condition(request):
    d={'a':5531000,'b':91000,'c':712800}
    return render(request,'condition.html',d)

