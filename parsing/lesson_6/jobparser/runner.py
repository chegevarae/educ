from scrapy.crawler import CrawlerProcess           # Импортируем класс для создания процесса
from scrapy.settings import Settings                # Импортируем класс для настроек

from jobparser import settings                      # Наши настройки
from jobparser.spiders.hhru import HhruSpider       # Класс паука
from jobparser.spiders.sjru import SjruSpider       # Класс второго паука


if __name__ == '__main__':
    crawler_settings = Settings()                   # Создаем объект с настройками
    crawler_settings.setmodule(settings)            # Привязываем к нашим настройкам

    process = CrawlerProcess(settings=crawler_settings)     # Создаем объект процесса для работы
    process.crawl(HhruSpider)                               # Добавляем нашего паука
    process.crawl(SjruSpider)

    process.start()                                         # Пуск