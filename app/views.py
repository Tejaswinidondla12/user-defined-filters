from django.shortcuts import render

# Create your views here.
def userdefinedfilters(request):
    d={'data':'HI Python HoW R yoU'}
    return render(request,'userdefinedfilters.html',d)