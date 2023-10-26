from soccer_bets.spiders import FootballDataSpider
from scrapy.crawler import CrawlerProcess


process = CrawlerProcess(
    settings={
        "FEEDS": {
            "items.json": {"format": "json"},
        },
    }
)
process.crawl(FootballDataSpider)
process.start()
