from wagtail.admin.panels import FieldPanel
from django.db import models
from wagtail.api import APIField

from cms.models.base import MainPagePropertiesMixin, BaseArticlePage


class MainPage(MainPagePropertiesMixin, BaseArticlePage):
    class Meta:
        verbose_name = 'Главная страница'


class BigDataMainPage(MainPagePropertiesMixin, BaseArticlePage):
    class Meta:
        verbose_name = 'Главная страница "Большие данные"'


class AIHistoryMainPage(MainPagePropertiesMixin, BaseArticlePage):
    class Meta:
        verbose_name = 'Главная страница "История развития ИИ"'


class ComputerVisionMainPage(MainPagePropertiesMixin, BaseArticlePage):
    class Meta:
        verbose_name = 'Главная страница "Компьютерное зрение"'


class MachineLearningMainPage(MainPagePropertiesMixin, BaseArticlePage):
    class Meta:
        verbose_name = 'Главная страница "Машинное обучение"'


class ArticlePage(BaseArticlePage):
    preview_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, null=True)
    parent_page_types = [
        'cms.BigDataMainPage', 'cms.AIHistoryMainPage', 'cms.ComputerVisionMainPage',
        'cms.MachineLearningMainPage'
    ]
    content_panels = [FieldPanel('preview_image')] + BaseArticlePage.content_panels
    api_fields = [APIField('preview_image')] + BaseArticlePage.api_fields

    class Meta:
        verbose_name = 'Статья'
