from django.db import models
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page

from cms.custom_fields import get_stream_field


class BaseArticlePage(Page):
    body = get_stream_field()
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
    api_fields = [
        APIField('body'),
    ]

    class Meta:
        abstract = True


class MainPagePropertiesMixin:
    max_count = 1
    parent_page_types = ['cms.MainPage']


class BaseTestPage(Page):
    body = StreamField(
        verbose_name='Контент',
        block_types=[
            ('paragraph', blocks.RichTextBlock(label='Параграф')),
            ('image', ImageChooserBlock(label='Изображение')),
            ('quote', blocks.BlockQuoteBlock(label='Цитата')),
            ('answers', blocks.ListBlock(blocks.CharBlock(label='Варианты ответов'), label='Варианты ответа'))
        ],
        use_json_field=True
    )
    correct_answer = models.CharField(verbose_name='Правильный ответ', max_length=128)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('correct_answer')
    ]
    api_fields = [
        APIField('title'),
        APIField('body'),
        APIField('correct_answer')
    ]

    class Meta:
        abstract = True
