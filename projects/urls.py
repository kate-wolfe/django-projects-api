from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import ProjectViewSet, ImageViewSet, UserViewSet

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("projects", ProjectViewSet, basename="projects")
router.register("images", ImageViewSet, basename="images")

urlpatterns = router.urls
