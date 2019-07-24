from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.serializers import UsersSerializer

from users.helpers import UsernamesResolutionHelper


@api_view(['GET'])
def index(request):
    users = Users.objects.all()
    data = UsersSerializer(users, many=True).data
    return Response(data)


@api_view(["GET", "POST"])
def duplicate_users(request):

    if request.method == "GET":
        affected_users = UsernamesResolutionHelper(
            resolve_type='duplicates', dry_run=True).get_users()
        data = UsersSerializer(affected_users, many=True).data
        return Response(data)

    if request.method == "POST":
        updated_user_list = UsernamesResolutionHelper(
            resolve_type='duplicates', dry_run=False).get_users()
        data = UsersSerializer(updated_user_list, many=True).data

        return Response(data)


@api_view(["GET", "POST"])
def disallowed_users(request):

    if request.method == "GET":
        affected_users = UsernamesResolutionHelper(
            resolve_type='disallowed', dry_run=True).get_users()
        data = UsersSerializer(affected_users, many=True).data
        return Response(data)

    elif request.method == "POST":
        updated_user_list = UsernamesResolutionHelper(
            resolve_type='disallowed', dry_run=False).get_users()
        data = UsersSerializer(updated_user_list, many=True).data

        return Response(data)
        # edge case - need to check if it collides with existing user names with potential usernames
        # edge case - what if there are numeric value at the end such as about1
