from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from sso.service.models import Service


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        """
        Returns a Token for a given user,
        Adds audience claim to the token, based on user access to services
        """
        token = super().get_token(user)

        # Get all services the user has access to
        services = Service.for_user(user)
        token['aud']=[service.identifier for service in services]
        return token