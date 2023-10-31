from rest_framework import viewsets
from .serializers import UserProfile, UserProfileSerializer
from .controllers import UserProfileController
from rest_framework.decorators import action
from user.models import User
class UserProfileViewSet(viewsets.ModelViewSet):
    """ This fetches all users in the UserProfile model and perform CRUD operations on them using the
    UserProfile model as well as the UserProfile serializer using a form parser for easy data entry"""

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = []
    @action(detail=False,url_path="me", methods=['GET','PUT'], name='Get User Details')
    def find_me(self, request):
        user = User.objects.get(id=request.user.id)
        data = dict(request.data)
        if data.get("user"):
            data.pop("user")
        if request.method == "GET":
            return UserProfileController.find_me(user)
        return UserProfileController.update_me(user, **data)