import bs4
import html
import requests

class td(object):

    def __init__(self):
        
        self.url = [
            "https://topdev.vn/blog/category/jobs/",
            "https://topdev.vn/blog/category/lap-trinh/",
            "https://topdev.vn/blog/category/workshop/",
            "https://topdev.vn/blog/category/hr/",
            "https://topdev.vn/blog/category/cong-nghe/",
            "https://topdev.vn/blog/category/developer-resources/"
        ]
        self.__html_code__  = ""


    def get_html_code(self, index_category):

        self.__html_code__ = requests.get(self.url[index_category]).text


    def get_articles_attributes(self):

        if self.__html_code__ ==  "":

            self.get_html_code(0)

        soup = bs4.BeautifulSoup(
                self.__html_code__,
                "html.parser"
            )

        raw_elements = [
            i for i in soup.find_all("script")
            if 'application/ld+json' in str(i)
        ][1]
        null = None # define null value in json
        raw_article_elements = eval(raw_elements.get_text())

        for element in raw_article_elements['hasPart']:
            yield {
                "image": element['image']['url'],
                "title": html.unescape(element['headline']),
                "link": element["mainEntityOfPage"]
            }