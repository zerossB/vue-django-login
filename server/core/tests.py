from django.test import TestCase
from rest_framework_jwt.settings import api_settings

from users.models import User


# Create your tests here.
class GeneralTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(GeneralTest, cls).setUpClass()

    def get_jwt(self, user=None, email=None):
        if not user:
            user = User.objects.filter(group=1).first()
        elif email:
            user = User.objects.filter(email=email).first()

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        jwt = jwt_encode_handler(payload)

        user.jwt = jwt
        user.save()

        return "JWT {}".format(user.jwt), user
