```markdown
# Парсер цен на диваны с divan.ru (

Проект для сбора данных о ценах на диваны с сайта divan.ru, анализа полученных данных и визуализации результатов.

## Особенности

- Парсинг данных с пагинацией
- Сохранение результатов в CSV-файл
- Расчет средней цены
- Построение гистограммы распределения цен
- Автоматическая обработка ошибок

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/JohnDroben/DivanParser-plt.git
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

Или вручную:
```bash
pip install scrapy matplotlib
```

## Использование

Запуск проекта:
```bash
python main.py
```

После выполнения:
1. Данные сохранятся в `divan_prices.csv`
2. В консоли отобразится средняя цена
3. Откроется окно с гистограммой цен

## Структура проекта

```
DivanParser/
├── main.py              # Главный скрипт для запуска
├── requirements.txt     # Список зависимостей
├── divanparser/
│   ├── spiders/
│   │   └── divan_spider.py  # Паук для парсинга
│   ├── analysis/
│   │   └── data_analysis.py # Анализ данных
│   └── settings.py      # Настройки Scrapy
└── README.md
```

## Зависимости

- Python 3.10+
- Scrapy 2.12+
- Matplotlib 3.5+
- lxml

## Лицензия

MIT License
```



