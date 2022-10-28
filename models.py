from django.db import models

# Create your models here.
class Artiste(models.Model):
   First_name= models.CharField(max_length=400)
   Last_name= models.CharField(max_length=400)
   Age= models.IntegerField( )


class Song(models.Model): 
     # Artiste=models.foreignkey(Artiste, on_delete=models.CASCADE) 
    Title=models.CharField(max_length=40)
    Date_released=models.DateField(auto_now=False)  
    Likes=models.IntegerField(400)
    Artiste_id=models.IntegerField(400)

class Lyric(models.Model):
    #song=models.Foreignkey(song,on delete=models.CASCADE)
    Content=models.CharField(max_length=400)
    Songs_id=models.CharField(max_length=400)