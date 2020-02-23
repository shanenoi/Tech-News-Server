from article_manager import Article
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from info import my_info

import article_manager
import json

articles = Article(article_manager.__file__.replace('article_manager.py', '../article_database/articles.db'))
STEP = 5


class News(View):

    def get(self, request):
        list_tables = articles.list_table()
        temp = {}
        for i in list_tables:
            articles.select_single(i, 0, 3)
            articles.format_time('%d/%m/%Y %H:%M:%S')
            temp[i] = articles.result

        articles.select(1, STEP)
        articles.format_time('%d/%m/%Y %H:%M:%S')

        return render(
                        request,
                        'tech_news/base_tech_index.html',
                        {
                            'list_articles': articles.result,
                            'authors': temp,
                            'step': STEP,
                            'title': "Recent News"
                        }
                    )


    def post(self, request):
        articles.select(request.POST.get('start'), STEP)
        articles.format_time('%d/%m/%Y %H:%M:%S')

        return HttpResponse(json.dumps(articles.result))


class Manage_cate(View):

    def get(self, request, table_name):
        list_tables = articles.list_table()
        list_tables.pop(list_tables.index(table_name))
        temp = {}
        for i in list_tables:
            articles.select_single(i, 0, 3)
            articles.format_time('%d/%m/%Y %H:%M:%S')
            temp[i] = articles.result

        articles.select_single(table_name, 1, STEP)
        articles.format_time('%d/%m/%Y %H:%M:%S')

        return render(
                        request,
                        'tech_news/base_tech_index.html',
                        {
                            'list_articles': articles.result,
                            'authors': temp,
                            'step': STEP,
                            'title': table_name
                        }
                    )


    def post(self, request, table_name):
        articles.select_single(table_name, request.POST.get('start'), STEP)
        articles.format_time('%d/%m/%Y %H:%M:%S')

        return HttpResponse(json.dumps(articles.result))
