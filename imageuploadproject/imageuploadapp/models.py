from django.db import models

# Create your models here.
class ImageUploadModel(models.Model):
    title=models.CharField(max_length=20)
    image=models.ImageField(upload_to='uploads')

    class Meta:
        db_table='users'