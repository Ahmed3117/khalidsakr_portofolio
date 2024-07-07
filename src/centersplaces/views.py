from django.shortcuts import render

from centersplaces.models import Center, Class, Dates, Government

# Create your views here.

def centersplaces(request):
    governments = Government.objects.all()
    centers = Center.objects.all()
    cotext={
        'governments': governments,
        'centers': centers,
    }
    return render(request, 'centersplaces/centers.html',context=cotext)

def centerdates(request, center_id):
    center = Center.objects.get(id=center_id)
    classes = Class.objects.all()
    center_dates = Dates.objects.filter(center = center)
    cotext={
        'center': center,
        'classes': classes,
        'center_dates': center_dates,
    }
    return render(request, 'centersplaces/centerdates.html',context=cotext)