import bs4
import requests


class qtm(object):

    def __init__(self):

        self.url = "https://quantrimang.com/"
        self.query = lambda number: f"?p={number}"
        self.__html_code__ = ""


    def get_html_code(self, page_number):

        self.__html_code__ = requests.get(self.url + self.query(page_number)).text


    def get_articles_attributes(self):

        if self.__html_code__ == "":

            self.get_html_code(0)
            
        soup = bs4.BeautifulSoup(
                self.__html_code__,
                "html.parser"
            )

        raw_article_elements = [
            i for i in soup.find_all("li") 
            if "listitem clearfix" in str(i)
        ]

        for element in raw_article_elements:
            yield {
                "image": element.find("img").get("data-src"),
                "title": element.find("img").get("alt"),
                "link": self.url + element.find("a").get("href")
            }