import re
from django.db.models import Count

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import Users, DisallowedUsernames
from users.serializers import UsersSerializer

from users.helpers import UsernamesResolutionHelper


@api_view(['GET'])
def index(request):
    users = Users.objects.all()
    data = UsersSerializer(users, many=True).data
    return Response(data)


@api_view(["GET", "POST"])
def duplicate_users(request):
    user_instances = UsernamesResolutionHelper().get_users()

    if request.method == "GET":
        data = UsersSerializer(user_instances, many=True).data
        return Response(data)

    if request.method == "POST":
        hash_map = {}
        updated_list = []
        for user in user_instances:
            if user.username not in hash_map:
                hash_map[user.username] = [user.id]
            else:
                hash_map[user.username].append(user.id)
                list_length = len(hash_map[user.username])

                match = re.search('\d', user.username)
                username = user.username[:match.start(
                )] if match is not None else user.username
                num = user.username[match.start():] if match is not None else 0
                digit = int(num) + list_length - 1

                while True:
                    potential_username = "{}{}".format(
                        username, str(digit))
                    if Users.username_exists(potential_username):
                        digit += 1
                    else:
                        user.username = potential_username
                        user.save()
                        break
                # edge case - what if the number is not at the end

        data = UsersSerializer(user_instances, many=True).data

        return Response(data)


@api_view(["GET", "POST"])
def disallowed_users(request):
    user_instances = user_instances = UsernamesResolutionHelper(
        resolve_type='disallowed').get_users()

    if request.method == "GET":
        data = UsersSerializer(user_instances, many=True).data
        return Response(data)

    elif request.method == "POST":
        updated_list = []
        hash_map = {}
        for user in user_instances:
            if user.username not in hash_map:
                hash_map[user.username] = [user.id]
                list_length = len(hash_map[user.username])

                user.username = "{}{}".format(user.username, str(list_length))
                user.save()
            else:
                hash_map[user.username].append(user.id)
                list_length = len(hash_map[user.username])

                while True:
                    potential_username = "{}{}".format(
                        user.username, str(list_length))

                    if Users.username_exists(potential_username):
                        list_length += 1
                    else:
                        user.username = potential_username
                        user.save()
                        break

                # edge case - need to check if it collides with existing user names with potential usernames
                # edge case - what if there are numeric value at the end such as about1

            updated_list.append(user)

        data = UsersSerializer(updated_list, many=True).data

        return Response(data)
