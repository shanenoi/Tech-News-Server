import bs4
import re
import html
import requests


class td(object):

    def __init__(self):
        self.url = "https://topdev.vn/blog/wp-admin/admin-ajax.php?td_theme_name=Newspaper&v=7.3"
        self.categories_id = {
                'jobs': 143,
                'lap-trinh': 1,
                'career': 5,
                'hr': 7,
                'cong-nghe': 145,
                'developer-resources': 951,
        }
        self.query_params = lambda currentPage, cate_Id:{
            'action': 'td_ajax_loop',
            'loopState[sidebarPosition]': None,
            'loopState[moduleId]': 10,
            'loopState[currentPage]': currentPage,
            'loopState[max_num_pages]': 2,
            'loopState[atts][category_id]': cate_Id,
            'loopState[atts][offset]': 4,
            'loopState[ajax_pagination_infinite_stop]': 0,
            'loopState[server_reply_html_data]': None
        }

        self.__html_code = ""


    def get_html_code(self, index_page):
        
        for i in self.categories_id.values():
            self.__html_code += eval(
                requests.post(
                    self.url,
                    data=self.query_params(index_page, list(
                            self.categories_id.values()
                        )[index_page]
                    )
                ).text
            )['server_reply_html_data']


    def get_articles_attributes(self):

        if self.__html_code == "":

            self.get_html_code(0)

        self.__html_code = re.sub('<\\\/([^<>]+)>', '</\g<1>>', self.__html_code)
        soup = bs4.BeautifulSoup(self.__html_code, 'html.parser')
        for i in soup.find_all('div', {'class': 'td_module_10 td_module_wrap td-animation-stack'}):
            temp = str(i)
            
            yield {
                    'image': re.findall('src="([^"]+)"', temp)[0],
                    'title': re.findall('title="([^"]+)"', temp)[0],
                    'link': re.findall('href="([^"]+)"', temp)[0]
            }
