from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    active= models.BooleanField(default=True)
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        return self.title
    

class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE) 
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating) + " | " + self.watchlist.title + "| " + str(self.review_user)
# Create your models here.
# 3 relationship methods, 1:1, 1:many, many:many. https://docs.djangoproject.com/en/5.1/topics/db/examples/

#See below for make migrations example after adding "platform variable"
'''^C(.gbenv) administrator@administrator-VMware-Virtual-Platform:~/Documents/watchlist$ python watchmateProject/manage.py makemigrations
Was watchlist.name renamed to watchlist.title (a CharField)? [y/N] y
It is impossible to add a non-nullable field 'platform' to watchlist without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option: 1
Please enter the default value as valid Python.
The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
Type 'exit' to exit this prompt
>>> None
Migrations for 'watchlist_app':
  watchmateProject/watchlist_app/migrations/0003_rename_name_watchlist_title_watchlist_platform.py
    ~ Rename field name on watchlist to title
    + Add field platform to watchlist
(.gbenv) administrator@administrator-VMware-Virtual-Platform:~/Documents/watchlist$ ^C'''