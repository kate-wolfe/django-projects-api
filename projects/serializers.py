from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Project, Image


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
        fields = (
            "id",
            "username",
            "first_name",
            "email",
        )
