from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=100)
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()

    rating =(
        (1, 'Worst'),
        (2, 'Bad'),
        (3, 'Not Bad'),
        (4, 'Good'),
        (5, 'Excellent'),
    )

    num_stats = models.IntegerField(choices=rating)
    def __str__(self):
        return self.name + ', Rating: ' + str(self.num_stats)

#We can input data using shell method

#py manage.py shell
# from api.models import Musician
# >>>obj = Musician(first_name = "jack", last_name = "ma", instrument = "guiter") 
# >>> obj.save()
# >>> print(Musician.objects.all()) cheak admin panel