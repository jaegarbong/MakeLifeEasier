from requests import get
from bs4 import BeautifulSoup
from re import match
from pandas import DataFrame, concat
from datetime import datetime as dt

class DSJobScraper:
    def __init__(self):
        self.url = r"https://www.analyticsinsight.net/top-10-data-science-jobs-to-apply-for-this-week/"
        self.jobs = {}

    def scrape_jobs(self):
        try:
            response = get(self.url)

            soup = BeautifulSoup(response.content, 'html.parser')
            h4_tags = soup.find_all("h4")

            for h4_tag in h4_tags:
                strong_tag = h4_tag.find_all("strong")  # Strong is the child tag

                if len(strong_tag) >= 2:
                    strong_text = strong_tag[1].get_text(strip=True)

                    next_sibling = h4_tag.find_next_sibling()
                    if next_sibling and next_sibling.name == 'p':
                        # P is the next tag after h4 that contains the descriptions
                        details = next_sibling.text

                    self.jobs[strong_text] = details
        except Exception as e:
            print(e)

    def process_jobs(self):

        pattern = r"^(.*?)\s+at+\s+(.*?)\s+\((.*?)\)$"

        df = DataFrame()

        for k, v in self.jobs.items():
            flag = match(pattern, k)
            if flag:
                title = flag.group(1)
                company = flag.group(2)
                location = flag.group(3)
                date = dt.today().strftime("%d-%m-%Y")
                df = concat(
                    [df,
                     DataFrame({'date':[date],'title': [title], 'company': [company], 'location': [location], 'description': [v]})])
            else:
                continue

        # Write the csv file.
        df.drop_duplicates()
        df.to_csv("jobs.csv", index=False)

    def write_to_drive(self):
        pass


scraper = DSJobScraper()
scraper.scrape_jobs()
scraper.process_jobs()
