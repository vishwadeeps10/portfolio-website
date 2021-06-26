from django.db import models

# Create your models here.
class fromfordemo(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    email_id = models.EmailField(max_length=100)
    phoneno=models.CharField(max_length=15)
    content= models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return f'{self.name},{self.timestamp}'