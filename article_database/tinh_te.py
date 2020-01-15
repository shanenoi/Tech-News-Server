import bs4
import json
import re
import requests


class tinh_te(object):

    def __init__(self):

        self.url = "https://tinhte.vn/"
        self.query = "https://tinhte.vn/appforo/index.php?threads/promoted&_bdImageApiThreadThumbnailHeight=sw&_bdImageApiThreadThumbnailWidth=460&fields_include=list_item%2Cuser_is_ignored%2Ccontent.thread_id%2Ccontent.thread_title%2Ccontent.first_post.post_body_plain_text%2Ccontent.first_post.post_id%2Ccontent.first_post.post_is_liked%2Ccontent.first_post.post_like_count%2Ccontent.first_post.poster_rank%2Ccontent.first_post.poster_has_verified_badge%2Ccontent.first_post.post_body%2Ccontent.first_post.attachments%2Ccontent.first_post.post_body_html%2Ccontent.thread_image.link%2Ccontent.thread_thumbnail.link%2Ccontent.links.permalink%2Ccontent.links.posts%2Ccontent.thread_create_date%2Ccontent.creator_user_id%2Ccontent.creator_username%2Ccontent.creator_has_verified_badge%2Ccontent.links.first_poster_avatar%2Ccontent.thread_post_count%2Ccontent.thread_view_count%2Ccontent.forum.forum_id%2Ccontent.forum.forum_title%2Ccontent.forum.links.permalink%2Ccontent.thread_tags%2Ccontent.permissions%2Ccontent.user_is_ignored%2Ccontent.latest_posts&limit=17&page={}&oauth_token={}"
        self.json_code = ""
    

    def get_auth_token(self):

        return re.search(
            'oauth_token=([^"]*)"',
            self.get_raw_html()
        ).groups()[0]


    def get_raw_html(self):

        return requests.get(self.url).text


    def get_json_code(self, page_number):

        self.json_code = requests.get(
            self.query.format(
                page_number,
                self.get_auth_token()
            )
        ).text


    def get_articles_attributes(self):

        if self.json_code == "":
            self.get_json_code(0)

        true = True   # Define value when convert json
        false = False # content to dict by eval function
        obj = eval(self.json_code)
        print(obj.keys())

        for ele in obj["threads"]:
            yield {
                "image": ele["thread_image"]["link"],
                "title": ele["thread_title"],
                "link": ele["links"]["permalink"]
            }