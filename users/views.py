import re
from django.db.models import Count

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import Users, DisallowedUsernames
from users.serializers import UsersSerializer


@api_view(['GET'])
def index(request):
    users = Users.objects.all()
    data = UsersSerializer(users, many=True).data
    return Response(data)


@api_view(["GET", "POST"])
def duplicate_users(request):
    duplicates = Users.objects.values("username").annotate(
        name_count=Count("username")).filter(name_count__gt=1)
    disallowed_usernames_list = DisallowedUsernames.objects.values_list(
        "invalid_username", flat=True
    )
    user_instances = Users.objects.filter(
        username__in=[item["username"] for item in duplicates])

    if request.method == "GET":
        data = UsersSerializer(user_instances, many=True).data
        return Response(data)

    if request.method == "POST":
        hash_map = {}
        for user in user_instances:

            if user.username in disallowed_usernames_list:
                continue

            if user.username not in hash_map:
                hash_map[user.username] = [user.id]
            else:
                hash_map[user.username].append(user.id)

        for username, id_list in hash_map.items():
            for index, user_id in enumerate(id_list):
                if index > 0:
                    try:
                        user = Users.objects.get(id=user_id)
                    except Users.DoesNotExist:
                        continue

                    match = re.search("\d", user.username)
                    username = user.username[:match.start(
                    )] if match is not None else user.username
                    num = user.username[match.start(
                    ):] if match is not None else 0
                    digit = int(num) + index
                    while True:
                        potential_username = "{}{}".format(
                            username, str(digit))
                        if Users.objects.filter(username=potential_username).exists():
                            digit += 1
                        else:
                            user.username = potential_username
                            user.save()
                            break

        data = UsersSerializer(user_instances, many=True).data

        return Response(user_instances)


@api_view(["GET", "POST"])
def disallowed_users(request):
    disallowed_usernames_list = DisallowedUsernames.objects.values_list(
        "invalid_username", flat=True
    )
    user_instances = Users.objects.filter(
        username__in=disallowed_usernames_list)

    if request.method == "GET":
        affected_rows = user_instances.values("id", "username")
        data = UsersSerializer(affected_rows, many=True).data
        return Response(data)

    elif request.method == "POST":
        # disallowed_names = Users.objects.filter(username__in=disallowed_usernames_list).values('username').annotate(name_count=Count('username')).filter(name_count__gt=1)
        hash_map = {}
        updated_list = []
        for user in user_instances:
            if user.username not in hash_map:
                hash_map[user.username] = [user.id]
            else:
                hash_map[user.username].append(user.id)

        for username, id_list in hash_map.items():
            for i, user_id in enumerate(id_list):
                try:
                    user = Users.objects.get(id=user_id)
                except Users.DoesNotExist:
                    continue

                user.username = "{}{}".format(username, str(i + 1))
                user.save()
                updated_list.append(user)

        data = UsersSerializer(updated_list, many=True).data

        return Response(data)


def hashing(user_instances):
    return


def update_duplicate_username()


return
