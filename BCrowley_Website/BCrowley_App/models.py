from django.db import models

# Create your models here.
class Media(models.Model):
    BOOK = 'BK'
    MOVIE = 'MV'
    MUSIC = 'MS'
    ARTICLE = 'AT'

    ONESTAR = 1
    TWOSTARS = 2
    THREESTARS = 3
    FOURSTARS = 4
    FIVESTARS = 5

    TYPE_CHOICES = (
    (BOOK, 'Book'),
    (MOVIE, 'Movie'),
    (MUSIC, 'Music'),
    (ARTICLE, 'Article'),
    )

    RATING_CHOICES = (
    (ONESTAR, 1),
    (TWOSTARS, 2),
    (THREESTARS, 3),
    (FOURSTARS, 4),
    (FIVESTARS, 5),
    )

    med_type = models.CharField(max_length=264,unique=False,choices=TYPE_CHOICES)
    id_name = models.CharField(max_length=264,unique=False)
    title = models.CharField(max_length=264,unique=False)
    author = models.CharField(max_length=264,unique=False)
    cover_photo = models.URLField(max_length=264,unique=False)
    online_reference = models.URLField(max_length=264,unique=False)
    rating = models.IntegerField(unique=False,choices=RATING_CHOICES)
    review = models.TextField(unique=False)

    def __str__(self):
        return self.title

class Inspiration(models.Model):

    QUOTE = 'QT'
    SPEECH = 'SP'
    CREATIVE = 'CR'

    TYPE_CHOICES = (
    (QUOTE, 'Quote'),
    (SPEECH, 'Speech'),
    (CREATIVE, 'Creative'),
    )

    ins_type = models.CharField(max_length=264,unique=False,choices=TYPE_CHOICES)
    id_name = models.CharField(max_length=264,unique=False)
    cover_photo = models.URLField(max_length=264,unique=False, blank=True)
    author=models.CharField(max_length=264,unique=False,default='Unknown')
    online_reference = models.URLField(max_length=264,unique=False,blank=True)
    description = models.TextField(unique=False)

    def __str__(self):
        return self.id_name

class Project(models.Model):

    project_name = models.CharField(max_length=264,unique=False)
    cover_photo = models.FilePathField(path='/home/brettcrowley77/bcrowley-website/BCrowley_Website/static/img')
