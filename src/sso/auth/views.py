from rest_framework_simplejwt.views import TokenObtainPairView

from sso.auth.serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Takes a set of user credentials and returns an access and refresh token pair.
    """
    serializer_class = CustomTokenObtainPairSerializer