from django.db.models import Count

from users.models import Users, DisallowedUsernames


class UsernamesResolutionHelper(object):
    def __init__(self, resolve_type='duplicates', dry_run=True):
        self.type = resolve_type
        self.dry_run = dry_run
        # self.hash_map = {}
        self.updated_user_list = []
        self.disallowed_usernames_list = DisallowedUsernames.get_disallowed_usernames_list()
        self.user_queries = getattr(self, resolve_type)()

    def duplicates(self):
        duplicate_names = Users.objects.values("username").annotate(
            name_count=Count("username")).filter(name_count__gt=1)

        user_queries = Users.objects.filter(
            username__in=[item["username"] for item in duplicate_names]).exclude(username__in=self.disallowed_usernames_list)

        return user_queries

    def disallowed(self):
        user_queries = Users.objects.filter(
            username__in=self.disallowed_usernames_list)
        return user_queries

    def get_users(self):

        if self.dry_run:
            return self.user_queries

        # for user in self.user_queries:

        return
