from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Project, Image
from .permissions import IsAuthorOrReadOnly
from .serializers import ProjectSerializer, ImagesSerializer, UserSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user_id=self.request.user)


class ImageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Image.objects.all()
    serializer_class = ImagesSerializer

    def get_queryset(self):
        return super().get_queryset().filter(Project.get_images(Project.id))


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
