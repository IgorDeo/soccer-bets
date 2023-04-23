# Scrapy Football Matches Spider
This is a Scrapy project that contains a single spider that scrapes football matches from "https://www.football-data.co.uk/" and stores each match in a MongoDB database.

## Installation
To use this project, you need to have Python and Scrapy installed on your machine. You can install them using the following commands:

```bash
pip install scrapy
```

You also need to have a MongoDB instance running on your machine or on a remote server. You can download MongoDB from the official website: https://www.mongodb.com/try/download/community

Once you have installed the prerequisites, you can clone this repository using the following command:

```bash
git clone https://github.com/your_username/scrapy-football-matches.git
```

## Usage
To use this spider, you need to create a .env file to configure the MongoDB connection. You need to set the following variables:

- `MONGODB_URI`: The URI of the MongoDB instance. Example: "mongodb://localhost:27017/"
- `MONGODB_DATABASE`: The name of the MongoDB database to use. Example: "football"


After you have configured the MongoDB connection, you can run the spider using the following command:


```bash
scrapy crawl football_matches
```
This will start the spider and scrape the football matches from "https://www.football-data.co.uk/". The scraped data will be stored in the MongoDB collection you have configured.

## Contributing
If you want to contribute to this project, you can create a pull request with your changes. Make sure to follow the PEP 8 style guide and write tests for your code.

## License
This project is licensed under the MIT License - see the LICENSE file for details.