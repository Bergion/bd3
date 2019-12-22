# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class SocialNetworkBlog(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField()
    user = models.ForeignKey('SocialNetworkCustomuser', models.DO_NOTHING, unique=True)

    class Meta:
        managed = True
        db_table = 'social_network_blog'

    def __str__(self):
        return self.name


class SocialNetworkCustomuser(models.Model):
    password = models.CharField(max_length=128)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)

    class Meta:
        managed = True
        db_table = 'social_network_customuser'

    def __str__(self):
        return self.username

class SocialNetworkPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField()
    blog = models.ForeignKey(SocialNetworkBlog, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'social_network_post'

    def __str__(self):
        return self.title

class SocialNetworkRate(models.Model):
    value = models.CharField(max_length=1)
    post = models.ForeignKey(SocialNetworkPost, models.DO_NOTHING)
    user = models.ForeignKey(SocialNetworkCustomuser, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'social_network_rate'
        unique_together = (('user', 'post'),)

    def __str__(self):
        return self.value