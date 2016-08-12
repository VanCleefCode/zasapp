from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import Signal
import datetime

# A new user has registered.
TIPO = [('Ventas','Ventas'),('Consultoria','Consultoria'),('Mercadeo','Mercadeo'),('Administacion','Administacion'),('Sistemas','Sistemas'),]
user_registered = Signal(providing_args=["user", "request"])

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    telefono = models.CharField(max_length=20,blank=True)
    tipo = models.CharField(max_length=20,choices=TIPO,blank=True)
    thumbnail = models.ImageField(upload_to = 'pic_folder_vendedores/', default = 'pic_folder/None/no-img.png') 
    created_at = models.DateTimeField(editable=False)
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = datetime.datetime.now()
        return super(UserProfile, self).save(*args, **kwargs)

def assure_user_profile_exists(pk):
    """
    Creates a user profile if a User exists, but the
    profile does not exist.  Use this in views or other
    places where you don't have the user object but have the pk.
    """
    user = User.objects.get(pk=pk)
    try:
        # fails if it doesn't exist
        userprofile = user.userprofile
    except UserProfile.DoesNotExist, e:
        userprofile = UserProfile(user=user)
        userprofile.save()
    return



def create_user_profile(**kwargs):
    UserProfile.objects.get_or_create(user=kwargs['user'])

user_registered.connect(create_user_profile)