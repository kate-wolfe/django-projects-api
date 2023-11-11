from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import ProjectViewSet, ImageViewSet, UserViewSet

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("projects", ProjectViewSet, basename="projects")
router.register("images", UserViewSet, basename="images")

urlpatterns = router.urls
