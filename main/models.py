from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):

    location = models.CharField(max_length=100, null=True, blank=True)
    time_zone = models.IntegerField(null=True, blank=True)
    created_at = models.IntegerField(null=True, blank=True)
    profile_image_url = models.CharField(max_length=100, null=True, blank=True)
    screen_name = models.CharField(max_length=100, null=True, blank=True)
    source = models.CharField(max_length=150, null=True, blank=True)
 
    def __unicode__(self):         
        return self.screen_name

#location, time_zone, created_at, screen_name, profile_image_url

# #class Tweet(models.Model):
#     favorites = models.IntegerField()
#     lang = models.TextField()

#     def __unicode__(self):
#         return self.favorites


# class Place(models.Model):
#     country = models.CharField(max_length=100, null=True, blank=True)
#     place_type = models.CharField(max_length=100, null=True, blank=True)

#     def __unicode__(self):
#         return self.country


# class CustomUser(AbstractBaseUser, PermissionsMixin):  
#     email = models.EmailField('email address', max_length=255, unique=True)
#     first_name = models.CharField('first name', max_length=30, blank=True, null=True)
#     last_name = models.CharField('last name', max_length=30, blank=True, null=True)
#     is_staff = models.BooleanField('staff status', default=False)
#     is_active = models.BooleanField('active', default=True)
#     date_joined = models.DateTimeField('date joined', auto_now_add=True)
#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     class Meta:
#         verbose_name = 'user'
#         verbose_name_plural = 'users'

#     def get_absolute_url(self):
#         return "/users/%s/" % urlquote(self.email)

#     def get_full_name(self):
#         full_name = '%s %s' % (self.first_name, self.last_name)
#         return full_name.strip()

#     def get_short_name(self):
#         return self.first_name

#     def email_user(self, subject, message, from_email=None):
#         send_mail(subject, message, from_email, [self.email])