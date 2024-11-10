from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField, RichTextUploadingFormField
from django.urls import reverse
from django.core.validators import URLValidator
from django.template.defaultfilters import slugify

# Create your models here.

#===========================================
#   Navigation Logo
# ==========================================


class navLogo(models.Model):
    img = models.ImageField(upload_to='logo/')

# Hero section slider 

# ==================================== -->
class homeSlider(models.Model):
    title = RichTextUploadingField()
    subtitle = RichTextUploadingField()
    description = RichTextUploadingField()
    bg_img = models.ImageField(upload_to='slides/')
    order = models.IntegerField(unique=True, help_text="Order of the sliding image section.")

    def __str__(self) :
        return f"slide {self.order}: {self.title}"
    
# ========================================
# courses category Section
# ========================================

class category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(category, self).save(*args, **kwargs)

    def __str__(self) :
        return self.name



# ==========================================
# courses section
# ==========================================

class course(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='course_images/', blank=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.title


# ===========================================
#  Mentors Section
# ===========================================



# Social Media Profile links
# ===========================================

class socialMediaProfile(models.Model):
    social_media_choices = (
        ('linkedin','linkedin'),
        ('twitter','twitter'),
        ('facebook','facebook'),
        ('instagram','instagram'),
        ('pinterest','pinterest'),
        ('youtube','youtube'),
    )

    team_member= models.ForeignKey('mentor',on_delete=models.CASCADE, related_name='social_media_profiles')
    platform = models.CharField(max_length=20,choices=social_media_choices)
    link = models.URLField(
        validators=[URLValidator(message="Enter a valid URL.")]
    )

    def __str__(self):
        return f"{self.team_member.name}'s {self.platform} Profile"
    
#    mentors 
# ============================================
class mentor(models.Model):
    img = models.ImageField(upload_to='mentors/')
    name = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    def __str__(self) :
        return self.name