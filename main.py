import json
import os
import pandas as pd
from scrapegraphai.graphs import SmartScraperGraph


class Scraper:
    def __init__(self, prompt, source, config):
        self.prompt = prompt
        self.source = source
        self.config = config
        self.smart_scraper_graph = SmartScraperGraph(
            prompt=self.prompt, source=self.source, config=self.config
        )

    def run(self):
        result = self.smart_scraper_graph.run()
        return result

    def save_to_csv(self, data, filename):
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print(df)


def main():
    graph_config = {
        "llm": {
            "api_key": os.getenv("OPENAI_API_KEY"),
            "model": "openai/gpt-4o-mini",
        },
        "verbose": True,
        "headless": False,
    }

    scraper = Scraper(
        prompt="Get the title, price, availability, rating, and image URL of all books on the page. Put the results in a csv file",
        source="https://books.toscrape.com/",
        config=graph_config,
    )

    result = scraper.run()
    scraper.save_to_csv(result, "scraped_data.csv")


if __name__ == "__main__":
    main()
