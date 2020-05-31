from django.http import JsonResponse

from .models import User, ActivityPeriod
from .serializers import ActivityPeriodSerializer


def users(request):
    if request.method == 'GET':
        users_activity = get_all_users_with_activity()
        response = {
            'ok': True,
            'members': users_activity
        }
        return JsonResponse(response)


def get_all_users_with_activity():
    users = User.objects.all()
    response = []
    for i in users:
        fuser = {'id': i.id,
                 'real_name': i.real_name,
                 'tz': i.tz,
                 'activity_periods': ActivityPeriodSerializer(ActivityPeriod.objects.filter(user_id=i.id), many=True).data}
        response.append(fuser)
    return response
