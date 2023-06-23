from wagtail import blocks
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock


def get_stream_field():
    return StreamField(
        verbose_name='Контент',
        block_types=[
            ('paragraph', blocks.RichTextBlock(label='Параграф')),
            ('image', ImageChooserBlock(label='Изображение')),
            ('quote', blocks.BlockQuoteBlock(label='Цитата'))
        ],
        use_json_field=True,
        blank=True
    )
