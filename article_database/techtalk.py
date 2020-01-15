import re
import requests

class tt(object):

    def __init__(self):

        self.url = [
            "http://techtalk.vn/tech",
            "https://techtalk.vn/category/dev",
            "http://techtalk.vn/resources",
            "https://techtalk.vn/category/su-kien",
            "https://techtalk.vn/category/chuyen-gia-noi",
            "https://techtalk.vn/category/tam-su-coder",
            "https://techtalk.vn/topdev"
        ]
        self.__html_code__ = ""


    def get_html_code(self, index_category):

        self.__html_code__ = requests.get(self.url[index_category]).text


    def get_articles_attributes(self):
        
        if self.__html_code__ == "":

            self.get_html_code(0)

        result = re.findall('<a href="([^"]+)" rel="[^"]*" title="[^"]*" data-wpel-link="[^"]*"><img width="\d*" height="\d*" class="[^"]*" src="([^"]+)" alt="[^"]*" title="([^"]+)"', self.__html_code__)
        
        for element in result:
            yield {
                "image": element[1],
                "title": element[2],
                "link": element[0],
            }