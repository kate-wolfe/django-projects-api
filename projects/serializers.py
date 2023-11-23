from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Project, Image

from dj_rest_auth.registration.serializers import RegisterSerializer


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "user_id",
            "craft_type",
            "title",
            "description",
            "object_type",
            "start_date",
            "end_date",
            "notes",
            "clay_type",
            "glaze_type",
            "needle_size",
            "yarn_weight",
            "yarn_amount",
            "yarn_color",
            "fabric_info",
            "floss_color",
        )
        model = Project


class ImagesSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField()

    class Meta:
        model = Image
        fields = ["id", "project_id", "image_url", "cover_image"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username", "email", "first_name")


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField()

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            "username": self.validated_data.get("username", ""),
            "password1": self.validated_data.get("password1", ""),
            "password2": self.validated_data.get("password2", ""),
            "email": self.validated_data.get("email", ""),
            "first_name": self.validated_data.get("first_name", ""),
        }
