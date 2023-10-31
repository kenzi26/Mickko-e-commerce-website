from .services import UserProfileService
from .serializers import UserProfileSerializer
from django.http import JsonResponse
class UserProfileController():
    def find_me(user):
        profile = UserProfileService.find_or_create_me(user)
        profile_serializer = UserProfileSerializer(profile, many=False)
        data = profile_serializer.data
        data['email'] = profile.user.email
        data['full_name'] = profile.user.full_name
        return JsonResponse(data)

    def update_me(user,**kwargs):
        profile = UserProfileService.update_or_create_me(user, **kwargs)
        profile_serializer = UserProfileSerializer(profile, many=False)
        data = profile_serializer.data
        data['email'] = profile.user.email
        data['full_name'] = profile.user.full_name
        return JsonResponse(data)