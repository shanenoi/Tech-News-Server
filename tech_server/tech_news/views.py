from article_manager import Article
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

import json

articles = Article('/home/pinkcat/Desktop/Tech-News-Server/article_database/articles.db')
STEP = 5


class News(View):

    def get(self, request):
        articles.select(1, STEP)
        articles.format_time('%d/%m/%Y %H:%M:%S')

        return render(
                        request,
                        'tech_news/based_news.html',
                        {
                            'list_articles': articles.result,
                            'step': STEP
                        }
                    )

    def post(self, request):
        articles.select(request.POST.get('start'), STEP)
        articles.format_time('%d/%m/%Y %H:%M:%S')

        return HttpResponse(json.dumps(articles.result))


def categories(request):
    return render(
                    request,
                    'tech_news/based_category.html',
                    {'list_tables': articles.list_table()}
                )


class Manage_cate(View):

    def get(self, request, table_name):
        articles.select_single(table_name, 1, STEP)
        articles.format_time('%d/%m/%Y %H:%M:%S')

        return render(
                        request,
                        'tech_news/based_news.html',
                        {
                            'list_articles': articles.result,
                            'step': STEP
                        }
                    )

    def post(self, request, table_name):
        articles.select_single(table_name, request.POST.get('start'), STEP)
        articles.format_time('%d/%m/%Y %H:%M:%S')

        return HttpResponse(json.dumps(articles.result))
