import datetime

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.utils.translation import gettext as _
from rest_framework import exceptions, permissions, response, status, views
from rest_framework_jwt.settings import api_settings

from core.api_helper import set_error
from users.serializers import UserSerializer

from .authentication import JWTAuthentication

api_settings.JWT_EXPIRATION_DELTA = datetime.timedelta(days=365)

# Create your views here.
class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    errors = dict()

    def validate_data(self, data):
        if not data:
            set_error(self.errors, "data", _("There is no information on the data"))

        if not data.get("username", ""):
            set_error(self.errors, "username", _("There is no username information"))

        if not data.get("password", ""):
            set_error(self.errors, "password", _("There is no password information"))

    def validate_user(self, user):
        if not user.is_active:
            set_error(self.errors, "data", _("Inactive user in the system"))
            return None

        if user.jwt:
            set_error(self.errors, "data", _("User is already logged in"))
            return None

        return user

    def post(self, request):
        data = request.data
        self.errors = dict()

        self.validate_data(data)

        username = data.get("username", "")
        password = data.get("password", "")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            user = self.validate_user(user)
        else:
            set_error(self.errors, "data", _("username or password is invalid"))

        if self.errors:
            self.errors["detail"] = _("Error signing in")
            raise exceptions.AuthenticationFailed(detail=self.errors)

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        jwt = jwt_encode_handler(payload)

        user.jwt = jwt
        user.save()

        login(request, user)
        return response.Response(
            {
                "token": jwt,
                "payload": UserSerializer(user).data,
            }
        )


class LogoutView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user = request.user

        user.jwt = None
        user.save()

        logout(request)

        return response.Response({"detail": _("User successfully disconnected!")})


class GetUserView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user = request.user
        return response.Response(
            {
                "token": user.jwt,
                "payload": UserSerializer(user).data,
            }
        )
