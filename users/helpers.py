import re
from django.db.models import Count

from users.models import Users, DisallowedUsernames


class UsernamesResolutionHelper(object):
    def __init__(self, resolve_type='duplicates', dry_run=True):
        self.type = resolve_type
        self.dry_run = dry_run
        self.disallowed_usernames_list = DisallowedUsernames.get_disallowed_usernames_list()
        self.user_queries = getattr(
            self, '{}_username_queries'.format(resolve_type))()

    def duplicates_username_queries(self):
        duplicate_names_list = Users.objects.values("username").annotate(
            name_count=Count("username")).filter(name_count__gt=1)

        user_queries = Users.objects.filter(
            username__in=[item["username"] for item in duplicate_names_list]).exclude(username__in=self.disallowed_usernames_list)

        return user_queries

    def disallowed_username_queries(self):
        user_queries = Users.objects.filter(
            username__in=self.disallowed_usernames_list)
        return user_queries

    def update_users(self):
        updated_user_list = []
        usernames = {}

        for user in self.user_queries:
            if user.username not in usernames:
                usernames[user.username] = [user.id]

                if self.type == 'disallowed':
                    list_length = len(usernames[user.username])
                    user.username = '{}{}'.format(
                        user.username, str(list_length))
                    user.save()

            else:
                usernames[user.username].append(user.id)
                list_length = len(usernames[user.username])

                if self.type == 'duplicates':
                    match = re.search('\d', user.username)
                    username = user.username[:match.start(
                    )] if match is not None else user.username
                    num = user.username[match.start(
                    ):] if match is not None else 0
                    list_length = int(num) + list_length - 1

                while True:
                    username = username if self.type == 'duplicates' else user.username
                    potential_username = '{}{}'.format(
                        username, str(list_length))

                    if Users.username_exists(potential_username):
                        list_length += 1
                    else:
                        user.username = potential_username
                        user.save()
                        break

            updated_user_list.append(user)

        return updated_user_list

    def get_users(self):

        if self.dry_run:
            return self.user_queries

        updated_user_list = self.update_users()

        return updated_user_list
