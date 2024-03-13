from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    singer = models.CharField(max_length=500)
    tags = models.CharField(max_length=100) 
    image = models.ImageField(upload_to='media/images')
    Song = models.FileField(upload_to='media/songs')
    movie = models.CharField(max_length=1000,default='')
    price=models.FloatField(default='199')
    # category= models.
    ALBUM_CHOICES = (
        ('TREANDING','treanding'),
        ('HINDI', 'Hindi'),
        ('ENGLISH', 'English'),
        ('MARATHI', 'Marathi'),
        ('DEVOTIONAL', 'devotional')
    )  

    categories= models.CharField(max_length=100, choices=ALBUM_CHOICES,default='NA')
    
    def __str__(self):
        return self.name
    

class Favourite(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    music_id=  models.CharField(max_length=20000000,default='')
    
    

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return(str(self.id))


class Download(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ForeignKey(song, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    download = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return str(self.id)


    