from django.db import models

# Create your models here.

class Test(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject



class Model_laws_data(models.Model):
    subject = models.CharField(max_length=200)
    imgfile = models.ImageField(null=True, upload_to="", blank=True)  # Need to do "pip3 install image" in cmd
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Model_regulation_data(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Model_SKTL_Policy(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Model_GuideManual(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Model_Trend(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class FileUpload(models.Model):
    title = models.TextField(max_length=40, null=True)
    imgfile = models.ImageField(null=True, upload_to="", blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    imgfile = models.ImageField(null=True, upload_to="", blank=True)  # Need to do "pip3 install image" in cmd, upload_to 는 저장될경로로 ""는 media 폴더를 의미
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()