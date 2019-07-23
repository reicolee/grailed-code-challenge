from django.db import models


class Users(models.Model):
    username = models.CharField(blank=True, null=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'users'

    @classmethod
    def username_exists(cls, username):
        return cls.objects.filter(username=username).exists()


class DisallowedUsernames(models.Model):
    invalid_username = models.CharField(blank=True, null=True, max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'disallowed_usernames'

    @classmethod
    def get_disallowed_usernames_list(cls):
        return cls.objects.values_list('invalid_username', flat=True)
