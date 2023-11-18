from django.db import models

# Create your models here.
class Blog(models.Model):

    title = models.CharField(max_length=255)
    descrption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/")
    pop_post = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.title
    

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
