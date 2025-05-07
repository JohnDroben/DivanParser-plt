# 3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные,
# найти среднюю цену и вывести ее, а также сделать гистограмму цен на диваны.

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from divanparser.spiders.divannewparser import DivannewparsSpider
from divanparser.analisis.data_analysis import (analyze_data)
import time

if __name__ == "__main__":
    # Запуск паука
    process = CrawlerProcess(get_project_settings())
    process.crawl(DivannewparsSpider)
    process.start()

    # Задержка для завершения записи файла
    print("Парсинг завершен")
    time.sleep(2)

    # После завершения парсинга запускаем анализ
    analyze_data()
    print("Анализ завершен")

