from django import forms
from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from cards_api.models import Card


class Article(TimeStampedModel, forms.ModelForm):
    author = models.CharField(max_length=100)
    content = forms.TextField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30})) #TODO Fix content field
    card = models.ForeignKey('cards_api.Card', null=True, blank=True)

    class Meta:
        model = FlatPage
