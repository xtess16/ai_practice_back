from cms.models.base import BaseTestPage, BaseArticlePage, MainPagePropertiesMixin


class MainTestPage(MainPagePropertiesMixin, BaseArticlePage):
    class Meta:
        verbose_name = 'Главная страница "Тесты"'


class TestPage(BaseTestPage):
    parent_page_types = ['cms.MainTestPage']

    class Meta:
        verbose_name = 'Тест'

