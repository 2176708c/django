from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime
from django.contrib.auth.models import User

now=datetime.now

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if self.views < 0:
            self.views = 0
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    first_visit = models.DateTimeField(null=True, blank = True)
    last_visit = models.DateTimeField(null=True, blank = True)

    def __str__(self):
        return self.title

class UserProfile(models.Model):

    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
