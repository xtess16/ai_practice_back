from django.core.management import BaseCommand
from django.db import transaction
from wagtail.models import Page, Site

from cms.models import MainPage, BigDataMainPage, AIHistoryMainPage, ComputerVisionMainPage, \
    MachineLearningMainPage, MainTestPage


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--recreate', action='store_true')

    def handle(self, *args, **options):
        if options['recreate']:
            Page.objects.not_exact_type(Page).delete()
            self.stdout.write(self.style.SUCCESS('Страницы удалены'))

        children = [{
            'model': BigDataMainPage,
        }, {
            'model': AIHistoryMainPage,
        }, {
            'model': ComputerVisionMainPage,
        }, {
            'model': MachineLearningMainPage,
        }, {
            'model': MainTestPage
        }]
        root_page = Page.objects.exact_type(Page).get(title='Root')
        self.stdout.write(self.style.SUCCESS(f'Корневая страница найдена: {root_page}'))
        try:
            main_page = MainPage.objects.get()
            self.stdout.write(self.style.SUCCESS(f'Главная страница найдена: {main_page}'))
        except MainPage.DoesNotExist:
            main_page = MainPage(
                title='Домашняя страница',
                body=[{'type': 'paragraph', 'value': 'Добро пожаловать!'}],
                slug=MainPage.__name__.lower()
            )
            with transaction.atomic():
                root_page.add_child(instance=main_page)
                main_page.save()
            self.stdout.write(self.style.SUCCESS(f'Главная страница создана: {main_page}'))

        site, created = Site.objects.get_or_create(
            root_page=main_page,
            defaults={
                'hostname': 'localhost',
                'port': '8001',
                'site_name': 'AI Practice',
                'is_default_site': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Сайт создан: {site}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Сайт уже существует: {site}'))
        for page in children:
            if not page['model'].objects.exists():
                with transaction.atomic():
                    added_page = page['model'](
                        title=page.get('title', page['model']._meta.verbose_name),
                        body=page.get('body', ''),
                        slug=page['model'].__name__.lower()
                    )
                    main_page.add_child(instance=added_page)
                    added_page.save()
                self.stdout.write(self.style.SUCCESS(f'{page["model"]._meta.verbose_name} создана'))
            else:
                self.stdout.write(self.style.SUCCESS(f'{page["model"]._meta.verbose_name} существует'))
