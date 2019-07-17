from django.db import models


class Users(models.Model):
    username = models.CharField(blank=True, null=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'users'
class DisallowedUsernames(models.Model):
    invalid_username = models.CharField(blank=True, null=True, max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'disallowed_usernames'


