from .models import UserProfile
class UserProfileService():
    def find_or_create_me(user):
        profile = UserProfile.objects.get_or_create(user= user )
        return profile[0]

    def update_or_create_me(user, **kwargs):
        profile = UserProfileService.find_or_create_me(user)
        if kwargs.get('phone'):
            profile.phone = kwargs.get('phone')
        if kwargs.get('address'):
            profile.address = kwargs.get('address')
        if kwargs.get('email'):
            profile.email = kwargs.get('email')
        if kwargs.get('full_name'):
            profile.full_name =kwargs.get('full_name')
        profile.save()
        return profile