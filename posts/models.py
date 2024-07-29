from django.db import models

# Create your models here.
class Post(models.Model): # 장고에서 쓰는 규칙 models.Model 상속
    title = models.CharField(max_length=100) 
    # CharField 문자형 데이터 (짧은 글자), TextField 문자형 데이터(긴 글자)
    content = models.TextField()
