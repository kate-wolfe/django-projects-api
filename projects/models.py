from django.conf import settings
from django.db import models


class Project(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    craft_type_choices = [
        ("POT", "Pottery"),
        ("KNI", "Knitting or Crochet"),
        ("EMB", "Embroidery or Cross-stitch"),
        ("SEW", "Sewing"),
        ("WOO", "Woodworking"),
        ("OTH", "Other"),
    ]
    craft_type = models.CharField(max_length=3, choices=craft_type_choices)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True)
    object_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    notes = models.TextField(blank=True)
    clay_type = models.CharField(max_length=50, blank=True)
    glaze_type = models.CharField(max_length=50, blank=True)
    needle_size = models.CharField(max_length=50, blank=True)
    yarn_weight = models.CharField(max_length=50, blank=True)
    yarn_amount = models.CharField(max_length=50, blank=True)
    yarn_color = models.CharField(max_length=250, blank=True)
    fabric_info = models.CharField(max_length=250, blank=True)
    floss_color = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title

    def get_images(self):
        return Image.objects.filter(project_id=self)


class Image(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    project_id = models.ForeignKey("Project", on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to="images")
    cover_image = models.BooleanField()

    def __str__(self):
        return self.image_url
