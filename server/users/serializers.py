from django.contrib.auth.models import Group, Permission
from rest_framework import serializers

from .models import User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name",)


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(read_only=True, many=True)
    permissions = serializers.SerializerMethodField()
    gravatar = serializers.SerializerMethodField()

    def get_permissions(self, obj):
        perm_dict = dict()
        permissions = []
        for permission in obj.get_all_permissions():
            app_name, per_name = permission.split(".")
            perm_dict.setdefault(app_name, []).append(per_name)

        for key in perm_dict.keys():
            permissions.append({"model": key, "list": perm_dict[key]})
        return permissions

    def get_gravatar(self, obj):
        return obj.get_gravatar_url()

    class Meta:
        model = User
        fields = (
            "uuid",
            "username",
            "name",
            "email",
            "jwt",
            "groups",
            "permissions",
            "gravatar",
        )
