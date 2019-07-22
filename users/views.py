from django.db.models import Count

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import Users, DisallowedUsernames
from users.serializers import UsersSerializer

@api_view(['GET', 'POST'])
def duplicate_users(request):
    duplicates = Users.objects.values('username').annotate(name_count=Count('username')).filter(name_count__gt=1)
    rows = Users.objects.filter(username__in=[item['username'] for item in duplicates])

    data = UsersSerializer(rows, many=True).data

    return Response(duplicates)



@api_view(['GET', 'POST'])
def disallowed_users(request): 
    disallowed_usernames_list = DisallowedUsernames.objects.values_list('invalid_username', flat=True)
    user_instances = Users.objects.filter(username__in=disallowed_usernames_list)

    if request.method == 'GET':
        affected_rows = user_instances.values('id', 'username')
        data = UsersSerializer(affected_rows, many=True).data
        return Response(data)
    
    elif request.method == 'POST':
        # disallowed_names = Users.objects.filter(username__in=disallowed_usernames_list).values('username').annotate(name_count=Count('username')).filter(name_count__gt=1)
        disallowed_username_set = set()
        for user in user_instances: 
            if user.username not in disallowed_username_set: 

            user.username = '{}{}'.format(user.username, str(user.id))
            user.save()
        
        data = UsersSerializer(user_instances, many=True).data

        return Response(data)



    return Response(data)