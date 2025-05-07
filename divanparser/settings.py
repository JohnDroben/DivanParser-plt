BOT_NAME = 'divanparser'

SPIDER_MODULES = ['divanparser.spiders']
NEWSPIDER_MODULE = 'divanparser.spiders'

FEED_FORMAT = 'csv'
FEED_URI = 'divan_parser.csv'
FEED_EXPORT_ENCODING = 'utf-8'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'