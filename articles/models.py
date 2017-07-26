from django.db import models
from model_utils.models import TimeStampedModel
from ckeditor.fields import RichTextField

class Article(TimeStampedModel):
    author = models.CharField(max_length=100)
    article_content = RichTextField(null=True)



