import scrapy
import pandas
import io

BASE_URL = "https://www.football-data.co.uk/"


class FootballDataSpider(scrapy.Spider):
    name = "football_data"
    allowed_domains = ["football-data.co.uk"]

    start_urls = [f"{BASE_URL}/data.php"]

    def parse(self, response):
        tags = response.xpath("/html/body/table[5]/tr[2]/td[3]/table/tr").css("a")

        for tag in tags:
            url = tag.xpath("@href").get()
            if url.endswith(".php"):
                yield response.follow(f"{BASE_URL}/{url}", self.parse_country_data)
                break

    def parse_country_data(self, response):
        tags_a = response.xpath("/html/body/table[5]/tr[2]/td[3]/a")
        for tag in tags_a:
            url = tag.xpath("@href").get()
            if url.endswith(".csv"):
                yield response.follow(url, self.parse_csv)

    def parse_csv(self, response):
        buffer = io.StringIO(response.body.decode("utf-8"))
        df = pandas.read_csv(buffer)
        # remove rows where date is before 2015
        df = df[df["Date"] > "01/01/2015"]
        for row in df.iterrows():
            yield row[1].to_dict()
