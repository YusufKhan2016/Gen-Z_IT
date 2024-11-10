from django.contrib import admin
from .models import *

# Register your models here.

# logo

admin.site.register(navLogo)

# home slider 

class slideAdmin(admin.ModelAdmin):
    list_display = ('title','order')

admin.site.register(homeSlider,slideAdmin)


# courses 

admin.site.register(category)
admin.site.register(course)

# Mentors
admin.site.register(socialMediaProfile)
admin.site.register(mentor)