from django.db import models
from uuid import uuid4
from datetime import datetime
# Create your models here

def get_file_path(instance, filename):
    ymd_path = datetime.now().strftime('%Y/%m/%d')
    uuid_name = uuid4().hex
    return '/'.join(['upload_file/', ymd_path, uuid_name])

class Model_laws_data(models.Model):
    subject = models.CharField(max_length=200)
    upload_files = models.FileField(upload_to=get_file_path, null=True, blank=True, verbose_name='파일')
    filename = models.CharField(max_length=64, null=True, verbose_name='첨부파일명')
    imgfile = models.ImageField(null=True, upload_to=get_file_path, blank=True, verbose_name='이미지')  # Need to do "pip3 install image" in cmd
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Model_regulation(models.Model):
    subject = models.CharField(max_length=200)
    upload_files = models.FileField(upload_to=get_file_path, null=True, blank=True, verbose_name='파일')
    filename = models.CharField(max_length=64, null=True, verbose_name='첨부파일명')
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Model_SKTL_policy(models.Model):
    subject = models.CharField(max_length=200)
    upload_files = models.FileField(upload_to=get_file_path, null=True, blank=True, verbose_name='파일')
    filename = models.CharField(max_length=64, null=True, verbose_name='첨부파일명')
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Model_guide(models.Model):
    subject = models.CharField(max_length=200)
    upload_files = models.FileField(upload_to=get_file_path, null=True, blank=True, verbose_name='파일')
    filename = models.CharField(max_length=64, null=True, verbose_name='첨부파일명')
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Model_trend(models.Model):
    subject = models.CharField(max_length=200)
    upload_files = models.FileField(upload_to=get_file_path, null=True, blank=True, verbose_name='파일')
    filename = models.CharField(max_length=64, null=True, verbose_name='첨부파일명')
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Model_magazine(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True, default='images/no_img.jpg')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    # modify_date = models.DateTimeField(null=True, blank=True)

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

class laws_Answer(models.Model):
    laws_data = models.ForeignKey(Model_laws_data, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

class regulation_Answer(models.Model):
    regulation = models.ForeignKey(Model_regulation, null=True, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

class SKTL_policy_Answer(models.Model):
    SKTL_policy = models.ForeignKey(Model_SKTL_policy, null=True, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

class guide_Answer(models.Model):
    guide = models.ForeignKey(Model_guide, null=True, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

class trend_Answer(models.Model):
    trend = models.ForeignKey(Model_trend, null=True, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

class magazine_Answer(models.Model):
    magazine = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()