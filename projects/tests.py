from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Project, Image


class ProjectTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            first_name="test1",
            email="test@email.com",
            password="secret",
        )

        cls.project = Project.objects.create(
            user_id=cls.user,
            craft_type="POT",
            title="Test Title",
            description="Test description.",
            object_type="Mug",
            start_date="2022-10-31",
            end_date="2023-01-01",
            notes="Test extended notes.",
            clay_type="Speckled Stoneware",
            glaze_type="Black",
            needle_size="8 mm",
            yarn_weight="Worsted",
            yarn_amount="5 skeins",
            yarn_color="Blue",
            fabric_info="14 count Aida",
            floss_color="Neon Green",
        )

    def test_project_model(self):
        self.assertEqual(self.project.user_id.username, "testuser")
        self.assertEqual(self.project.craft_type, "POT")
        self.assertEqual(self.project.title, "Test Title")
        self.assertEqual(self.project.description, "Test description.")
        self.assertEqual(self.project.object_type, "Mug")
        self.assertEqual(self.project.start_date, "2022-10-31")
        self.assertEqual(self.project.end_date, "2023-01-01")
        self.assertEqual(self.project.notes, "Test extended notes.")
        self.assertEqual(self.project.clay_type, "Speckled Stoneware")
        self.assertEqual(self.project.glaze_type, "Black")
        self.assertEqual(self.project.needle_size, "8 mm")
        self.assertEqual(self.project.yarn_weight, "Worsted")
        self.assertEqual(self.project.yarn_amount, "5 skeins")
        self.assertEqual(self.project.yarn_color, "Blue")
        self.assertEqual(self.project.fabric_info, "14 count Aida")
        self.assertEqual(self.project.floss_color, "Neon Green")
        self.assertEqual(str(self.project), "Test Title")
