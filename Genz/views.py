from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    logo = navLogo.objects.first()
    slides = homeSlider.objects.order_by('order')
    courses = course.objects.all()
    categories = category.objects.all()
    socialMediaProfiles = socialMediaProfile.objects.all()
    mentors = mentor.objects.all()

    context = {
        'slides':slides,
        'courses':courses,
        'categories': categories,
        'socialMediaProfiles':socialMediaProfiles,
        'mentors':mentors,
        'logo':logo,
    }
    
    return render(request, 'index.html',context)